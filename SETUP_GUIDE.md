# PRP System Setup Guide

## 🚀 Quick Start - Complete Setup

```bash
# 1. Clone the template
git clone <repository-url>
cd prp-system-template

# 2. Set up logging (NEW!)
chmod +x setup-logging.sh
./setup-logging.sh

# 3. Source the aliases
source .claude/logging_aliases.sh

# 4. Set up PRP system (if needed)
/setup-prp-system --detect-tech --create-example
```

## ✅ What Gets Set Up

Your complete PRP system with logging includes:

### 📁 Directory Structure

```
.claude/                     # Claude Code configuration
├── commands/                # Slash commands
├── hooks/                   # Logging hooks (NEW!)
│   ├── user_prompt_submit.py
│   ├── stop_hook.py
│   └── post_tool_use.py
├── scripts/                 # Logging scripts (NEW!)
│   ├── claude_archive_system.sh
│   └── claude_jsonl_logger.py
├── logs/                    # Conversation archives
│   ├── current/
│   └── archive/
└── settings.template.json   # Template settings

PRPs/
├── templates/
│   └── prp_base.md          # Base template for all PRPs
├── ai_docs/                 # AI documentation framework
│   ├── README.md            # AI docs guide
│   ├── react-typescript-conventions.md
│   └── supabase-patterns.md
├── examples/                # Example PRPs
├── run_prp.py              # Python runner script
└── README.md               # PRP system guide

logs/                        # Project-level logs (NEW!)
├── user_prompts_*.json      # Daily prompt logs
├── tool_usage_*.json        # Tool usage tracking
└── token_summary.txt        # Token usage summary
```

## 📊 NEW: Logging System

The template now includes automatic logging that tracks all your Claude interactions:

### Features

- **Automatic prompt logging**: Every prompt is saved with timestamp
- **Token tracking**: Real-time token usage from Claude's native logs
- **Cost estimation**: Automatic cost calculations
- **Conversation archives**: Full transcripts with metadata
- **Tool usage tracking**: Monitor which tools are used most

### Using the Logging System

```bash
# Check current session
claude-status

# View token usage
claude-tokens

# Archive current session
claude-archive

# Export conversation
claude-export my-conversation.md

# List all archives
claude-list
```

### Log Locations

- **Project logs**: `./logs/` - Daily logs of prompts and tool usage
- **Conversation archives**: `./.claude/logs/` - Full conversation transcripts
- **Current session**: `./.claude/logs/current/` - Live session data

### 🚀 How to Use the PRP System

#### 1. Create a New PRP

```bash
# Copy the base template
cp PRPs/templates/prp_base.md PRPs/my-feature.md

# Edit the PRP with your requirements
nano PRPs/my-feature.md
```

#### 2. Run Your PRP with AI

```bash
# Execute the PRP
python PRPs/run_prp.py PRPs/my-feature.md

# Or validate the structure only
python PRPs/run_prp.py PRPs/my-feature.md --validate-only
```

#### 3. Example PRP Created

I've created an example PRP for you: `PRPs/example-user-auth.md`

- Shows how to structure a complete feature requirement
- Demonstrates proper use of ai_docs references
- Includes comprehensive requirements and implementation steps

### 📚 Key Components

#### PRP Templates (`PRPs/templates/`)

- **prp_base.md**: Base template with all required sections
- Copy this for each new feature you want to develop

#### AI Documentation (`PRPs/ai_docs/`)

- Contains patterns and conventions for your tech stack
- Referenced in PRPs to provide AI with project context
- Automatically detected and suggested by the tech stack script

#### Python Runner (`PRPs/run_prp.py`)

- Validates PRP structure
- Executes PRPs with AI assistance
- Provides helpful feedback and guidance

### 🎯 Best Practices

1. **Be Specific**: Include exact patterns and function names
2. **Reference ai_docs**: Always include relevant documentation
3. **Iterate**: Refine PRPs based on AI output quality
4. **Document**: Keep PRPs updated as requirements change

### 🔧 Customization

#### Adding New Technologies

1. Run: `python scripts/detect-tech-stack.py`
2. Create corresponding ai_docs files
3. Update documentation with new patterns

#### Modifying Patterns

1. Edit ai_docs files with your project's specific patterns
2. Update PRP templates if needed
3. Test with sample PRPs

### 📖 Next Steps

1. **Review the example PRP**: `PRPs/example-user-auth.md`
2. **Create your first PRP**: Copy the template and start developing
3. **Customize ai_docs**: Add your project's specific patterns
4. **Integrate with your workflow**: Use PRPs for all new features

### 🆘 Getting Help

- **PRP System Guide**: `PRPs/README.md`
- **AI Documentation Guide**: `PRPs/ai_docs/README.md`
- **Main Documentation**: `README.md`

---

**You're all set!** Start creating PRPs and experience the power of structured, pattern-driven AI-assisted development! 🚀
