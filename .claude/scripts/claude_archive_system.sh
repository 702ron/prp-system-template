#!/bin/bash

# Claude Code Archive System - Clean Implementation
# Uses only JSONL data for accurate conversation archiving

PROJECT_LOG_DIR="$PWD/.claude/logs"
ARCHIVE_DIR="$PROJECT_LOG_DIR/archive"
CURRENT_DIR="$PROJECT_LOG_DIR/current"

# Ensure directories exist
mkdir -p "$ARCHIVE_DIR" "$CURRENT_DIR"

# Generate current session archive
archive_current_session() {
    local timestamp=$(date '+%Y%m%d_%H%M%S')
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
        
        # Create session summary
        local summary_file="$CURRENT_DIR/session_summary.md"
        cat > "$summary_file" << EOF
# Current Session Summary

**Session ID**: $session_id  
**Project**: $project_name  
**Date**: $(date '+%Y-%m-%d %H:%M:%S')  
**Messages**: $message_count  
**Tokens**: $(printf "%'d" $total_tokens 2>/dev/null || echo $total_tokens)  
**Cost**: \$$estimated_cost  

## Quick Actions
- [View Full Conversation](#view-conversation)
- [Export Archive](#export-archive)
- [Resume Context](#resume-context)

---
*Updated: $(date '+%Y-%m-%d %H:%M:%S')*
EOF
        
        # Generate full conversation archive
        local conversation_file="$CURRENT_DIR/full_conversation.md"
        python3 "$script_dir/claude_jsonl_logger.py" -o "$conversation_file" 2>/dev/null
        
        if [ -f "$conversation_file" ]; then
            echo "✅ Session archived:"
            echo "   📊 Summary: $summary_file"
            echo "   💬 Conversation: $conversation_file"
            echo "   📈 Stats: $message_count messages, $total_tokens tokens, \$$estimated_cost"
            
            # Create archived copy with timestamp
            cp "$summary_file" "$ARCHIVE_DIR/session_${timestamp}_summary.md"
            cp "$conversation_file" "$ARCHIVE_DIR/conversation_${timestamp}.md"
            
            echo "   🗃️  Archived copies created in $ARCHIVE_DIR"
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
    
    if [ -f "$CURRENT_DIR/session_summary.md" ]; then
        cat "$CURRENT_DIR/session_summary.md"
    else
        echo "No current session archive found."
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
        echo "Recent archives:"
        ls -t "$ARCHIVE_DIR"/*summary.md 2>/dev/null | head -5 | while read -r file; do
            if [ -f "$file" ]; then
                local basename_file=$(basename "$file")
                local date_part=$(echo "$basename_file" | grep -o '[0-9]\{8\}_[0-9]\{6\}')
                local readable_date=$(echo "$date_part" | sed 's/_/ /' | sed 's/\([0-9]\{4\}\)\([0-9]\{2\}\)\([0-9]\{2\}\) \([0-9]\{2\}\)\([0-9]\{2\}\)\([0-9]\{2\}\)/\1-\2-\3 \4:\5:\6/')
                echo "  📅 $readable_date"
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
    echo "Clean implementation using JSONL data only"
    echo ""
    echo "Usage: $0 {archive|status|list|cleanup|help}"
    echo ""
    echo "Commands:"
    echo "  archive  - Archive current session with real data"
    echo "  status   - Show current session status and summary"
    echo "  list     - List archived sessions"
    echo "  cleanup  - Remove blank/broken log files"
    echo "  help     - Show this help"
    echo ""
    echo "Files stored in: $PROJECT_LOG_DIR"
    echo "Current session: $CURRENT_DIR"
    echo "Archives: $ARCHIVE_DIR"
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