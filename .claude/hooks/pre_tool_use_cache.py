#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""
PreToolUse Cache Hook for Claude Code
Implements smart caching to reduce token usage by avoiding redundant operations.
"""

import json
import sys
import os
import hashlib
import time
from pathlib import Path
from datetime import datetime, timedelta

class TokenOptimizationCache:
    def __init__(self):
        self.cache_dir = Path(os.getcwd()) / ".claude" / "cache"
        self.cache_dir.mkdir(exist_ok=True)
        self.file_cache_path = self.cache_dir / "file_cache.json"
        self.command_cache_path = self.cache_dir / "command_cache.json" 
        self.search_cache_path = self.cache_dir / "search_cache.json"
        
        # Cache TTL in seconds
        self.file_cache_ttl = 300  # 5 minutes for file reads
        self.command_cache_ttl = 60  # 1 minute for commands
        self.search_cache_ttl = 600  # 10 minutes for searches
        
    def load_cache(self, cache_path):
        """Load cache data from file."""
        if not cache_path.exists():
            return {}
        try:
            with open(cache_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    
    def save_cache(self, cache_path, cache_data):
        """Save cache data to file."""
        try:
            with open(cache_path, 'w') as f:
                json.dump(cache_data, f, indent=2)
        except IOError:
            pass  # Fail silently
    
    def is_cache_valid(self, cache_entry, ttl_seconds):
        """Check if cache entry is still valid."""
        if not cache_entry or 'timestamp' not in cache_entry:
            return False
        
        cached_time = datetime.fromisoformat(cache_entry['timestamp'])
        expiry_time = cached_time + timedelta(seconds=ttl_seconds)
        return datetime.now() < expiry_time
    
    def get_file_hash(self, file_path):
        """Get file modification time and size as a simple hash."""
        try:
            stat = os.stat(file_path)
            return f"{stat.st_mtime}_{stat.st_size}"
        except OSError:
            return None
    
    def should_cache_file_read(self, tool_input):
        """Check if we should cache this file read operation."""
        file_path = tool_input.get('file_path')
        if not file_path or not os.path.exists(file_path):
            return False, None
        
        # Only cache files under reasonable size (1MB)
        try:
            file_size = os.path.getsize(file_path)
            if file_size > 1024 * 1024:  # 1MB
                return False, None
        except OSError:
            return False, None
        
        file_hash = self.get_file_hash(file_path)
        if not file_hash:
            return False, None
        
        cache_key = f"{file_path}_{file_hash}"
        cache_data = self.load_cache(self.file_cache_path)
        
        if cache_key in cache_data:
            cache_entry = cache_data[cache_key]
            if self.is_cache_valid(cache_entry, self.file_cache_ttl):
                return True, cache_entry['content']
        
        return False, None
    
    def should_cache_command(self, tool_input):
        """Check if we should cache this command."""
        command = tool_input.get('command', '')
        
        # Only cache safe, deterministic commands
        safe_commands = ['ls', 'find', 'grep', 'wc', 'cat', 'head', 'tail']
        command_start = command.split()[0] if command.split() else ''
        
        if command_start not in safe_commands:
            return False, None
        
        # Don't cache commands with time-sensitive operations
        if any(keyword in command.lower() for keyword in ['date', 'time', 'ps', 'top', 'df']):
            return False, None
        
        command_hash = hashlib.md5(command.encode()).hexdigest()
        cache_data = self.load_cache(self.command_cache_path)
        
        if command_hash in cache_data:
            cache_entry = cache_data[command_hash]
            if self.is_cache_valid(cache_entry, self.command_cache_ttl):
                return True, cache_entry
        
        return False, None
    
    def should_cache_search(self, tool_input):
        """Check if we should cache this search operation."""
        pattern = tool_input.get('pattern', '')
        path = tool_input.get('path', '.')
        
        if not pattern:
            return False, None
        
        search_hash = hashlib.md5(f"{pattern}_{path}".encode()).hexdigest()
        cache_data = self.load_cache(self.search_cache_path)
        
        if search_hash in cache_data:
            cache_entry = cache_data[search_hash]
            if self.is_cache_valid(cache_entry, self.search_cache_ttl):
                return True, cache_entry['result']
        
        return False, None
    
    def cache_file_content(self, file_path, content):
        """Cache file content for future use."""
        file_hash = self.get_file_hash(file_path)
        if not file_hash:
            return
        
        cache_key = f"{file_path}_{file_hash}"
        cache_data = self.load_cache(self.file_cache_path)
        
        cache_data[cache_key] = {
            'content': content,
            'timestamp': datetime.now().isoformat(),
            'file_path': file_path
        }
        
        self.save_cache(self.file_cache_path, cache_data)
    
    def process_tool_call(self, input_data):
        """Process incoming tool call and check for cache opportunities."""
        tool_name = input_data.get('tool_name')
        tool_input = input_data.get('tool_input', {})
        
        # Handle Read tool caching
        if tool_name == 'Read':
            should_cache, cached_content = self.should_cache_file_read(tool_input)
            if should_cache:
                # Return cached response format
                return {
                    'block_tool': True,
                    'cached_response': {
                        'success': True,
                        'content': cached_content,
                        'cached': True,
                        'cache_source': 'file_cache'
                    }
                }
        
        # Handle Bash command caching
        elif tool_name == 'Bash':
            should_cache, cached_result = self.should_cache_command(tool_input)
            if should_cache:
                return {
                    'block_tool': True,
                    'cached_response': {
                        'success': True,
                        'stdout': cached_result.get('stdout', ''),
                        'stderr': cached_result.get('stderr', ''),
                        'cached': True,
                        'cache_source': 'command_cache'
                    }
                }
        
        # Handle Grep/search caching
        elif tool_name in ['Grep', 'Glob']:
            should_cache, cached_result = self.should_cache_search(tool_input)
            if should_cache:
                return {
                    'block_tool': True,
                    'cached_response': {
                        'success': True,
                        'result': cached_result,
                        'cached': True,
                        'cache_source': 'search_cache'
                    }
                }
        
        # Allow tool to proceed normally
        return {'block_tool': False}

def main():
    try:
        # Check if optimizations are disabled for this session
        disable_flag = Path(os.getcwd()) / ".claude" / ".optimization_disabled"
        if disable_flag.exists():
            # Optimizations disabled, let all tools proceed normally
            sys.exit(0)
        
        input_data = json.loads(sys.stdin.read())
        
        cache = TokenOptimizationCache()
        result = cache.process_tool_call(input_data)
        
        if result.get('block_tool'):
            # Tool is blocked, return cached response
            print(json.dumps(result['cached_response']))
            sys.exit(1)  # Block the tool
        else:
            # Let tool proceed
            sys.exit(0)
            
    except json.JSONDecodeError:
        # Invalid input, let tool proceed
        sys.exit(0)
    except Exception:
        # Any error, let tool proceed to avoid breaking workflow
        sys.exit(0)

if __name__ == "__main__":
    main()