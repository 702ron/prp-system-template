#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""
PostToolUse Hook for Claude Code
Logs tool usage for monitoring and creates periodic token summaries.
"""

import json
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime

def get_current_token_usage():
    """Get current token usage from Claude's JSONL logs."""
    try:
        # Use the logger script from project directory
        script_path = Path(__file__).parent.parent / "scripts" / "claude_jsonl_logger.py"
        result = subprocess.run(
            ['python3', str(script_path), '--summary'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if result.returncode == 0 and result.stdout:
            return result.stdout.strip()
        return None
    except:
        return None

def log_tool_usage(input_data, logs_dir):
    """Log tool usage to daily file."""
    tool_name = input_data.get('tool_name', 'unknown')
    tool_input = input_data.get('tool_input', {})
    tool_response = input_data.get('tool_response', {})
    timestamp = datetime.now().isoformat()
    
    # Create daily tool usage log
    today = datetime.now().strftime('%Y-%m-%d')
    tool_log_file = logs_dir / f"tool_usage_{today}.json"
    
    # Load existing log or create new
    if tool_log_file.exists():
        try:
            with open(tool_log_file, 'r') as f:
                tool_logs = json.load(f)
        except:
            tool_logs = []
    else:
        tool_logs = []
    
    # Add new entry
    tool_logs.append({
        'timestamp': timestamp,
        'session_id': input_data.get('session_id', 'unknown'),
        'tool_name': tool_name,
        'success': tool_response.get('success', True) if isinstance(tool_response, dict) else True
    })
    
    # Write back
    with open(tool_log_file, 'w') as f:
        json.dump(tool_logs, f, indent=2)
    
    # Update token summary periodically (every 10 tool uses)
    if len(tool_logs) % 10 == 0:
        update_token_summary(logs_dir)

def update_token_summary(logs_dir):
    """Update the token usage summary file."""
    token_usage = get_current_token_usage()
    if not token_usage:
        return
    
    summary_file = logs_dir / "token_summary.txt"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(summary_file, 'w') as f:
        f.write(f"Last Updated: {timestamp}\n")
        f.write("-" * 40 + "\n")
        f.write(token_usage)
        f.write("\n" + "-" * 40 + "\n")
        f.write(f"Log Location: {logs_dir}\n")

def main():
    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Ensure logs directory exists
        logs_dir = Path(os.getcwd()) / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        # Log tool usage
        log_tool_usage(input_data, logs_dir)
        
        # Exit successfully
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Silently fail - don't block tools
        sys.exit(0)
        
    except Exception:
        # Silently fail - don't block tools
        sys.exit(0)

if __name__ == "__main__":
    main()