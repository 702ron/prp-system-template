#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""
Pre-Compact Hook for Claude Code
Automatically generates a conversation summary before the conversation is compacted.
This preserves the full context and learning from the session.
"""

import json
import sys
import subprocess
import os
from pathlib import Path
from datetime import datetime

def generate_conversation_summary():
    """Generate a conversation summary before compacting."""
    try:
        # Run the summary generator script
        script_path = Path(__file__).parent.parent / "scripts" / "conversation_summary_generator.py"
        
        if not script_path.exists():
            print("⚠️  Summary generator script not found, skipping summary generation", file=sys.stderr)
            return
        
        result = subprocess.run(
            ['uv', 'run', str(script_path), '--trigger', 'pre-compact'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if result.returncode == 0:
            print("📋 Conversation summary generated before compacting", file=sys.stderr)
            if result.stdout:
                print(result.stdout.strip(), file=sys.stderr)
        else:
            print(f"⚠️  Summary generation failed: {result.stderr}", file=sys.stderr)
            
    except Exception as e:
        print(f"Error generating summary: {e}", file=sys.stderr)

def main():
    try:
        # Read input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Log the pre-compact event
        session_id = input_data.get('session_id', 'unknown')
        timestamp = datetime.now().isoformat()
        
        # Create logs directory if it doesn't exist
        logs_dir = Path(os.getcwd()) / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        # Log the pre-compact event
        compact_log = logs_dir / "compact_events.json"
        compact_events = []
        
        if compact_log.exists():
            try:
                with open(compact_log, 'r') as f:
                    compact_events = json.load(f)
            except (json.JSONDecodeError, IOError):
                compact_events = []
        
        compact_events.append({
            'timestamp': timestamp,
            'session_id': session_id,
            'hook_event_name': input_data.get('hook_event_name', 'PreCompact'),
            'action': 'conversation_summary_generated'
        })
        
        with open(compact_log, 'w') as f:
            json.dump(compact_events, f, indent=2)
        
        # Generate the conversation summary
        print("📋 Generating conversation summary before compacting...", file=sys.stderr)
        generate_conversation_summary()
        
        # Exit successfully
        sys.exit(0)
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(0)
        
    except Exception as e:
        print(f"Error in pre-compact hook: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()