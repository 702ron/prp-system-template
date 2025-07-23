# PRP System Template

A comprehensive PRP (Product Requirement Prompt) system template for AI-assisted development. This template provides everything you need to set up AI-assisted development with consistent, production-ready code generation across all your projects.

## 🚀 Quick Start (5 Minutes)

### 0. Setup Slash Commands (Required for Claude Code)
Before using any slash commands, you need to set up the `.claude` directory in your project:

```bash
# Option 1: Clone this template repository
git clone https://github.com/702ron/prp-system-template.git my-new-project
cd my-new-project

# Option 2: Copy the .claude directory to your existing project
cp -r prp-system-template/.claude /path/to/your/project/

# Option 3: Download just the .claude directory
curl -L https://github.com/702ron/prp-system-template/archive/main.tar.gz | tar -xz --strip-components=1 prp-system-template-main/.claude
```

**Note**: The `.claude` directory contains all the slash commands. Without it, the commands won't be available in Claude Code.

### 1. Choose Your Starting Point

#### For New Projects
Start from scratch with comprehensive setup:
```bash
# In Claude Code
/new-project "A web application for task management with user authentication"
```

#### For Existing Projects
Enhance your existing codebase:
```bash
# In Claude Code
/analyze-project "I want to add user authentication and improve the UI"
```

#### For PRP System Only
Add PRP system to any project:
```bash
# Option 1: Run the automated setup script
./scripts/setup-prp-system.sh

# Option 2: Use Claude slash command (in Claude Code)
/setup-prp-system
/setup-prp-system --tech-stack  # With tech stack detection
/setup-prp-system --full        # Complete setup with examples
```

### 2. Detect Your Tech Stack (Optional)
```bash
# Automatically detect your project's technology stack and create appropriate ai_docs
python scripts/detect-tech-stack.py
```

### 3. Create Your First PRP
```bash
# Create a new PRP for your feature
cp PRPs/templates/prp_base.md PRPs/my-feature.md

# Edit the PRP with your requirements
# Then run with AI
python PRPs/run_prp.py PRPs/my-feature.md
```

### 4. Use Claude Slash Commands (Optional)
```bash
# In Claude Code, type "/" to see available commands
/prp-base-create implement user authentication
/prp-base-execute PRPs/my-feature.md
/review-general src/
```

## 🎯 Three Ways to Use This Template

### 1. **New Project** (Recommended for new development)
```bash
# Clone the template and start fresh
git clone https://github.com/702ron/prp-system-template.git my-new-project
cd my-new-project

# Use the new project command
/new-project "A React application for e-commerce with payment processing"
```

### 2. **Existing Project** (Add PRP system to current project)
```bash
# Copy just the .claude directory to your existing project
cp -r prp-system-template/.claude /path/to/your/project/

# Use the analyze project command
/analyze-project "I want to add real-time notifications and improve performance"
```

### 3. **PRP System Only** (Minimal setup)
```bash
# Copy the .claude directory and run setup
cp -r prp-system-template/.claude /path/to/your/project/
/setup-prp-system --full
```

## 📋 What's Included

### Core PRP System
- **PRP Templates**: Structured prompts for AI-assisted development
- **Python Runner**: Script to execute PRPs with AI
- **Validation**: Built-in PRP structure validation
- **Examples**: Sample PRPs demonstrating best practices
- **Claude Commands**: 12+ slash commands for AI-assisted development

### AI Documentation Framework (ai_docs)
- **Technology Patterns**: Pre-built patterns for React, TypeScript, Supabase, etc.
- **Convention Guides**: Coding standards and best practices
- **Integration Patterns**: Database, API, and workflow patterns
- **Extensible**: Easy to add new patterns for your tech stack

### Automation Scripts
- **Setup Script**: One-command PRP system installation
- **Tech Stack Detection**: Automatic detection of project technologies
- **Template Validation**: Ensures proper setup and structure

### Comprehensive Documentation
- **Setup Guides**: Step-by-step installation instructions
- **Usage Examples**: Real-world PRP examples
- **Best Practices**: Guidelines for effective AI-assisted development
- **Troubleshooting**: Common issues and solutions

## 🏗️ Project Structure

```
prp-system-template/
├── .claude/                # Claude Code commands
│   └── commands/           # 12+ slash commands for AI development
├── PRPs/                   # PRP system core
│   ├── templates/          # PRP templates
│   │   ├── prp_base.md    # Base PRP template
│   │   ├── prp_base_typescript.md
│   │   ├── prp_planning.md
│   │   ├── prp_spec.md
│   │   └── prp_task.md
│   ├── ai_docs/           # AI documentation framework
│   │   ├── README.md      # AI docs guide
│   │   ├── react-typescript-conventions.md
│   │   ├── supabase-patterns.md
│   │   └── [20+ additional patterns]
│   ├── examples/          # Example PRPs
│   ├── scripts/           # PRP runner scripts
│   ├── run_prp.py        # Python runner script
│   └── README.md         # PRP system guide
├── scripts/               # Automation scripts
│   ├── setup-prp-system.sh # Setup automation
│   ├── detect-tech-stack.py # Tech stack detection
│   └── setup-guide.md    # Detailed setup guide
├── docs/                  # Documentation
├── CLAUDE.md             # Project guidelines
├── CLAUDE_COMMANDS_GUIDE.md # Slash commands guide
└── README.md             # This file
```

## 🎯 Features

### AI-Assisted Development
- **Structured Prompts**: Consistent PRP format for reliable AI output
- **Context-Aware**: ai_docs provide deep project context to AI
- **Pattern-Driven**: Follow established patterns for consistent code
- **Quality Assurance**: Built-in validation and best practices
- **Claude Integration**: 12+ slash commands for seamless AI development

### Technology Agnostic
- **Multi-Stack Support**: Works with React, Vue, Angular, Node.js, Python, etc.
- **Automatic Detection**: Detects your tech stack and suggests appropriate ai_docs
- **Extensible**: Easy to add support for new technologies

### Team Collaboration
- **Shared Patterns**: Consistent patterns across team members
- **Documentation**: Comprehensive guides for onboarding
- **Version Control**: Track pattern evolution with your codebase

## 🛠️ Supported Technologies

### Frontend
- React (with TypeScript)
- Vue.js
- Angular
- Next.js
- Tailwind CSS
- Material-UI
- Chakra UI

### Backend
- Node.js/Express
- Python/Django
- Python/FastAPI
- Go
- Rust

### Databases
- Supabase
- PostgreSQL
- MongoDB
- Prisma
- Redis

### Tools
- TypeScript
- Vite
- Webpack
- Jest
- Cypress
- Playwright

## 📖 Usage Examples

### Creating a New PRP
```bash
# Copy the base template
cp PRPs/templates/prp_base.md PRPs/user-authentication.md

# Edit with your requirements
nano PRPs/user-authentication.md

# Run with AI
python PRPs/run_prp.py PRPs/user-authentication.md
```

### Using ai_docs in PRPs
```markdown
## All Needed Context

### AI Documentation (Recommended)
- **file**: PRPs/ai_docs/react-typescript-conventions.md
  **why**: Component structure and TypeScript patterns
- **file**: PRPs/ai_docs/supabase-patterns.md
  **why**: Database operations and authentication patterns
```

### Tech Stack Detection
```bash
# Detect your project's tech stack
python scripts/detect-tech-stack.py

# Output example:
# 📋 Detected Technology Stack:
#   Frontend: React, Tailwind CSS, TypeScript
#   Database: Supabase
#   Tools: Vite
# 
# 📝 Suggested ai_docs to create:
#   - PRPs/ai_docs/react-typescript-conventions.md
#   - PRPs/ai_docs/tailwind-patterns.md
#   - PRPs/ai_docs/supabase-patterns.md
```

## 🔧 Customization

## 🛠️ Troubleshooting

### Slash Commands Not Appearing
If you don't see the slash commands in Claude Code:

1. **Check .claude directory exists**:
   ```bash
   ls -la .claude/commands/
   ```

2. **Verify command files are present**:
   ```bash
   ls .claude/commands/development/
   # Should show: analyze-project.md, new-project.md, setup-prp-system.md, etc.
   ```

3. **Restart Claude Code**: Sometimes Claude Code needs to be restarted to detect new commands

4. **Check file permissions**:
   ```bash
   chmod -R 644 .claude/commands/
   ```

### Common Issues

**"Command not found" errors**:
- Ensure you're in the correct project directory
- Verify the `.claude` directory is in your project root
- Check that command files have `.md` extensions

**Permission errors**:
- Make sure you have read permissions on the `.claude` directory
- Try copying the directory again if permissions are corrupted

**Commands not updating**:
- Clear Claude Code cache
- Restart the Claude Code application
- Verify you're using the latest version of the template

### Adding New Technologies
1. Update `scripts/detect-tech-stack.py` to detect your technology
2. Create corresponding ai_docs files
3. Update documentation with new patterns

### Modifying Patterns
1. Edit ai_docs files with your project's specific patterns
2. Update PRP templates if needed
3. Test with sample PRPs

### Creating Project Templates
1. Copy this template to your own repository
2. Customize ai_docs for your preferred tech stack
3. Enable GitHub template option
4. Share with your team

## 📚 Documentation

- **[PRP System Guide](PRPs/README.md)** - Main PRP system documentation
- **[AI Documentation Guide](PRPs/ai_docs/README.md)** - Using ai_docs effectively
- **[Claude Commands Guide](CLAUDE_COMMANDS_GUIDE.md)** - Complete slash commands reference
- **[Systematic Setup Guide](docs/SYSTEMATIC_SETUP_GUIDE.md)** - Complete setup process
- **[Project Template Guide](docs/PROJECT_TEMPLATE_GUIDE.md)** - Creating reusable templates
- **[Development Guidelines](CLAUDE.md)** - Best practices and conventions

## 🚀 Getting Started

### For New Projects
1. **Use this template**: Click "Use this template" on GitHub
2. **Set up PRP system**: Run `./scripts/setup-prp-system.sh`
3. **Detect tech stack**: Run `python scripts/detect-tech-stack.py`
4. **Create first PRP**: Copy template and start developing

### For Existing Projects
1. **Copy PRP system**: Copy `PRPs/` and `scripts/` directories
2. **Run setup**: Execute `./scripts/setup-prp-system.sh`
3. **Detect stack**: Run `python scripts/detect-tech-stack.py`
4. **Customize**: Edit ai_docs with your project's patterns

## 🤝 Contributing

1. Fork this template
2. Create a feature branch
3. Make your improvements
4. Test with sample projects
5. Submit a pull request

## 📈 Success Metrics

Track these metrics to measure PRP system effectiveness:

- **Code Quality**: Reduced bugs, improved consistency
- **Development Speed**: Faster feature delivery
- **Team Productivity**: Reduced onboarding time
- **Documentation Quality**: Better pattern coverage
- **AI Output Quality**: Higher success rate of generated code

## 🐛 Troubleshooting

### Common Issues

1. **AI generates inconsistent code**
   - Review ai_docs for completeness
   - Update patterns to match actual codebase
   - Be more specific in PRP requirements

2. **PRPs take too long to create**
   - Use templates and examples
   - Reuse patterns from existing ai_docs
   - Start with simple PRPs and iterate

3. **Setup script fails**
   - Check file permissions
   - Verify Python installation
   - Ensure proper directory structure

### Getting Help

- Review existing ai_docs for patterns
- Check PRP examples for similar features
- Update documentation with new patterns
- Share successful PRPs with the team

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the PRPs-agentic-eng repository
- Built for consistent AI-assisted development
- Designed for team collaboration and code quality

---

**Ready to supercharge your development with AI?** Start with this template and experience the power of structured, pattern-driven AI-assisted development! 🚀