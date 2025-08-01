#!/bin/bash

# One-Time Token Optimization Setup
# Run this once to permanently enable token optimization

echo "🚀 Setting up permanent token optimization..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 1. Copy settings template to active settings
echo "📋 Setting up Claude Code settings..."
if [ ! -f "$PROJECT_ROOT/settings.local.json" ]; then
    cp "$PROJECT_ROOT/settings.template.json" "$PROJECT_ROOT/settings.local.json"
    echo "✅ Created settings.local.json"
else
    echo "⚠️  settings.local.json already exists, skipping copy"
fi

# 2. Add environment variables to shell profile
echo "🔧 Adding environment variables to shell profile..."
ENV_FILE="$PROJECT_ROOT/token_optimize.env"
SHELL_PROFILE=""

# Detect shell and profile file
if [ -n "$ZSH_VERSION" ]; then
    SHELL_PROFILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_PROFILE="$HOME/.bashrc"
else
    # Try to detect from SHELL variable
    case "$SHELL" in
        */zsh) SHELL_PROFILE="$HOME/.zshrc" ;;
        */bash) SHELL_PROFILE="$HOME/.bashrc" ;;
        *) SHELL_PROFILE="$HOME/.profile" ;;
    esac
fi

# Add source line to profile if not already present
SOURCE_LINE="source \"$ENV_FILE\""
if [ -f "$SHELL_PROFILE" ]; then
    if ! grep -q "$ENV_FILE" "$SHELL_PROFILE"; then
        echo "" >> "$SHELL_PROFILE"
        echo "# Claude Code Token Optimization" >> "$SHELL_PROFILE"
        echo "$SOURCE_LINE" >> "$SHELL_PROFILE"
        echo "✅ Added environment variables to $SHELL_PROFILE"
    else
        echo "⚠️  Environment variables already in $SHELL_PROFILE"
    fi
else
    echo "⚠️  Could not detect shell profile, manually add:"
    echo "   echo '$SOURCE_LINE' >> ~/.zshrc  # or ~/.bashrc"
fi

# 3. Source the environment variables for current session
echo "📥 Loading environment variables for current session..."
source "$ENV_FILE"
echo "✅ Environment variables loaded"

# 4. Create cache directory
CACHE_DIR="$PROJECT_ROOT/cache"
mkdir -p "$CACHE_DIR"
echo "✅ Created cache directory"

# 5. Set executable permissions on hooks
echo "🔧 Setting executable permissions on hooks..."
chmod +x "$PROJECT_ROOT/hooks"/*.py
echo "✅ Hook permissions set"

# 6. Test the setup
echo "🧪 Testing token optimization setup..."

# Test environment variables
if [ "$CLAUDE_CODE_ENABLE_TELEMETRY" = "1" ]; then
    echo "✅ Telemetry enabled"
else
    echo "❌ Telemetry not enabled"
fi

if [ "$DISABLE_NON_ESSENTIAL_MODEL_CALLS" = "1" ]; then
    echo "✅ Non-essential calls disabled"
else
    echo "❌ Non-essential calls not disabled"
fi

# Test hooks exist
if [ -f "$PROJECT_ROOT/hooks/pre_tool_use_cache.py" ]; then
    echo "✅ Caching hook installed"
else
    echo "❌ Caching hook missing"
fi

if [ -f "$PROJECT_ROOT/hooks/user_prompt_submit.py" ]; then
    echo "✅ Prompt optimization hook installed"
else
    echo "❌ Prompt optimization hook missing"
fi

echo ""
echo "🎉 Token optimization setup complete!"
echo ""
echo "📋 What's now permanently enabled:"
echo "  ✅ Smart file/command/search caching"
echo "  ✅ Automatic prompt compression and optimization"
echo "  ✅ Token usage monitoring and logging"
echo "  ✅ Environment variables for reduced token usage"
echo "  ✅ OpenTelemetry telemetry tracking"
echo ""
echo "💡 The optimizations will work automatically in all future Claude Code sessions"
echo ""
echo "📊 To check token usage anytime:"
echo "   ../logs/monitoring/token_summary.sh"
echo ""
echo "🔄 Restart your terminal or run 'source $SHELL_PROFILE' to reload environment"