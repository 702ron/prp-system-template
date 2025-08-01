# Claude Commands Guide

This guide provides comprehensive documentation for all slash commands available in the PRP System Template.

## 🚀 Quick Start Commands

### `/setup-prp-system`
Sets up the complete PRP system in your project.

**Options:**
- `--detect-tech` - Automatically detect and configure for your tech stack
- `--create-example` - Create an example PRP for demonstration

**Example:**
```
/setup-prp-system --detect-tech --create-example
```

### `/new-project`
Creates a new project from scratch with full PRP system integration.

**Options:**
- `--name <project-name>` - Project name
- `--type <project-type>` - Project type (web, api, mobile, desktop)
- `--tech <tech-stack>` - Technology stack
- `--template <template>` - Project template

**Example:**
```
/new-project --name my-app --type web --tech react-typescript --template modern
```

### `/analyze-project`
Analyzes existing projects and integrates PRP system.

**Options:**
- `--tech-stack` - Detect and document tech stack
- `--structure` - Analyze project structure
- `--dependencies` - Analyze dependencies
- `--create-prps` - Create initial PRPs based on analysis

**Example:**
```
/analyze-project --tech-stack --structure --create-prps
```

## 🔧 Development Commands

### `/review`
Comprehensive review command that analyzes code, builds, and changes with different scopes.

**Usage:**
```
/review [scope] [focus-area]
```

**Scopes:**
- `build` - Comprehensive build analysis and enhancement recommendations
- `code` - Code quality and structure review
- `changes` - Review git staged/unstaged changes
- `typescript` - TypeScript-specific review

**Options:**
- `focus-area` - Specific area to focus on (performance, security, features, etc.)

**Examples:**
```
/review build performance
/review code src/auth/
/review changes
/review typescript src/components/
```

### `/prp-create`
Create Product Requirement Prompts (PRPs) with language-specific templates and patterns.

**Usage:**
```
/prp-create [feature] [options]
```

**Options:**
- `--language <lang>` - Programming language (js, ts, python, go, rust, php, java)
- `--framework <framework>` - Framework (react, vue, angular, next, express, django, etc.)
- `--template <template>` - Template type (base, auth, api, ui, testing, deployment)
- `--output <path>` - Output path for PRP file
- `--ai-docs` - Include AI documentation patterns
- `--examples` - Include implementation examples
- `--testing` - Include testing requirements
- `--deployment` - Include deployment considerations

**Examples:**
```
/prp-create implement user authentication --language ts --framework react
/prp-create add API endpoints --language python --framework fastapi --ai-docs
/prp-create implement database models --template api
```

### `/git`
Comprehensive git operations command that handles commits, branches, conflicts, and repository management.

**Usage:**
```
/git [operation] [options]
```

**Operations:**
- `commit` - Commit staged changes with smart message generation
- `branch` - Create, switch, or manage branches
- `conflict` - Resolve merge conflicts with AI assistance
- `sync` - Sync with remote repository (pull/push)
- `status` - Show repository status and changes
- `history` - Show commit history and analysis
- `cleanup` - Clean up repository (stash, reset, etc.)

**Options:**
- `--message <msg>` - Custom commit message
- `--branch <name>` - Branch name for branch operations
- `--remote <name>` - Remote name (default: origin)
- `--force` - Force operations when needed
- `--interactive` - Interactive mode for complex operations
- `--dry-run` - Show what would be done without executing

**Examples:**
```
/git commit --message "Add user authentication feature"
/git branch create feature/user-auth
/git conflict resolve
/git sync pull
/git status
/git history --count 10
/git cleanup stash
```

## 📋 Project Management Commands

### `/create-pr`
Creates a pull request with comprehensive description and review checklist.

**Options:**
- `--title <title>` - PR title
- `--description <desc>` - PR description
- `--reviewers <list>` - List of reviewers
- `--labels <list>` - Labels to apply

**Example:**
```
/create-pr --title "Add user authentication" --reviewers "john,alice"
```

### `/new-dev-branch`
Creates a new development branch with proper naming conventions.

**Options:**
- `--type <type>` - Branch type (feature, bugfix, hotfix)
- `--name <name>` - Branch name
- `--base <branch>` - Base branch (default: main)

**Example:**
```
/new-dev-branch --type feature --name user-auth
```

## 🔍 Analysis and Debugging Commands

### `/debug-RCA`
Performs Root Cause Analysis (RCA) for issues and bugs.

**Options:**
- `--issue <description>` - Issue description
- `--logs <path>` - Path to log files
- `--context <context>` - Additional context

**Example:**
```
/debug-RCA --issue "User login fails" --logs logs/app.log
```

### `/onboarding`
Creates onboarding documentation and setup guides for new team members.

**Options:**
- `--role <role>` - Team member role
- `--tech-stack` - Include tech stack documentation
- `--processes` - Include development processes

**Example:**
```
/onboarding --role "Frontend Developer" --tech-stack --processes
```

### `/prime-core`
Primes the AI with core project context and patterns.

**Example:**
```
/prime-core
```

## 🎯 Command Categories

### Setup & Initialization
- `/setup-prp-system` - Complete system setup
- `/new-project` - New project creation
- `/analyze-project` - Existing project analysis
- `/onboarding` - Team member onboarding

### Development Workflow
- `/review` - Comprehensive code and build reviews
- `/prp-create` - Create feature requirements
- `/git` - Git operations and management
- `/new-dev-branch` - Development branch creation

### Project Management
- `/create-pr` - Pull request creation
- `/debug-RCA` - Issue analysis and debugging
- `/prime-core` - AI context priming

## 🔄 Command Consolidation

The following commands have been consolidated to reduce complexity and improve usability:

### Review Commands → `/review`
- `review-build` → `/review build`
- `review-code` → `/review code`
- `review-changes` → `/review changes`
- `review-typescript` → `/review typescript`

### PRP Commands → `/prp-create`
- `prp-base-create` → `/prp-create` (with language detection)
- `prp-typescript-create` → `/prp-create --language ts`

### Git Commands → `/git`
- `smart-commit` → `/git commit`
- Various git operations → `/git [operation]`

## 📚 Best Practices

### Command Usage
1. **Start with setup**: Use `/setup-prp-system` for new projects
2. **Regular reviews**: Use `/review` regularly for code quality
3. **Structured development**: Use `/prp-create` for all new features
4. **Git workflow**: Use `/git` for all repository operations

### Workflow Integration
1. **Feature Development**:
   ```
   /prp-create implement new feature
   /new-dev-branch --type feature --name new-feature
   # ... development work ...
   /review code src/
   /git commit
   /create-pr
   ```

2. **Code Review Process**:
   ```
   /review build
   /review code src/
   /review changes
   ```

3. **Issue Resolution**:
   ```
   /debug-RCA --issue "description"
   /git branch create bugfix/issue-name
   # ... fix implementation ...
   /review code
   /git commit
   ```

## 🛠️ Troubleshooting

### Common Issues
1. **Command not found**: Ensure `.claude` directory is properly set up
2. **Permission errors**: Check file permissions and git configuration
3. **Missing dependencies**: Run `/setup-prp-system` to install required tools

### Getting Help
- Use `/prime-core` to refresh AI context
- Check command documentation with `--help` flag
- Review generated reports and logs for detailed information

## 📈 Advanced Usage

### Custom Templates
Create custom templates by modifying the template files in the PRP system.

### Integration with CI/CD
Use commands in CI/CD pipelines for automated code review and quality checks.

### Team Collaboration
Share command outputs and reports with team members for better collaboration.

---

*This guide is part of the PRP System Template - an AI-assisted development framework.* 