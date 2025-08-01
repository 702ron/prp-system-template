#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""
Stop Hook for Claude Code
Automatically archives the conversation with full token usage when Claude stops responding.
"""

import json
import sys
import subprocess
import os
from pathlib import Path
from datetime import datetime

def run_archive_command():
    """Run the claude-archive command to save conversation data."""
    try:
        # Run the archive script from project directory
        script_path = Path(__file__).parent.parent / "scripts" / "claude_archive_system.sh"
        result = subprocess.run(
            ['bash', str(script_path), 'archive'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if result.returncode == 0:
            print(f"✅ Conversation archived successfully", file=sys.stderr)
            if result.stdout:
                print(result.stdout.strip(), file=sys.stderr)
        else:
            print(f"⚠️  Archive command failed: {result.stderr}", file=sys.stderr)
            
    except Exception as e:
        print(f"Error running archive: {e}", file=sys.stderr)

def main():
    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Check if this is a recursive stop hook call
        if input_data.get('stop_hook_active', False):
            # Don't trigger archive again if we're already in a stop hook
            sys.exit(0)
        
        # Log the stop event
        session_id = input_data.get('session_id', 'unknown')
        timestamp = datetime.now().isoformat()
        
        # Create logs directory if it doesn't exist
        logs_dir = Path(os.getcwd()) / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        # Log the stop event
        stop_log = logs_dir / "stop_events.json"
        stop_events = []
        
        if stop_log.exists():
            try:
                with open(stop_log, 'r') as f:
                    stop_events = json.load(f)
            except:
                stop_events = []
        
        stop_events.append({
            'timestamp': timestamp,
            'session_id': session_id,
            'hook_event_name': input_data.get('hook_event_name', 'Stop')
        })
        
        with open(stop_log, 'w') as f:
            json.dump(stop_events, f, indent=2)
        
        # Run the archive command
        print("🗂️  Archiving conversation with token usage...", file=sys.stderr)
        run_archive_command()
        
        # Exit successfully
        sys.exit(0)
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(0)
        
    except Exception as e:
        print(f"Error in stop hook: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()