#!/bin/bash

# Claude Code Archive System - Clean Implementation
# Uses only JSONL data for accurate conversation archiving

PROJECT_LOG_DIR="$PWD/.claude/logs"
ARCHIVE_DIR="$PROJECT_LOG_DIR/archive"
CURRENT_DIR="$PROJECT_LOG_DIR/current"

# Ensure directories exist
mkdir -p "$ARCHIVE_DIR" "$CURRENT_DIR"

# Archive old session files for different session IDs
archive_old_sessions() {
    local current_session_id="$1"
    local timestamp=$(date '+%Y%m%d_%H%M%S')
    
    # Find existing conversation files and archive them
    for conv_file in "$CURRENT_DIR"/convo-*.md; do
        if [ -f "$conv_file" ]; then
            local filename=$(basename "$conv_file")
            # Move to archive with additional timestamp suffix
            local archive_name="${filename%.md}_archived_${timestamp}.md"
            local archive_path="$ARCHIVE_DIR/$archive_name"
            
            mv "$conv_file" "$archive_path" 2>/dev/null && \
                echo "📦 Archived old conversation: $archive_path"
        fi
    done
}

# Generate current session archive
archive_current_session() {
    local project_name=$(basename "$PWD")
    
    echo "🗂️  Archiving current Claude Code session..."
    
    # Get session data from JSONL
    local summary_output
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    summary_output=$(python3 "$script_dir/claude_jsonl_logger.py" --summary 2>/dev/null)
    
    if [ $? -eq 0 ] && [ -n "$summary_output" ]; then
        # Parse session info
        local session_id=$(echo "$summary_output" | grep "Session:" | cut -d' ' -f2)
        local message_count=$(echo "$summary_output" | grep "Messages:" | cut -d' ' -f2)
        local total_tokens=$(echo "$summary_output" | grep "Total Tokens:" | cut -d' ' -f3 | tr -d ',')
        local estimated_cost=$(echo "$summary_output" | grep "Estimated Cost:" | cut -d'$' -f2)
        
        # Archive old sessions before creating new one
        archive_old_sessions "$session_id"
        
        # Create timestamp-based file names
        local timestamp=$(date '+%Y%m%d_%H%M%S')
        local conversation_file="$CURRENT_DIR/convo-$timestamp.md"
        
        # Generate full conversation archive
        python3 "$script_dir/claude_jsonl_logger.py" -o "$conversation_file" 2>/dev/null
        
        if [ -f "$conversation_file" ]; then
            echo "✅ Session archived:"
            echo "   💬 Conversation: $conversation_file"
            echo "   📈 Stats: $message_count messages, $total_tokens tokens, \$$estimated_cost"
            echo "   🆔 Session ID: $session_id"
        else
            echo "❌ Failed to generate conversation archive"
        fi
    else
        echo "⚠️  No JSONL data available - creating basic archive"
        
        local basic_file="$CURRENT_DIR/session_summary.md"
        cat > "$basic_file" << EOF
# Current Session Summary

**Project**: $project_name  
**Date**: $(date '+%Y-%m-%d %H:%M:%S')  
**Status**: Basic archive (JSONL data unavailable)

## Try Manual Commands
\`\`\`bash
python3 .claude/scripts/claude_jsonl_logger.py --summary
python3 .claude/scripts/claude_jsonl_logger.py -o conversation.md
\`\`\`

---
*Generated: $(date '+%Y-%m-%d %H:%M:%S')*
EOF
        echo "Basic archive created: $basic_file"
    fi
}

# Show current session status
show_current_status() {
    echo "📋 Current Claude Code Session Status"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Look for any current conversation files
    local current_files=("$CURRENT_DIR"/convo-*.md)
    if [ -f "${current_files[0]}" ]; then
        local current_file="${current_files[0]}"
        local timestamp=$(basename "$current_file" | sed 's/convo-\(.*\)\.md/\1/')
        
        echo "**Current Session**: $timestamp"
        echo "**Conversation File**: $current_file"
        echo "**File Size**: $(du -h "$current_file" | cut -f1)"
        echo "**Last Modified**: $(stat -c '%y' "$current_file" 2>/dev/null || stat -f '%Sm' "$current_file")"
        echo ""
        echo "## Quick Actions"
        echo "- View: \`cat \"$current_file\"\`"
        echo "- Open: \`open \"$current_file\"\`"
        echo "- Archive: \`$0 archive\`"
    else
        echo "No current session conversation found."
        echo ""
        echo "Run: $0 archive"
    fi
    
    echo ""
    echo "📁 Archive Location: $PROJECT_LOG_DIR"
}

# List archived sessions
list_archives() {
    echo "🗃️  Archived Claude Code Sessions"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if [ -d "$ARCHIVE_DIR" ] && [ "$(ls -A "$ARCHIVE_DIR" 2>/dev/null)" ]; then
        echo "Recent archived conversations:"
        
        # Show session-based archives first
        ls -t "$ARCHIVE_DIR"/convo-*_*.md 2>/dev/null | head -5 | while read -r file; do
            if [ -f "$file" ]; then
                local basename_file=$(basename "$file")
                local session_part=$(echo "$basename_file" | sed 's/convo-\([^_]*\)_.*\.md/\1/')
                local date_part=$(echo "$basename_file" | grep -o '[0-9]\{8\}_[0-9]\{6\}')
                local readable_date=$(echo "$date_part" | sed 's/_/ /' | sed 's/\([0-9]\{4\}\)\([0-9]\{2\}\)\([0-9]\{2\}\) \([0-9]\{2\}\)\([0-9]\{2\}\)\([0-9]\{2\}\)/\1-\2-\3 \4:\5:\6/')
                echo "  🆔 ${session_part:0:8}... archived on $readable_date"
            fi
        done
        
        # Show legacy timestamp-based archives
        ls -t "$ARCHIVE_DIR"/conversation_*.md 2>/dev/null | head -3 | while read -r file; do
            if [ -f "$file" ]; then
                local basename_file=$(basename "$file")
                local date_part=$(echo "$basename_file" | grep -o '[0-9]\{8\}_[0-9]\{6\}')
                local readable_date=$(echo "$date_part" | sed 's/_/ /' | sed 's/\([0-9]\{4\}\)\([0-9]\{2\}\)\([0-9]\{2\}\) \([0-9]\{2\}\)\([0-9]\{2\}\)\([0-9]\{2\}\)/\1-\2-\3 \4:\5:\6/')
                echo "  📅 Legacy archive from $readable_date"
            fi
        done
        
        echo ""
        echo "Archive directory: $ARCHIVE_DIR"
    else
        echo "No archived sessions found."
    fi
}

# Clean up old blank logs
cleanup_blank_logs() {
    echo "🧹 Cleaning up blank conversation logs..."
    
    # Find and remove blank log files (typically 53 bytes with just timestamp and empty content)
    local blank_files=$(find "$PROJECT_LOG_DIR" -name "*_full.log" -size -100c 2>/dev/null)
    
    if [ -n "$blank_files" ]; then
        echo "Found blank log files:"
        echo "$blank_files"
        
        echo "$blank_files" | while read -r file; do
            if [ -f "$file" ]; then
                rm "$file"
                echo "  🗑️  Removed: $(basename "$file")"
            fi
        done
    else
        echo "No blank log files found."
    fi
}

# Show help
show_help() {
    echo "Claude Code Archive System"
    echo "Session-based conversation archiving using JSONL data"
    echo ""
    echo "Usage: $0 {archive|status|list|cleanup|help}"
    echo ""
    echo "Commands:"
    echo "  archive  - Archive current session with session ID-based naming"
    echo "  status   - Show current active session and file details"
    echo "  list     - List archived sessions (both session-based and legacy)"
    echo "  cleanup  - Remove blank/broken log files"
    echo "  help     - Show this help"
    echo ""
    echo "File Structure:"
    echo "  Current:  $CURRENT_DIR/convo-<timestamp>.md"
    echo "  Archive:  $ARCHIVE_DIR/convo-<timestamp>_archived_<timestamp>.md"
    echo "  Logs:     $PROJECT_LOG_DIR"
}

# Main command handler
case "$1" in
    "archive")
        archive_current_session
        ;;
    "status")
        show_current_status
        ;;
    "list")
        list_archives
        ;;
    "cleanup")
        cleanup_blank_logs
        ;;
    "help"|"--help"|"-h"|"")
        show_help
        ;;
    *)
        show_help
        exit 1
        ;;
esac