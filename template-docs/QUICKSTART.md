# 🚀 Quick Start Guide

**Get up and running with the PRP System Template in under 5 minutes!**

## ⚡ Super Quick Start (2 minutes)

```bash
# 1. Use as GitHub template or clone
git clone https://github.com/your-repo/prp-system-template.git my-project
cd my-project

# 2. One command setup (installs everything)
bash .claude/scripts/one_time_setup.sh

# 3. You're ready! Test it works:
/token-test status
claude-status
```

## 📋 What Just Happened?

The one-time setup script just installed:

✅ **Token Optimization**: 30-50% cost savings  
✅ **Comprehensive Logging**: Full conversation tracking  
✅ **13 AI Agents**: Specialized development experts  
✅ **28+ Commands**: Complete development toolkit  
✅ **PRP System**: Structured feature development  

## 🎯 First Steps

### 1. Create Your First Feature

```bash
# Auto-detects your tech stack and creates comprehensive requirements
/prp-create "user authentication system"

# Or be specific about the language
/prp-create "user auth with JWT" --language typescript
```

### 2. Execute the Feature

```bash
# Interactive execution with validation loops
uv run PRPs/scripts/prp_runner.py --prp user-auth --interactive

# Or headless for CI/CD
uv run PRPs/scripts/prp_runner.py --prp user-auth --output-format json
```

### 3. Monitor Your Usage

```bash
# Check token usage and savings
claude-tokens

# View current session
claude-status

# Test optimization effectiveness
/token-test test
```

## 🔧 Adapt to Your Project

### For Existing Projects

```bash
# Copy template files to existing project
cp -r prp-system-template/.claude ./
cp -r prp-system-template/PRPs ./

# Run setup
bash .claude/scripts/one_time_setup.sh

# Analyze your project
/analyze-project --tech-stack --structure --create-prps
```

### Just Want the Commands?

```bash
# Minimal setup - just copy Claude commands
cp -r prp-system-template/.claude ./

# Commands work immediately with basic functionality
/review code src/
/git commit
/debug-RCA --issue "login fails"
```

## 🎨 Customize for Your Stack

### Detect Your Tech Stack

```bash
# Automatically detect and configure
/setup-prp-system --detect-tech --create-example

# This creates AI docs and patterns for your specific frameworks
```

### Manual Customization

```bash
# Add framework-specific patterns
edit PRPs/ai_docs/react-patterns.md
edit PRPs/ai_docs/supabase-patterns.md

# Customize PRP templates
edit PRPs/templates/prp_base_typescript.md
```

## 🚦 Verification Checklist

Verify everything is working:

```bash
# ✅ Commands available
/token-test status        # Should show optimization status
/review --help           # Should show command help

# ✅ Logging active  
claude-status            # Should show current session info
ls logs/                 # Should have log files

# ✅ PRP system ready
ls PRPs/templates/       # Should show available templates
ls PRPs/examples/        # Should show example PRPs

# ✅ Agents installed
# Just use Claude - agents are automatically selected
```

## 🔥 Power User Tips

### Development Workflow

```bash
# Create feature branch
/new-dev-branch --type feature --name auth-system

# Create and execute PRP
/prp-create "JWT authentication with refresh tokens" --language ts
uv run PRPs/scripts/prp_runner.py --prp auth-system --interactive

# Review and improve
/review code src/auth/ typescript performance
/refactor-component AuthProvider --extract-hooks

# Create PR
/create-pr --title "Add JWT authentication system"
```

### Token Optimization

```bash
# Measure baseline (optimizations off)
/token-test off
# ... do some development work ...

# Enable optimizations and compare  
/token-test on
# ... do the same work ...

# See the savings!
/token-test status
```

### Logging and Analytics

```bash
# Archive completed sessions
claude-archive "Implemented auth system"

# Export conversations
claude-export auth-implementation.md

# Monitor daily usage
tail -f logs/token_summary.txt
```

## 🆘 Troubleshooting

### Commands Not Working
```bash
# Ensure .claude directory exists in project root
ls -la .claude/

# Re-run setup if needed
bash .claude/scripts/one_time_setup.sh
```

### Logging Not Active
```bash
# Check status
claude-status

# Verify hooks are installed
ls .claude/hooks/
```

### PRP System Issues
```bash
# Install Python dependencies
pip install uv

# Test PRP validation
uv run PRPs/scripts/prp_runner.py --help
```

## 📚 What's Next?

### Learn the System
- **[README.md](README.md)** - Complete feature overview
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions  
- **[CLAUDE.md](CLAUDE.md)** - AI development guidelines

### Explore Examples
- **[PRPs/examples/](PRPs/examples/)** - Example feature requirements
- **[logs/](logs/)** - Sample usage analytics
- **[docs/](docs/)** - Comprehensive documentation

### Start Building
1. **Create your first PRP**: `/prp-create "your feature idea"`
2. **Execute with validation**: `uv run PRPs/scripts/prp_runner.py --prp your-feature --interactive`
3. **Monitor and optimize**: `claude-status` and `/token-test`
4. **Iterate and improve**: Customize templates and patterns

---

**🎉 You're all set!** The template is now configured for your project. Start building faster with AI-assisted development!

**Need help?** Check the troubleshooting section above or review the full documentation.