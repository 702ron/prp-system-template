#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""
UserPromptSubmit Hook for Claude Code
Creates project-level logs and logs all user prompts for audit purposes.
"""

import json
import sys
import os
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

def log_user_prompt(input_data, logs_dir):
    """Log the user prompt to a daily log file."""
    session_id = input_data.get('session_id', 'unknown')
    prompt = input_data.get('prompt', '')
    timestamp = input_data.get('timestamp', datetime.now(timezone.utc).isoformat())
    
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
    
    # Add new prompt entry
    log_entry = {
        'timestamp': timestamp,
        'session_id': session_id,
        'prompt': prompt,
        'cwd': input_data.get('cwd', ''),
        'prompt_length': len(prompt)
    }
    
    log_data.append(log_entry)
    
    # Write back to file
    try:
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
    except IOError as e:
        print(f"Warning: Could not write to log file: {e}", file=sys.stderr)

def main():
    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Ensure logs directory exists
        logs_dir = ensure_project_logs_dir()
        
        # Log the prompt
        log_user_prompt(input_data, logs_dir)
        
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