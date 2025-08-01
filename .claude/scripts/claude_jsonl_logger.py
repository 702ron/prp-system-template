#!/usr/bin/env python3

"""
Claude Code JSONL Logger
Reads Claude's native JSONL files to extract conversations and token usage
Based on the approach from Claude-Code-Usage-Monitor
"""

import json
import os
import glob
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any
import argparse
import sys

class ClaudeConversationLogger:
    def __init__(self, projects_path: str = None):
        self.projects_path = projects_path or os.path.expanduser("~/.claude/projects")
        self.current_project = self.detect_current_project()
        
    def detect_current_project(self) -> Optional[str]:
        """Detect current project based on working directory"""
        cwd = os.getcwd()
        # Convert path to Claude's naming convention
        project_name = cwd.replace('/', '-')
        if project_name.startswith('-'):
            project_name = project_name[1:]
        
        project_dir = os.path.join(self.projects_path, f"-{project_name}")
        if os.path.exists(project_dir):
            return project_dir
        
        # Fallback: find most recent project directory
        try:
            project_dirs = [d for d in os.listdir(self.projects_path) 
                          if os.path.isdir(os.path.join(self.projects_path, d))]
            if project_dirs:
                # Sort by modification time, return most recent
                project_dirs.sort(key=lambda x: os.path.getmtime(os.path.join(self.projects_path, x)), reverse=True)
                return os.path.join(self.projects_path, project_dirs[0])
        except OSError:
            pass
        
        return None
    
    def find_jsonl_files(self, project_dir: str = None) -> List[str]:
        """Find all JSONL files in project directory"""
        target_dir = project_dir or self.current_project
        if not target_dir or not os.path.exists(target_dir):
            return []
        
        pattern = os.path.join(target_dir, "*.jsonl")
        return glob.glob(pattern)
    
    def parse_jsonl_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Parse JSONL file line by line"""
        entries = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        entry = json.loads(line)
                        entries.append(entry)
                    except json.JSONDecodeError as e:
                        print(f"Warning: Malformed JSON on line {line_num} in {file_path}: {e}", file=sys.stderr)
                        continue
        except IOError as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
        
        return entries
    
    def extract_conversation_data(self, entries: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract conversation data and token usage from JSONL entries"""
        conversation = {
            'session_id': None,
            'messages': [],
            'total_tokens': {
                'input_tokens': 0,
                'output_tokens': 0,
                'cache_creation_input_tokens': 0,
                'cache_read_input_tokens': 0,
                'total': 0
            },
            'start_time': None,
            'end_time': None,
            'project_path': None,
            'git_branch': None
        }
        
        for entry in entries:
            # Extract session metadata
            if not conversation['session_id'] and 'sessionId' in entry:
                conversation['session_id'] = entry['sessionId']
            
            if not conversation['project_path'] and 'cwd' in entry:
                conversation['project_path'] = entry['cwd']
                
            if not conversation['git_branch'] and 'gitBranch' in entry:
                conversation['git_branch'] = entry['gitBranch']
            
            # Track timestamps
            if 'timestamp' in entry:
                timestamp = entry['timestamp']
                if not conversation['start_time'] or timestamp < conversation['start_time']:
                    conversation['start_time'] = timestamp
                if not conversation['end_time'] or timestamp > conversation['end_time']:
                    conversation['end_time'] = timestamp
            
            # Extract messages
            if 'message' in entry:
                msg = entry['message']
                message_data = {
                    'timestamp': entry.get('timestamp'),
                    'role': msg.get('role'),
                    'content': self.extract_content(msg.get('content', '')),
                    'type': entry.get('type'),
                    'uuid': entry.get('uuid')
                }
                
                # Extract token usage from assistant messages
                if 'usage' in msg:
                    usage = msg['usage']
                    message_data['token_usage'] = usage
                    
                    # Add to totals
                    conversation['total_tokens']['input_tokens'] += usage.get('input_tokens', 0)
                    conversation['total_tokens']['output_tokens'] += usage.get('output_tokens', 0)
                    conversation['total_tokens']['cache_creation_input_tokens'] += usage.get('cache_creation_input_tokens', 0)
                    conversation['total_tokens']['cache_read_input_tokens'] += usage.get('cache_read_input_tokens', 0)
                
                conversation['messages'].append(message_data)
        
        # Calculate total tokens
        conversation['total_tokens']['total'] = sum([
            conversation['total_tokens']['input_tokens'],
            conversation['total_tokens']['output_tokens'],
            conversation['total_tokens']['cache_creation_input_tokens'],
            conversation['total_tokens']['cache_read_input_tokens']
        ])
        
        return conversation
    
    def extract_content(self, content) -> str:
        """Extract readable content from message content"""
        if isinstance(content, str):
            return content
        elif isinstance(content, list):
            # Handle tool use and text content
            text_parts = []
            for item in content:
                if isinstance(item, dict):
                    if item.get('type') == 'text':
                        text_parts.append(item.get('text', ''))
                    elif item.get('type') == 'tool_use':
                        tool_name = item.get('name', 'unknown_tool')
                        text_parts.append(f"[TOOL: {tool_name}]")
                    elif item.get('type') == 'tool_result':
                        text_parts.append("[TOOL_RESULT]")
            return ' '.join(text_parts)
        return str(content)
    
    def estimate_cost(self, total_tokens: int, model: str = "claude-sonnet-4") -> float:
        """Estimate cost based on token usage"""
        # Sonnet 4 pricing: ~$3 per 1M tokens (approximate)
        cost_per_million = 3.0
        return (total_tokens * cost_per_million) / 1_000_000
    
    def generate_conversation_log(self, conversation: Dict[str, Any], output_file: str = None) -> str:
        """Generate human-readable conversation log"""
        if not output_file:
            session_id = conversation.get('session_id', 'unknown')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"conversation_{session_id}_{timestamp}.log"
        
        log_content = []
        
        # Header
        log_content.append(f"# Claude Code Conversation Log")
        log_content.append(f"Session ID: {conversation.get('session_id', 'Unknown')}")
        log_content.append(f"Project: {conversation.get('project_path', 'Unknown')}")
        log_content.append(f"Git Branch: {conversation.get('git_branch', 'Unknown')}")
        log_content.append(f"Start Time: {conversation.get('start_time', 'Unknown')}")
        log_content.append(f"End Time: {conversation.get('end_time', 'Unknown')}")
        log_content.append("")
        
        # Token usage summary
        tokens = conversation['total_tokens']
        log_content.append(f"## Token Usage Summary")
        log_content.append(f"- Input Tokens: {tokens['input_tokens']:,}")
        log_content.append(f"- Output Tokens: {tokens['output_tokens']:,}")
        log_content.append(f"- Cache Creation: {tokens['cache_creation_input_tokens']:,}")
        log_content.append(f"- Cache Read: {tokens['cache_read_input_tokens']:,}")
        log_content.append(f"- **Total Tokens: {tokens['total']:,}**")
        log_content.append(f"- **Estimated Cost: ${self.estimate_cost(tokens['total']):.6f}**")
        log_content.append("")
        
        # Conversation
        log_content.append(f"## Conversation ({len(conversation['messages'])} messages)")
        log_content.append("")
        
        for i, msg in enumerate(conversation['messages'], 1):
            timestamp = msg.get('timestamp', 'Unknown')
            role = msg.get('role', 'unknown').upper()
            content = msg.get('content', '')
            
            # Format timestamp
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            except (ValueError, AttributeError):
                formatted_time = timestamp
            
            log_content.append(f"### Message {i} - {role} [{formatted_time}]")
            
            # Add token usage info for assistant messages
            if 'token_usage' in msg:
                usage = msg['token_usage']
                log_content.append(f"*Tokens: {usage.get('input_tokens', 0)} in + {usage.get('output_tokens', 0)} out*")
            
            log_content.append("")
            
            # Content (truncate if very long)
            if len(content) > 2000:
                log_content.append(f"{content[:2000]}...")
                log_content.append(f"*[Content truncated - {len(content)} total characters]*")
            else:
                log_content.append(content)
            
            log_content.append("")
            log_content.append("---")
            log_content.append("")
        
        log_text = '\n'.join(log_content)
        
        # Write to file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(log_text)
            return output_file
        except IOError as e:
            print(f"Error writing to {output_file}: {e}", file=sys.stderr)
            return None
    
    def process_current_project(self, hours_back: int = 24) -> Optional[Dict[str, Any]]:
        """Process current project's conversation data"""
        if not self.current_project:
            print("No current project detected", file=sys.stderr)
            return None
        
        jsonl_files = self.find_jsonl_files()
        if not jsonl_files:
            print("No JSONL files found in current project", file=sys.stderr)
            return None
        
        print(f"Found {len(jsonl_files)} JSONL files in {self.current_project}")
        
        # Process most recent file (or combine all files)
        latest_file = max(jsonl_files, key=os.path.getmtime)
        print(f"Processing: {latest_file}")
        
        entries = self.parse_jsonl_file(latest_file)
        if not entries:
            print("No valid entries found", file=sys.stderr)
            return None
        
        conversation = self.extract_conversation_data(entries)
        return conversation

def main():
    parser = argparse.ArgumentParser(description='Claude Code Conversation Logger')
    parser.add_argument('--projects-path', help='Path to Claude projects directory')
    parser.add_argument('--output', '-o', help='Output file for conversation log')
    parser.add_argument('--json', action='store_true', help='Output as JSON instead of readable log')
    parser.add_argument('--summary', action='store_true', help='Show summary only')
    
    args = parser.parse_args()
    
    logger = ClaudeConversationLogger(args.projects_path)
    conversation = logger.process_current_project()
    
    if not conversation:
        print("No conversation data found", file=sys.stderr)
        sys.exit(1)
    
    if args.summary:
        tokens = conversation['total_tokens']
        print(f"Session: {conversation.get('session_id', 'Unknown')}")
        print(f"Messages: {len(conversation['messages'])}")
        print(f"Total Tokens: {tokens['total']:,}")
        print(f"Estimated Cost: ${logger.estimate_cost(tokens['total']):.6f}")
    elif args.json:
        print(json.dumps(conversation, indent=2, default=str))
    else:
        output_file = logger.generate_conversation_log(conversation, args.output)
        if output_file:
            print(f"Conversation log written to: {output_file}")

if __name__ == "__main__":
    main()