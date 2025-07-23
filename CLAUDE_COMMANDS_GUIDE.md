# Claude Slash Commands Guide

## Overview

This PRP system template now includes comprehensive Claude slash commands from the [PRPs-agentic-eng repository](https://github.com/Wirasm/PRPs-agentic-eng.git). These commands provide powerful AI-assisted development workflows that integrate seamlessly with Claude Code.

## Available Commands

### 🚀 PRP Creation & Execution

#### `/prp-base-create`
Creates comprehensive PRPs with research and context gathering.

**Usage:**
```
/prp-base-create implement user authentication with JWT tokens
```

**Features:**
- Generates complete PRP structure
- Includes research and context gathering
- Provides implementation blueprint
- Sets up validation loops

#### `/prp-base-execute`
Executes PRPs against your codebase with full context.

**Usage:**
```
/prp-base-execute PRPs/my-feature.md
```

**Features:**
- Runs PRPs with full project context
- Integrates with ai_docs
- Provides real-time feedback
- Generates production-ready code

#### `/prp-planning-create`
Creates planning documents with diagrams and architecture.

**Usage:**
```
/prp-planning-create design a microservices architecture
```

**Features:**
- Generates architectural diagrams
- Creates implementation plans
- Includes timeline estimates
- Provides resource requirements

#### `/prp-spec-create`
Creates detailed technical specifications.

**Usage:**
```
/prp-spec-create API specification for user management
```

**Features:**
- Generates API contracts
- Creates database schemas
- Defines interfaces
- Includes validation rules

#### `/prp-spec-execute`
Executes specifications to generate code.

**Usage:**
```
/prp-spec-execute PRPs/api-spec.md
```

**Features:**
- Converts specs to working code
- Generates tests
- Creates documentation
- Validates implementation

#### `/prp-task-create`
Creates detailed task breakdowns from PRPs.

**Usage:**
```
/prp-task-create PRPs/my-feature.md
```

**Features:**
- Breaks down PRPs into tasks
- Estimates effort
- Assigns priorities
- Creates dependencies

#### `/prp-task-execute`
Executes individual tasks from task lists.

**Usage:**
```
/prp-task-execute implement authentication middleware
```

**Features:**
- Focuses on specific tasks
- Provides targeted implementation
- Includes testing
- Validates completion

#### `/api-contract-define`
Defines API contracts and interfaces.

**Usage:**
```
/api-contract-define user management API
```

**Features:**
- Generates OpenAPI specs
- Creates TypeScript interfaces
- Defines request/response schemas
- Includes validation rules

### 🔍 Code Review & Quality

#### `/review-general`
Performs comprehensive code review.

**Usage:**
```
/review-general src/auth/
```

**Features:**
- Analyzes code quality
- Identifies potential issues
- Suggests improvements
- Checks best practices

#### `/review-staged-unstaged`
Reviews git changes for quality.

**Usage:**
```
/review-staged-unstaged
```

**Features:**
- Reviews staged changes
- Analyzes unstaged modifications
- Provides feedback
- Suggests improvements

#### `/refactor-simple`
Performs simple refactoring tasks.

**Usage:**
```
/refactor-simple improve error handling in auth module
```

**Features:**
- Identifies refactoring opportunities
- Suggests improvements
- Maintains functionality
- Improves code quality

### 🛠️ Development Workflow

#### `/prime-core`
Primes Claude with project context.

**Usage:**
```
/prime-core
```

**Features:**
- Loads project context
- Sets up development environment
- Configures AI assistance
- Prepares for development

#### `/onboarding`
Onboards new team members.

**Usage:**
```
/onboarding
```

**Features:**
- Explains project structure
- Sets up development environment
- Provides coding guidelines
- Introduces workflows

#### `/debug-RCA`
Performs root cause analysis for debugging.

**Usage:**
```
/debug-RCA investigate authentication failures
```

**Features:**
- Analyzes error patterns
- Identifies root causes
- Suggests solutions
- Provides debugging strategies

#### `/new-dev-branch`
Creates new development branches.

**Usage:**
```
/new-dev-branch feature/user-auth
```

**Features:**
- Creates feature branches
- Sets up tracking
- Configures development environment
- Prepares for development

#### `/setup-prp-system`
Automatically sets up the complete PRP system in your project.

**Usage:**
```
/setup-prp-system
/setup-prp-system --tech-stack
/setup-prp-system --full
```

**Features:**
- Creates directory structure
- Sets up PRP templates and runner scripts
- Creates AI documentation framework
- Optionally detects tech stack and creates ai_docs
- Optionally creates example PRPs

### 📝 Git & GitHub Operations

#### `/create-pr`
Creates pull requests with comprehensive descriptions.

**Usage:**
```
/create-pr implement user authentication
```

**Features:**
- Generates PR descriptions
- Includes testing information
- Provides review guidelines
- Sets up CI/CD integration

#### `/smart-commit`
Creates intelligent commit messages.

**Usage:**
```
/smart-commit
```

**Features:**
- Analyzes changes
- Generates descriptive messages
- Follows conventional commits
- Includes context

## How to Use Commands

### 1. In Claude Code
1. Type `/` to see available commands
2. Select a command from the list
3. Provide arguments when prompted
4. Follow the generated instructions

### 2. Command Structure
Most commands follow this pattern:
```
/command-name [arguments]
```

### 3. Integration with PRPs
Commands work seamlessly with your PRP system:
- Use `/prp-base-create` to generate PRPs
- Use `/prp-base-execute` to implement them
- Use `/review-general` to validate the code
- Use `/create-pr` to submit changes

## Command Categories

### 🎯 PRP Workflow
- **Creation**: `/prp-base-create`, `/prp-planning-create`, `/prp-spec-create`
- **Execution**: `/prp-base-execute`, `/prp-spec-execute`, `/prp-task-execute`
- **Management**: `/prp-task-create`, `/api-contract-define`

### 🔍 Quality Assurance
- **Review**: `/review-general`, `/review-staged-unstaged`
- **Refactoring**: `/refactor-simple`
- **Debugging**: `/debug-RCA`

### 🚀 Development
- **Setup**: `/prime-core`, `/onboarding`, `/setup-prp-system`
- **Workflow**: `/new-dev-branch`, `/smart-commit`
- **Collaboration**: `/create-pr`

## Best Practices

### 1. Start with Context
Always use `/prime-core` when starting a new session to load project context.

### 2. Setup PRP System
Use `/setup-prp-system` to quickly initialize the PRP system in new projects.

### 3. Use PRPs for Features
For new features, use the PRP workflow:
1. `/prp-base-create` to generate the PRP
2. `/prp-base-execute` to implement it
3. `/review-general` to validate the code

### 4. Regular Reviews
Use `/review-staged-unstaged` before committing to ensure code quality.

### 5. Smart Commits
Use `/smart-commit` to create meaningful commit messages.

## Integration with Your Workflow

### Development Cycle
1. **Plan**: Use `/prp-planning-create` for new features
2. **Specify**: Use `/prp-spec-create` for detailed requirements
3. **Implement**: Use `/prp-base-execute` for development
4. **Review**: Use `/review-general` for quality assurance
5. **Commit**: Use `/smart-commit` for version control
6. **Submit**: Use `/create-pr` for collaboration

### Team Collaboration
- Use `/onboarding` for new team members
- Use `/create-pr` for code reviews
- Use `/review-general` for quality gates
- Use `/debug-RCA` for problem solving

## Advanced Usage

### Custom Commands
You can create custom commands in `.claude/commands/`:

```markdown
# .claude/commands/my-command.md

# My Custom Command

Description of what this command does.

## Arguments: $ARGUMENTS

[Your command implementation]
```

### Command Chaining
Commands can be chained together for complex workflows:

1. `/prp-base-create` → Generate PRP
2. `/prp-base-execute` → Implement feature
3. `/review-general` → Validate code
4. `/smart-commit` → Commit changes
5. `/create-pr` → Submit for review

## Troubleshooting

### Common Issues

1. **Commands not appearing**: Ensure `.claude/commands/` directory exists
2. **Context not loading**: Use `/prime-core` to reload project context
3. **PRP execution fails**: Check that ai_docs are properly referenced

### Getting Help

- Review the original [PRPs-agentic-eng repository](https://github.com/Wirasm/PRPs-agentic-eng.git)
- Check the `CLAUDE.md` file for project-specific guidelines
- Use `/onboarding` for comprehensive setup instructions

---

**Ready to supercharge your development?** Start using these commands to experience the full power of AI-assisted development with Claude Code! 🚀 