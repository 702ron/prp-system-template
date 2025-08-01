# PRP System Template

An AI-assisted development framework that combines Product Requirement Prompts (PRPs) with comprehensive Claude slash commands for structured, efficient development workflows. Now includes automatic conversation logging and token usage tracking!

## 🚀 Quick Start

### For New Projects

```bash
# Clone or download this template
git clone <repository-url>
cd prp-system-template

# Set up logging system (NEW!)
chmod +x setup-logging.sh
./setup-logging.sh

# Set up AI agents (NEW!)
chmod +x setup-agents.sh
./setup-agents.sh

# Set up the complete PRP system
/setup-prp-system --detect-tech --create-example
```

### For Existing Projects

```bash
# Analyze and integrate with existing project
/analyze-project --tech-stack --structure --create-prps

# Add logging capabilities
./setup-logging.sh

# Install AI agents
./setup-agents.sh
```

## 📊 NEW: Automatic Logging System

This template now includes a comprehensive logging system that tracks:
- All user prompts to Claude
- Complete conversation transcripts
- Token usage (input, output, cache)
- Estimated costs
- Tool usage patterns

### Setting Up Logging

```bash
# Run the setup script
./setup-logging.sh

# Source the aliases (add to your shell profile)
source .claude/logging_aliases.sh

# Check current session
claude-status
```

### Logging Features

- **Automatic**: Logs are created automatically via Claude Code hooks
- **Project-level logs**: Stored in `./logs/` directory
- **Conversation archives**: Full transcripts in `./.claude/logs/`
- **Token tracking**: Real-time token usage from Claude's native logs
- **Cost estimation**: Automatic cost calculations
- **Daily logs**: Organized by date for easy review

### Available Commands

```bash
claude-archive    # Archive current session
claude-status     # Show current session info
claude-tokens     # View token usage
claude-export     # Export conversation to file
claude-list       # List archived sessions
```

## 🤖 NEW: AI Agents System

This template includes a comprehensive set of specialized AI agents for different development tasks:

### Setting Up Agents

```bash
# Install agents to your user directory
./setup-agents.sh

# List available agents
./setup-agents.sh list

# Check installation status
./setup-agents.sh status

# Force reinstall all agents
./setup-agents.sh install --force
```

### Available Agents

- **api-designer** - Design REST, GraphQL, and gRPC APIs with best practices
- **backend-developer** - Server-side implementation, APIs, authentication, middleware
- **code-quality-analyzer** - Comprehensive code review and automated fixes
- **database-specialist** - Schema design, query optimization, data modeling
- **debugger** - Root cause analysis and error investigation
- **devops-engineer** - CI/CD, containerization, infrastructure as code
- **documentation-specialist** - Technical documentation, README files, API docs
- **frontend-developer** - React, Vue, Angular, and modern UI development
- **performance-optimizer** - Application performance analysis and optimization
- **security-auditor** - Security vulnerability assessment and compliance
- **system-architect** - High-level system design and architecture decisions
- **test-strategist** - Testing strategies, unit tests, integration tests
- **ui-ux-designer** - User interface design, accessibility, user experience

### Agent Features

- **Specialized Knowledge**: Each agent has deep expertise in their domain
- **Context Aware**: Agents understand your project structure and conventions
- **Tool Integration**: Access to all Claude Code tools for implementation
- **Quality Focus**: Built-in best practices and validation patterns

### Enhanced Conversation Logs

The logging system now captures detailed information instead of just placeholders:

**Before:**
```
### Message 5 - ASSISTANT [2025-08-01 03:15:03]
[TOOL: TodoWrite]
---
### Message 6 - USER [2025-08-01 03:15:03]
[TOOL_RESULT]
```

**After:**
```
### Message 5 - ASSISTANT [2025-08-01 03:15:03]
*Tokens: 6 in + 175 out*

[TOOL USE: TodoWrite]
Tool ID: toolu_01GhRZA9S2eNP1woJLY6e4Z2
Parameters:
  - todos: [4 items]
---
### Message 6 - USER [2025-08-01 03:15:03]
*Tool Result Data: {
  "oldTodos": [...],
  "newTodos": [...]
}*

[TOOL RESULT]
Tool Use ID: toolu_01GhRZA9S2eNP1woJLY6e4Z2
Output:
Todos have been modified successfully...
```

This provides complete visibility into:
- Tool parameters and inputs
- Full tool outputs and results
- Tool execution IDs for tracing
- Error states and debugging info

## 📋 Available Commands

### 🎯 Core Commands

- **`/setup-prp-system`** - Complete system setup with tech stack detection
- **`/new-project`** - Create new projects from scratch
- **`/analyze-project`** - Analyze and enhance existing projects

### 🔧 Development Commands

- **`/review`** - Comprehensive code, build, and change reviews
- **`/prp-create`** - Create feature requirements with language-specific templates
- **`/git`** - Complete git operations with AI assistance

### 📋 Project Management

- **`/create-pr`** - Create pull requests with comprehensive descriptions
- **`/new-dev-branch`** - Create development branches with proper conventions
- **`/debug-RCA`** - Root cause analysis for issues and bugs
- **`/onboarding`** - Create onboarding documentation for team members

## 🔄 Command Consolidation

The system has been streamlined with consolidated commands for better usability:

### Review Commands → `/review`

- `review-build` → `/review build`
- `review-code` → `/review code`
- `review-changes` → `/review changes`
- `review-typescript` → `/review typescript`

### PRP Commands → `/prp-create`

- `prp-base-create` → `/prp-create` (with automatic language detection)
- `prp-typescript-create` → `/prp-create --language ts`

### Git Commands → `/git`

- `smart-commit` → `/git commit`
- Various git operations → `/git [operation]`

## 📁 Project Structure

```
prp-system-template/
├── .claude/                    # Claude commands and configuration
│   ├── commands/              # Slash command definitions
│   └── ai_docs/              # AI documentation patterns
├── PRPs/                      # Product Requirement Prompts
│   ├── templates/            # PRP templates
│   ├── examples/             # Example PRPs
│   └── ai_docs/             # AI documentation
├── scripts/                   # Setup and utility scripts
├── docs/                      # Documentation
└── README.md                 # This file
```

## 🛠️ Setup Instructions

### 1. Basic Setup

The `.claude` directory containing slash commands must be set up for full functionality:

**Option A: Clone the entire repo**

```bash
git clone <repository-url>
cd prp-system-template
```

**Option B: Copy the .claude directory**

```bash
# Copy the .claude directory to your project root
cp -r prp-system-template/.claude ./
```

### 2. Complete PRP System Setup

For the full PRP system (AI docs, templates, examples, etc.):

```bash
# Run the setup command
/setup-prp-system --detect-tech --create-example
```

### 3. Claude Development Guidelines

For optimal AI-assisted development, review the comprehensive guidelines:

```bash
# Read the Claude development guidelines
/read docs/CLAUDE.md
```

**Key Features:**

- **Slash Commands**: Complete reference of available commands for file operations, development tools, and AI assistance
- **Task Management**: Structured approach for handling long-running tasks with progress tracking
- **Progress Reporting**: Standardized format for documenting task completion and next steps
- **Best Practices**: Guidelines for effective use of AI tools and maintaining code quality

**Example Usage:**

```bash
# Create a new PRP following the guidelines
/read PRPs/examples/example-slash-commands-test.md

# Use slash commands for development tasks
/read package.json
/edit src/components/NewComponent.tsx
/run npm test
```

**Quick Reference:**

```bash
# Access the quick reference card
/read docs/SLASH_COMMANDS_QUICK_REFERENCE.md
```

### 3. Usage Scenarios

#### New Project Development

```bash
/new-project --name my-app --type web --tech react-typescript
```

#### Existing Project Enhancement

```bash
/analyze-project --tech-stack --structure --create-prps
```

#### Slash Commands Only

If you only need the slash commands without the full PRP system:

- Copy the `.claude` directory to your project
- Commands will work with basic functionality

## 📚 Usage Examples

### Feature Development Workflow

```bash
# 1. Create feature requirement
/prp-create implement user authentication --language ts --framework react

# 2. Create development branch
/new-dev-branch --type feature --name user-auth

# 3. Review implementation
/review code src/auth/

# 4. Commit changes
/git commit --message "Add user authentication"

# 5. Create pull request
/create-pr --title "Add user authentication" --reviewers "team"
```

### Code Review Process

```bash
# Comprehensive review
/review build performance
/review code src/
/review changes
```

### Issue Resolution

```bash
# Debug and fix issues
/debug-RCA --issue "User login fails"
/git branch create bugfix/login-issue
# ... implement fix ...
/review code
/git commit
```

## 🎯 Key Features

### AI-Assisted Development

- **Smart Code Generation**: Language-specific templates and patterns
- **Intelligent Reviews**: Comprehensive analysis with actionable recommendations
- **Context-Aware Commits**: AI-generated commit messages based on changes
- **Conflict Resolution**: AI-assisted merge conflict resolution

### Structured Workflows

- **PRP System**: Product Requirement Prompts for systematic feature development
- **Quality Gates**: Automated code review and quality checks
- **Documentation**: AI-generated documentation and onboarding guides
- **Team Collaboration**: Pull request creation and review workflows

### Technology Support

- **Multiple Languages**: JavaScript, TypeScript, Python, Go, Rust, PHP, Java
- **Framework Integration**: React, Vue, Angular, Next.js, Express, Django, FastAPI
- **Development Tools**: Git integration, CI/CD support, testing frameworks

## 📖 Documentation

- **[Claude Commands Guide](CLAUDE_COMMANDS_GUIDE.md)** - Complete command reference
- **[Project Template Guide](docs/PROJECT_TEMPLATE_GUIDE.md)** - Project setup and structure
- **[Systematic Setup Guide](docs/SYSTEMATIC_SETUP_GUIDE.md)** - Step-by-step setup instructions
- **[CLAUDE.md](docs/CLAUDE.md)** - AI development guidelines

## 🔧 Troubleshooting

### Common Issues

1. **Commands not found**: Ensure `.claude` directory is in your project root
2. **Missing functionality**: Run `/setup-prp-system` for complete PRP system
3. **Permission errors**: Check file permissions and git configuration

### Getting Help

- Use `/prime-core` to refresh AI context
- Check command documentation with `--help` flags
- Review generated reports for detailed information

## 🤝 Contributing

This template is designed to be easily customizable and extensible:

1. **Custom Commands**: Add new commands in `.claude/commands/`
2. **Templates**: Modify PRP templates in `PRPs/templates/`
3. **AI Documentation**: Update patterns in `PRPs/ai_docs/`
4. **Scripts**: Enhance setup scripts in `scripts/`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Ready to supercharge your development?** Start with `/setup-prp-system` to experience the full power of AI-assisted development! 🚀
