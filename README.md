# PRP System Template 🚀

**A complete template for AI-assisted development** - Start any new project with the power of Product Requirement Prompts (PRPs), specialized AI agents, token optimization, and comprehensive logging.

> **Perfect for**: New projects, existing project enhancement, team onboarding, and systematic AI-driven development workflows.

## 🚀 Quick Start

### Option 1: Use as Template for New Project

```bash
# 1. Use as GitHub template or clone
git clone https://github.com/your-repo/prp-system-template.git my-new-project
cd my-new-project

# 2. Run one-time setup (enables everything)
bash .claude/scripts/one_time_setup.sh

# 3. Initialize for your project
/setup-prp-system --detect-tech --create-example

# 4. Start developing!
/prp-create "implement user authentication" --language ts
```

### Option 2: Add to Existing Project

```bash
# 1. Copy the template files
cp -r prp-system-template/.claude ./
cp -r prp-system-template/PRPs ./

# 2. Run setup
bash .claude/scripts/one_time_setup.sh

# 3. Analyze and enhance existing project
/analyze-project --tech-stack --structure --create-prps
```

### Option 3: Just the Commands (Minimal Setup)

```bash
# Copy just the Claude commands
cp -r prp-system-template/.claude ./
# Commands work immediately with basic functionality
```

## 🎯 What's Included

### 📊 Token Optimization System

**Save 30-50% on token usage** with intelligent caching and prompt optimization:

```bash
# Toggle optimizations for A/B testing
/token-test on    # Enable optimizations
/token-test off   # Disable for baseline testing
/token-test test  # Run guided comparison
```

**Features:**
- Smart file caching (50-80% reduction in redundant reads)
- Prompt compression (5-15% length reduction)
- Simple query routing to Haiku model (60-70% cost savings)
- Command result caching (40-60% reduction in repeated operations)

### 📊 Comprehensive Logging System

**Track everything** with automatic conversation logging:

```bash
claude-status     # Current session info
claude-tokens     # Token usage breakdown
claude-archive    # Save conversation
claude-export     # Export to file
```

**Captures:**
- All prompts and responses with timestamps
- Token usage (input, output, cache) and costs
- Tool usage patterns and parameters
- Complete conversation transcripts
- Daily usage summaries

### 🤖 Specialized AI Agents System

**13 expert agents** ready to handle specific development tasks:

```bash
# One-time setup installs all agents
bash .claude/scripts/one_time_setup.sh

# Claude automatically chooses the right agent
# Or specify: "Use the frontend-developer agent to..."
```

**Available Agents:**
- `api-designer` - REST/GraphQL API design
- `backend-developer` - Server-side implementation
- `code-quality-analyzer` - Code review & fixes
- `database-specialist` - Schema design & optimization
- `debugger` - Root cause analysis
- `devops-engineer` - CI/CD & infrastructure
- `documentation-specialist` - Technical documentation
- `frontend-developer` - React/Vue/Angular development
- `performance-optimizer` - Performance analysis
- `security-auditor` - Vulnerability assessment
- `system-architect` - System design
- `test-strategist` - Testing strategies
- `ui-ux-designer` - Interface design

### 📋 Product Requirement Prompts (PRPs)

**Structured approach** to feature development with validation loops:

```bash
# Create comprehensive feature requirements
/prp-create "user authentication system" --language typescript

# Execute with built-in validation
uv run PRPs/scripts/prp_runner.py --prp user-auth --interactive
```

**PRP Structure:**
- **Goal**: Specific end state and success criteria
- **Context**: All necessary documentation and examples
- **Implementation**: Detailed blueprint with task breakdown
- **Validation**: Executable tests and quality checks

**Templates Available:**
- `prp_base.md` - General features
- `prp_base_typescript.md` - TypeScript/React projects
- `prp_planning.md` - Architecture planning
- `prp_spec.md` - Detailed specifications
- `prp_task.md` - Simple tasks

## 📋 28+ Claude Commands

### 🎯 Project Setup
- `/setup-prp-system` - Complete system setup with tech detection
- `/new-project` - Create projects from scratch
- `/analyze-project` - Enhance existing projects

### 🚀 Development Workflow
- `/prp-create` - Create feature requirements (auto-detects language)
- `/review` - Code, build, and change reviews
- `/git` - Smart git operations with AI assistance

### 🛠️ Code Quality
- `/debug-RCA` - Root cause analysis
- `/refactor-component` - Intelligent refactoring
- `/test-strategy` - Testing approach design

### 📋 Project Management
- `/create-pr` - Pull requests with smart descriptions
- `/new-dev-branch` - Development branches with conventions
- `/onboarding` - Team member documentation

### 🔧 Utilities
- `/token-test` - Token optimization testing
- `/prime-core` - Refresh AI context
- `/rapid-parallel` - Parallel development workflows

## 🏗️ Template Architecture

### Directory Structure
```
prp-system-template/
├── .claude/                    # Claude Code configuration
│   ├── commands/              # 28+ slash commands
│   ├── hooks/                 # Logging & optimization hooks
│   ├── logs/                  # Session logs (current & archive)
│   ├── scripts/               # Setup & utility scripts
│   └── settings.template.json # Configuration template
├── PRPs/                      # Product Requirement Prompts
│   ├── templates/            # PRP templates for different uses
│   ├── examples/             # Example PRPs to learn from
│   ├── ai_docs/             # Framework-specific documentation
│   └── scripts/             # PRP execution utilities
├── scripts/                   # Project setup scripts
├── logs/                      # Usage logs and monitoring
└── docs/                      # Comprehensive documentation
```

### Key Design Principles

1. **Template-First**: Everything is designed to be copied and customized
2. **One-Pass Success**: PRPs enable AI to implement working code immediately
3. **Validation Loops**: Every feature includes executable quality checks
4. **Context-Rich**: Comprehensive documentation and examples included
5. **Token Efficient**: Built-in optimizations reduce costs by 30-50%

## 🛠️ Setup Instructions

### Prerequisites
- [Claude Code](https://claude.ai/code) installed
- Git configured
- Python 3.8+ (for PRP system)
- Node.js (if using JavaScript/TypeScript projects)

### Method 1: Use as GitHub Template (Recommended)

1. **Click "Use this template" on GitHub**
2. **Clone your new repository**
3. **Run one-time setup:**
   ```bash
   cd your-new-project
   bash .claude/scripts/one_time_setup.sh
   ```
4. **Initialize for your tech stack:**
   ```bash
   /setup-prp-system --detect-tech --create-example
   ```

### Method 2: Manual Setup

```bash
# Download and extract
wget https://github.com/your-repo/prp-system-template/archive/refs/heads/main.zip
unzip main.zip
cd prp-system-template-main

# Run setup
bash .claude/scripts/one_time_setup.sh

# Configure for your project
/setup-prp-system --detect-tech --create-example
```

### Verification

```bash
# Check that commands work
/token-test status

# Verify logging
claude-status

# Test PRP system
ls PRPs/examples/
```

## 🎯 Usage Examples

### Feature Development Workflow

```bash
# 1. Create comprehensive feature requirements
/prp-create "implement user authentication with JWT" --language typescript

# 2. Create development branch
/new-dev-branch --type feature --name user-auth

# 3. Execute PRP with validation
uv run PRPs/scripts/prp_runner.py --prp user-auth --interactive

# 4. Review implementation
/review code src/auth/

# 5. Create pull request
/create-pr --title "Add JWT authentication" --reviewers "team"
```

### Code Quality Workflow

```bash
# Comprehensive code review
/review build performance typescript

# Debug production issues
/debug-RCA --issue "Login timeout errors"

# Refactor components
/refactor-component UserProfile --extract-hooks --optimize
```

### Token Optimization Workflow

```bash
# Measure baseline usage
/token-test off
# ... perform typical development tasks ...

# Enable optimizations and compare
/token-test on
# ... perform same tasks ...

# View savings report
/token-test status
```

## 🎯 Key Features

### 🚀 AI-First Development
- **One-Pass Implementation**: PRPs enable AI to build working features immediately
- **Context-Rich Prompts**: Comprehensive documentation and examples included
- **Validation Loops**: Executable quality checks built into every feature
- **Smart Agent Selection**: Specialized AI agents for different development tasks

### 💰 Cost Optimization
- **30-50% Token Savings**: Intelligent caching and prompt optimization
- **Smart Model Routing**: Simple queries use cost-effective Haiku model
- **Usage Tracking**: Detailed analytics on token consumption and costs
- **A/B Testing**: Built-in tools to measure optimization effectiveness

### 📊 Complete Observability
- **Conversation Logging**: Full transcripts with metadata and timestamps
- **Token Analytics**: Detailed usage breakdowns and cost estimation
- **Tool Monitoring**: Track which development tools are used most
- **Project Insights**: Daily summaries and usage patterns

### 🔧 Developer Experience
- **28+ Commands**: Comprehensive slash command library
- **Template System**: Copy-paste ready for any new project
- **Framework Support**: JavaScript, TypeScript, Python, Go, Rust, and more
- **Team Ready**: Onboarding documentation, conventions, and guidelines

## 📖 Documentation

### Essential Guides
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions
- **[TOKEN_OPTIMIZATION_SETUP.md](.claude/TOKEN_OPTIMIZATION_SETUP.md)** - Token saving configuration
- **[CLAUDE.md](CLAUDE.md)** - Project-specific AI guidelines
- **[PRPs/README.md](PRPs/README.md)** - PRP system guide

### Quick References
- **[CLAUDE_COMMANDS_GUIDE.md](CLAUDE_COMMANDS_GUIDE.md)** - All available commands
- **[PROJECT_TEMPLATE_GUIDE.md](docs/PROJECT_TEMPLATE_GUIDE.md)** - Template usage patterns
- **[SLASH_COMMANDS_QUICK_REFERENCE.md](docs/SLASH_COMMANDS_QUICK_REFERENCE.md)** - Command cheat sheet

### Examples and Patterns
- **[PRPs/examples/](PRPs/examples/)** - Example feature requirements
- **[PRPs/ai_docs/](PRPs/ai_docs/)** - Framework-specific documentation
- **[logs/](logs/)** - Sample usage analytics

## 🚀 Ready to Start?

### For New Projects
```bash
# Use as GitHub template, then:
bash .claude/scripts/one_time_setup.sh
/setup-prp-system --detect-tech --create-example
```

### For Existing Projects
```bash
# Copy template files, then:
cp -r prp-system-template/.claude ./
bash .claude/scripts/one_time_setup.sh
/analyze-project --tech-stack --structure
```

### Just Want the Commands?
```bash
# Minimal setup:
cp -r prp-system-template/.claude ./
# Commands work immediately!
```

## 🔧 Troubleshooting

### Common Issues
- **Commands not found**: Ensure `.claude/` directory is in project root
- **Optimizations not working**: Run `bash .claude/scripts/one_time_setup.sh`
- **Logging not active**: Check `claude-status` and verify hooks installation
- **PRP validation failing**: Ensure Python dependencies: `pip install uv`

### Getting Help
- Use `/prime-core` to refresh AI context with project information
- Check command documentation: `/help` or `[command] --help`
- Review logs: `claude-status` and `claude-tokens`
- Validate setup: `/token-test status`

## 🤝 Customization

**This template is designed to be completely customizable:**

### Adding Custom Commands
```bash
# Add new slash commands
cp .claude/commands/template.md .claude/commands/my-command.md
# Edit and customize for your needs
```

### Modifying PRP Templates
```bash
# Customize for your tech stack
edit PRPs/templates/prp_base.md
# Add framework-specific patterns
edit PRPs/ai_docs/your-framework.md
```

### Extending AI Documentation
```bash
# Add project-specific patterns
echo "## Your Pattern" >> PRPs/ai_docs/custom-patterns.md
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🎯 Next Steps

1. **🚀 Get Started**: Use as template or copy `.claude/` directory
2. **⚡ Setup**: Run `bash .claude/scripts/one_time_setup.sh`
3. **🎯 First Feature**: `/prp-create "your first feature"`
4. **📊 Monitor**: Track usage with `claude-status` and `/token-test`
5. **🔄 Iterate**: Customize templates and patterns for your workflow

**Ready to build faster with AI?** Start your next project with this template! 🚀
