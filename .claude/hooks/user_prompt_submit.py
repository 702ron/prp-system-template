#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""
Enhanced UserPromptSubmit Hook for Claude Code
Creates project-level logs, optimizes prompts for token efficiency,
and provides smart model routing for simple queries.
"""

import json
import sys
import os
import re
from pathlib import Path
from datetime import datetime, timezone

def ensure_project_logs_dir():
    """Ensure the project-level logs directory exists."""
    # Get the current working directory (project root)
    project_root = Path(os.getcwd())
    logs_dir = project_root / "logs"
    
    # Create logs directory if it doesn't exist
    logs_dir.mkdir(exist_ok=True)
    
    return logs_dir

class PromptOptimizer:
    """Optimize prompts for token efficiency and smart routing."""
    
    def __init__(self):
        self.simple_query_patterns = [
            r'^(what|how|why|when|where|who)\s+.*\?$',
            r'^(is|are|can|will|would|should)\s+.*\?$',
            r'^(explain|define|describe)\s+.*$',
            r'^(help|show|tell)\s+(me\s+)?.*$',
            r'^\w+\s*\+\s*\w+$',  # Simple math
            r'^ls$|^pwd$|^date$',  # Simple commands
        ]
        
        self.compression_patterns = [
            (r'\s+', ' '),  # Multiple spaces to single
            (r'\n\s*\n\s*\n+', '\n\n'),  # Multiple newlines to double
            (r'(very|really|quite|extremely|incredibly)\s+', ''),  # Remove intensifiers
            (r'\b(um|uh|well|you know|like)\b\s*', ''),  # Remove filler words
        ]
    
    def is_simple_query(self, prompt):
        """Check if prompt is a simple query that could use Haiku."""
        prompt_clean = prompt.strip().lower()
        
        # Check length - simple queries are usually short
        if len(prompt_clean) > 200:
            return False
        
        # Check against patterns
        for pattern in self.simple_query_patterns:
            if re.match(pattern, prompt_clean, re.IGNORECASE):
                return True
        
        return False
    
    def compress_prompt(self, prompt):
        """Compress prompt by removing redundancy and filler."""
        compressed = prompt
        
        for pattern, replacement in self.compression_patterns:
            compressed = re.sub(pattern, replacement, compressed, flags=re.MULTILINE)
        
        return compressed.strip()
    
    def should_add_context(self, prompt):
        """Determine if we should add cached context to avoid re-reading files."""
        context_keywords = ['implement', 'create', 'build', 'modify', 'update', 'fix', 'refactor']
        prompt_lower = prompt.lower()
        
        return any(keyword in prompt_lower for keyword in context_keywords)
    
    def get_cached_context(self):
        """Get recently cached file context to avoid re-reading."""
        try:
            cache_dir = Path(os.getcwd()) / ".claude" / "cache"
            file_cache_path = cache_dir / "file_cache.json"
            
            if not file_cache_path.exists():
                return ""
            
            with open(file_cache_path, 'r') as f:
                cache_data = json.load(f)
            
            # Get most recent 3 cached files as context
            recent_files = []
            for cache_key, cache_entry in cache_data.items():
                if 'timestamp' in cache_entry and 'file_path' in cache_entry:
                    cache_time = datetime.fromisoformat(cache_entry['timestamp'])
                    if (datetime.now() - cache_time).total_seconds() < 300:  # 5 minutes
                        recent_files.append({
                            'path': cache_entry['file_path'],
                            'time': cache_time,
                            'size': len(cache_entry.get('content', ''))
                        })
            
            if recent_files:
                recent_files.sort(key=lambda x: x['time'], reverse=True)
                context_files = recent_files[:3]
                
                context = "\n\nRecent file context (cached):\n"
                for file_info in context_files:
                    context += f"- {file_info['path']} ({file_info['size']} chars)\n"
                
                return context
            
        except Exception:
            pass
        
        return ""

def log_user_prompt(input_data, logs_dir, optimizer):
    """Log the user prompt and apply optimizations."""
    session_id = input_data.get('session_id', 'unknown')
    original_prompt = input_data.get('prompt', '')
    timestamp = input_data.get('timestamp', datetime.now(timezone.utc).isoformat())
    
    # Analyze and optimize prompt
    is_simple = optimizer.is_simple_query(original_prompt) 
    compressed_prompt = optimizer.compress_prompt(original_prompt)
    should_add_context = optimizer.should_add_context(original_prompt)
    
    # Calculate token savings
    original_length = len(original_prompt)
    compressed_length = len(compressed_prompt)
    token_savings = original_length - compressed_length
    
    # Create daily log file
    today = datetime.now().strftime('%Y-%m-%d')
    log_file = logs_dir / f"user_prompts_{today}.json"
    
    # Load existing log data or create new
    if log_file.exists():
        try:
            with open(log_file, 'r') as f:
                log_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            log_data = []
    else:
        log_data = []
    
    # Add new prompt entry with optimization data
    log_entry = {
        'timestamp': timestamp,
        'session_id': session_id,
        'original_prompt': original_prompt,
        'compressed_prompt': compressed_prompt,
        'cwd': input_data.get('cwd', ''),
        'original_length': original_length,
        'compressed_length': compressed_length,
        'token_savings': token_savings,
        'is_simple_query': is_simple,
        'compression_ratio': round(token_savings / original_length * 100, 2) if original_length > 0 else 0,
        'optimization_applied': token_savings > 0
    }
    
    log_data.append(log_entry)
    
    # Write back to file
    try:
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
    except IOError as e:
        print(f"Warning: Could not write to log file: {e}", file=sys.stderr)
    
    return compressed_prompt, is_simple, should_add_context

def main():
    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Check if optimizations are disabled for this session
        disable_flag = Path(os.getcwd()) / ".claude" / ".optimization_disabled"
        optimization_disabled = disable_flag.exists()
        
        # Ensure logs directory exists
        logs_dir = ensure_project_logs_dir()
        
        # Initialize optimizer
        optimizer = PromptOptimizer()
        
        # Log and optimize the prompt (but skip optimization if disabled)
        if optimization_disabled:
            # Just log without optimization
            session_id = input_data.get('session_id', 'unknown')
            original_prompt = input_data.get('prompt', '')
            timestamp = input_data.get('timestamp', datetime.now(timezone.utc).isoformat())
            
            today = datetime.now().strftime('%Y-%m-%d')
            log_file = logs_dir / f"user_prompts_{today}.json"
            
            if log_file.exists():
                try:
                    with open(log_file, 'r') as f:
                        log_data = json.load(f)
                except (json.JSONDecodeError, IOError):
                    log_data = []
            else:
                log_data = []
            
            log_entry = {
                'timestamp': timestamp,
                'session_id': session_id,
                'original_prompt': original_prompt,
                'cwd': input_data.get('cwd', ''),
                'original_length': len(original_prompt),
                'optimization_disabled': True,
                'baseline_mode': True
            }
            
            log_data.append(log_entry)
            
            try:
                with open(log_file, 'w') as f:
                    json.dump(log_data, f, indent=2)
            except IOError:
                pass
            
            print("🚫 Optimization disabled - baseline mode", file=sys.stderr)
            sys.exit(0)
        
        # Normal optimization path
        compressed_prompt, is_simple, should_add_context = log_user_prompt(input_data, logs_dir, optimizer)
        
        # Create optimized prompt data
        optimization_data = {
            'original_prompt': input_data.get('prompt', ''),
            'compressed_prompt': compressed_prompt,
            'is_simple_query': is_simple,
            'token_savings': len(input_data.get('prompt', '')) - len(compressed_prompt),
            'should_add_context': should_add_context
        }
        
        # Add cached context if needed
        if should_add_context:
            cached_context = optimizer.get_cached_context()
            if cached_context:
                optimization_data['added_context'] = cached_context
                compressed_prompt += cached_context
        
        # Output optimization information for logging
        if optimization_data['token_savings'] > 0:
            print(f"🔧 Prompt optimized: {optimization_data['token_savings']} chars saved", file=sys.stderr)
        
        if is_simple:
            print(f"💡 Simple query detected - consider using Haiku model", file=sys.stderr)
        
        # Update the prompt in input_data if significantly compressed
        if optimization_data['token_savings'] > 10:  # Only if meaningful savings
            input_data['prompt'] = compressed_prompt
            # Output the modified input data
            print(json.dumps(input_data))
        
        # Exit successfully (allows prompt to proceed)
        sys.exit(0)
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(0)  # Fail open - don't block user on parsing errors
        
    except Exception as e:
        print(f"Error in user prompt hook: {e}", file=sys.stderr)
        sys.exit(0)  # Fail open - don't block user on unexpected errors

if __name__ == "__main__":
    main()