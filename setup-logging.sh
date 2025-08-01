#!/bin/bash
# Setup script for Claude Code Logging System

echo "🚀 Setting up Claude Code Logging System..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "⚠️  Warning: Not in a git repository. Consider initializing with 'git init'"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p .claude/hooks
mkdir -p .claude/scripts
mkdir -p .claude/logs/archive
mkdir -p .claude/logs/current
mkdir -p logs

# Make scripts executable
echo "🔧 Setting permissions..."
chmod +x .claude/hooks/*.py 2>/dev/null
chmod +x .claude/scripts/*.sh 2>/dev/null
chmod +x .claude/scripts/*.py 2>/dev/null

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "   Please install Python 3.11 or later."
    exit 1
fi

# Check for uv (for hook execution)
if ! command -v uv &> /dev/null; then
    echo "⚠️  uv is not installed. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo "   You may need to restart your terminal or run: source ~/.bashrc"
fi

# Create local settings from template if it doesn't exist
if [ ! -f ".claude/settings.local.json" ]; then
    echo "📝 Creating settings from template..."
    if [ -f ".claude/settings.template.json" ]; then
        cp .claude/settings.template.json .claude/settings.local.json
    else
        cat > .claude/settings.local.json << 'EOF'
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(python3:*)",
      "Bash(bash:*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(wc:*)",
      "Bash(find:*)",
      "Bash(grep:*)",
      "Bash(mkdir:*)",
      "Bash(chmod:*)"
    ],
    "deny": []
  },
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/user_prompt_submit.py"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/stop_hook.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/post_tool_use.py"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/pre_compact.py"
          }
        ]
      }
    ]
  }
}
EOF
    fi
fi

# Add .claude/settings.local.json to .gitignore if not already there
if [ -f .gitignore ]; then
    if ! grep -q ".claude/settings.local.json" .gitignore; then
        echo ".claude/settings.local.json" >> .gitignore
    fi
fi

# Create aliases file for easy access
echo "📝 Creating aliases file..."
cat > .claude/logging_aliases.sh << 'EOF'
# Claude Code Logging System Aliases
# Source this file in your shell: source .claude/logging_aliases.sh

# Archive commands
alias claude-archive='bash .claude/scripts/claude_archive_system.sh archive'
alias claude-status='bash .claude/scripts/claude_archive_system.sh status'
alias claude-list='bash .claude/scripts/claude_archive_system.sh list'
alias claude-cleanup='bash .claude/scripts/claude_archive_system.sh cleanup'

# Direct data access
alias claude-tokens='python3 .claude/scripts/claude_jsonl_logger.py --summary'
alias claude-json='python3 .claude/scripts/claude_jsonl_logger.py --json'

# Summary generation
alias claude-summary='uv run .claude/scripts/conversation_summary_generator.py'
alias claude-create-summary='uv run .claude/scripts/conversation_summary_generator.py --trigger manual'

# Quick functions
claude-current() {
    echo "📋 Current Session:"
    python3 .claude/scripts/claude_jsonl_logger.py --summary
}

claude-export() {
    local filename="${1:-conversation_export.md}"
    echo "💾 Exporting conversation to: $filename"
    python3 .claude/scripts/claude_jsonl_logger.py -o "$filename"
    echo "✅ Export complete: $filename"
}

echo "✅ Claude Code Logging aliases loaded!"
echo "📖 Run 'claude-status' to see current session"
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "📚 Quick Start:"
echo "   1. Source the aliases: source .claude/logging_aliases.sh"
echo "   2. Start using Claude Code - logs will be created automatically"
echo "   3. Run 'claude-status' to see session info"
echo "   4. Run 'claude-tokens' to see token usage"
echo ""
echo "📁 Logs will be stored in:"
echo "   - ./logs/ (project-level logs)"
echo "   - ./.claude/logs/ (conversation archives)"
echo ""
echo "🔄 Note: Restart Claude Code for hooks to take effect"