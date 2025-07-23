# Claude Development Guidelines

## Overview

This document provides comprehensive guidelines for AI-assisted development using Claude and the PRP (Product Requirement Prompt) system. These guidelines ensure consistent, high-quality code generation and maintainable development practices.

## Claude Slash Commands and Task Management

### Using Slash Commands

Claude has access to powerful slash commands that should be used whenever possible to complete tasks efficiently. Always prioritize using these commands over manual instructions:

#### File Operations

- **`/read`** - Read file contents to understand current state
- **`/edit`** - Make precise edits to files with clear instructions
- **`/search`** - Search for specific code patterns or text
- **`/grep`** - Find exact text matches across files
- **`/list`** - Explore directory structure

#### Development Tools

- **`/run`** - Execute terminal commands for setup, testing, and deployment
- **`/mcp_supabase_*`** - Database operations, project management, and migrations
- **`/mcp_github_*`** - Repository management, issue tracking, and code review
- **`/mcp_context7_*`** - Access to up-to-date library documentation

#### AI-Assisted Development

- **`/codebase_search`** - Semantic search for relevant code patterns
- **`/file_search`** - Fuzzy file search for quick navigation

### Task Management Guidelines

#### For Long-Running Tasks

When working on complex, multi-step tasks:

1. **Break Down the Task**: Divide large tasks into smaller, manageable steps
2. **Use Slash Commands**: Leverage available tools to automate repetitive tasks
3. **Provide Progress Updates**: Give clear status updates at each step
4. **Suggest Next Steps**: Always provide actionable next steps when completing a phase

#### Progress Reporting Format

When completing a task phase, use this format:

```markdown
## ✅ Task Phase Complete: [Phase Name]

### What was accomplished:

- [ ] Specific achievement 1
- [ ] Specific achievement 2
- [ ] Specific achievement 3

### Next Steps:

1. **Immediate Next Action**: [Specific action with slash command if applicable]
2. **Follow-up Tasks**: [List of related tasks]
3. **Potential Issues**: [Any concerns or blockers to address]

### Commands Used:

- `/command1` - [purpose]
- `/command2` - [purpose]
```

#### Example Task Flow

```markdown
## 🔄 Working on: User Authentication System

### Current Phase: Database Schema Setup

- [x] Created users table with proper constraints
- [x] Added authentication-related columns
- [ ] Setting up Row Level Security policies

### Next Steps:

1. **Run RLS migration**: `/mcp_supabase_apply_migration`
2. **Test authentication flow**: `/run npm test auth`
3. **Update API documentation**: `/edit docs/api.md`

### Commands Used:

- `/mcp_supabase_apply_migration` - Created users table
- `/mcp_supabase_list_tables` - Verified table creation
```

### Best Practices for Slash Commands

#### 1. Always Use Available Tools

- Check available commands before manual work
- Use `/read` to understand current file state
- Use `/search` to find relevant patterns
- Use `/run` for terminal operations

#### 2. Be Specific with Commands

- Provide clear parameters for each command
- Explain the purpose of each command used
- Use appropriate flags and options

#### 3. Handle Errors Gracefully

- When commands fail, provide clear error analysis
- Suggest alternative approaches
- Document any workarounds needed

#### 4. Maintain Context

- Keep track of which files have been modified
- Note any configuration changes made
- Document any new dependencies added

### Integration with PRP System

When using slash commands with PRPs:

1. **Reference PRP Requirements**: Use `/read` to load PRP files
2. **Follow ai_docs Patterns**: Use `/search` to find relevant patterns
3. **Implement Step by Step**: Use `/edit` for each implementation step
4. **Test Continuously**: Use `/run` for testing and validation
5. **Document Progress**: Update PRP with completion status

## PRP System Integration

### What is a PRP?

A PRP (Product Requirement Prompt) is a structured document that provides comprehensive context to AI for generating production-ready code. It includes:

- Clear requirements and specifications
- Technical context and architecture patterns
- AI documentation references (ai_docs)
- Implementation guidelines and success criteria

### PRP Structure

```markdown
## Overview

Brief description of the feature or component to be developed.

## Requirements

### Functional Requirements

- [ ] Requirement 1
- [ ] Requirement 2

### Non-Functional Requirements

- Performance: [specifications]
- Security: [requirements]
- Accessibility: [standards]

## Technical Specifications

### Technology Stack

- Frontend: [React/Vue/Angular/etc.]
- Backend: [Node.js/Python/Go/etc.]
- Database: [PostgreSQL/MongoDB/etc.]

### Architecture Patterns

- State Management: [Redux/Zustand/Context/etc.]
- API Patterns: [REST/GraphQL/etc.]
- Database Patterns: [ORM/Query Builder/etc.]

## All Needed Context

### AI Documentation (Recommended)

- **file**: PRPs/ai_docs/[relevant-pattern].md
  **why**: [why this pattern is relevant]

### Project Files

- **file**: [path to relevant file]
  **why**: [why this file is important for context]

### External Documentation

- **url**: [external documentation URL]
  **why**: [why this documentation is needed]

## Implementation Notes

### Critical Requirements

- [ ] CRITICAL: [critical requirement]
- [ ] IMPORTANT: [important requirement]
- [ ] NOTE: [general note]

### Implementation Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Output

### Code Quality Standards

- [ ] Follows project TypeScript conventions
- [ ] Implements proper error handling
- [ ] Includes comprehensive testing
- [ ] Follows accessibility guidelines

### Deliverables

- [ ] Component/function implementation
- [ ] Unit tests
- [ ] Integration tests
- [ ] Documentation updates

## Success Criteria

- [ ] Feature works as specified
- [ ] Code follows project patterns
- [ ] Tests pass with 80%+ coverage
- [ ] Performance meets requirements
- [ ] Accessibility standards met
```

## AI Documentation (ai_docs) System

### Purpose

ai_docs provide curated documentation that gives AI deep context about your project's implementation patterns. This ensures:

- Consistent code generation
- Faster development
- Knowledge preservation
- Project-specific context

### Using ai_docs in PRPs

```markdown
## All Needed Context

### AI Documentation (Recommended)

- **file**: PRPs/ai_docs/react-typescript-conventions.md
  **why**: Component structure and TypeScript patterns
- **file**: PRPs/ai_docs/supabase-patterns.md
  **why**: Database operations and authentication patterns
- **file**: PRPs/ai_docs/admin-dashboard-patterns.md
  **why**: Admin interface patterns and conventions
```

### Creating New ai_docs

````markdown
# [Technology/Feature] Patterns

## Overview

Brief description of the patterns covered.

## Core Patterns

### Pattern 1: [Pattern Name]

```typescript
// Code example
```
````

### Pattern 2: [Pattern Name]

```typescript
// Code example
```

## Best Practices

- [ ] Practice 1
- [ ] Practice 2

## Common Pitfalls

- [ ] Pitfall 1 and how to avoid it
- [ ] Pitfall 2 and how to avoid it

## Related Patterns

- Link to related ai_docs files
- Cross-reference with other patterns

## Examples

- Real-world examples from your codebase
- Common use cases and implementations

````

## Development Commands

### PRP System Commands

```bash
# Set up PRP system
./scripts/setup-prp-system.sh

# Detect technology stack
python scripts/detect-tech-stack.py

# Create new PRP
cp PRPs/templates/prp_base.md PRPs/my-feature.md

# Validate PRP structure
python PRPs/run_prp.py PRPs/my-feature.md --validate-only

# Run PRP with AI
python PRPs/run_prp.py PRPs/my-feature.md
````

### AI-Assisted Development Workflow

1. **Create PRP**: Copy base template and fill in requirements
2. **Reference ai_docs**: Include relevant pattern documentation
3. **Run with AI**: Execute PRP to generate code
4. **Review and Iterate**: Refine PRP based on output quality
5. **Implement**: Copy generated code to project files
6. **Test**: Ensure code meets requirements and standards

## Best Practices for PRPs

### 1. Be Specific and Detailed

- Include exact function names and patterns
- Specify error handling requirements
- Define performance expectations
- Reference existing code patterns

### 2. Reference ai_docs

- Always include relevant ai_docs
- Explain why each ai_doc is relevant
- Cross-reference related patterns
- Keep ai_docs updated with new patterns

### 3. Include Project Context

- Reference specific project files
- Include external documentation URLs
- Explain project-specific requirements
- Consider existing architecture

### 4. Define Clear Success Criteria

- Specify test requirements
- Define performance metrics
- Include accessibility standards
- Set code quality expectations

### 5. Iterate and Improve

- Refine PRPs based on AI output
- Update ai_docs with successful patterns
- Learn from failed attempts
- Share successful PRPs with team

### 6. Leverage Slash Commands and Task Management

- **Use Available Tools**: Always check for available slash commands before manual work
- **Track Progress**: Use the progress reporting format for complex tasks
- **Provide Next Steps**: Include clear next steps in PRP completion
- **Document Commands**: Note which commands were used and their purpose
- **Handle Errors**: Document any issues and workarounds encountered

## AI Integration Guidelines

### Task Completion and Next Steps Protocol

When working with Claude on development tasks, follow this protocol for effective task management:

#### For Complex Tasks

1. **Initial Assessment**: Use `/read` and `/search` to understand the current state
2. **Task Breakdown**: Divide into phases with clear deliverables
3. **Progress Tracking**: Use the progress reporting format for each phase
4. **Next Steps**: Always provide actionable next steps when completing a phase

#### Task Completion Template

```markdown
## 🎯 Task Complete: [Task Name]

### Summary of Accomplishments:

- [ ] [Specific achievement with impact]
- [ ] [Specific achievement with impact]
- [ ] [Specific achievement with impact]

### Files Modified:

- `path/to/file1` - [what was changed]
- `path/to/file2` - [what was changed]

### Commands Executed:

- `/command1` - [purpose and outcome]
- `/command2` - [purpose and outcome]

### Next Steps:

1. **Immediate Actions** (if any):

   - [ ] Action 1 with `/command` if applicable
   - [ ] Action 2 with `/command` if applicable

2. **Follow-up Tasks**:

   - [ ] Related task 1
   - [ ] Related task 2

3. **Testing & Validation**:

   - [ ] Run tests: `/run npm test`
   - [ ] Check functionality: [specific check]
   - [ ] Verify deployment: [if applicable]

4. **Documentation Updates**:
   - [ ] Update README if needed
   - [ ] Update API docs if applicable
   - [ ] Update PRP with lessons learned

### Potential Issues to Monitor:

- [ ] Issue 1 and mitigation strategy
- [ ] Issue 2 and mitigation strategy
```

### Claude API Integration

```python
# Example integration with Claude API
import anthropic
import os

def run_with_claude(prp_content):
    # Set up Claude API client
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

    # Prepare prompt with PRP content and task management instructions
    prompt = f"""
    You are an expert software developer. Please implement the following feature:

    {prp_content}

    IMPORTANT: Use available slash commands whenever possible and provide clear next steps.

    Please provide:
    1. Complete implementation code using appropriate tools
    2. Unit tests
    3. Brief explanation of the implementation
    4. Clear next steps for testing and deployment
    5. Any potential issues to monitor
    """

    # Send to Claude
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text
```

### Custom AI Integration

```python
# Modify PRPs/run_prp.py for custom AI integration
def run_with_ai(prp_content, ai_tool="claude"):
    if ai_tool == "claude":
        return run_with_claude(prp_content)
    elif ai_tool == "openai":
        return run_with_openai(prp_content)
    elif ai_tool == "custom":
        return run_with_custom_ai(prp_content)
    else:
        print(f"Unsupported AI tool: {ai_tool}")
        return None
```

## Code Quality Standards

### TypeScript/JavaScript Standards

- Use TypeScript for type safety
- Follow ESLint and Prettier configurations
- Implement proper error handling
- Use async/await for asynchronous operations
- Include JSDoc comments for complex functions

### React Component Standards

- Use functional components with hooks
- Implement proper prop types
- Follow component naming conventions
- Use React.memo for performance optimization
- Implement proper error boundaries

### Testing Standards

- Write unit tests for all functions
- Use React Testing Library for components
- Achieve 80%+ code coverage
- Test error scenarios
- Use meaningful test descriptions

### Database Standards

- Use prepared statements for queries
- Implement proper connection pooling
- Handle database errors gracefully
- Use transactions for complex operations
- Follow naming conventions

## Project-Specific Guidelines

### React/TypeScript Projects

- Use shadcn/ui components
- Follow Tailwind CSS patterns
- Implement proper state management
- Use React Query for data fetching
- Follow component composition patterns

### Supabase Projects

- Use Supabase client for database operations
- Implement Row Level Security (RLS)
- Use Supabase Auth for authentication
- Follow Supabase best practices
- Use real-time subscriptions appropriately

### Admin Dashboard Projects

- Follow admin interface patterns
- Implement proper data visualization
- Use consistent UI components
- Follow accessibility guidelines
- Implement proper error handling

## Troubleshooting

### Common Issues

1. **AI generates inconsistent code**

   - Review ai_docs for completeness
   - Update patterns to match actual codebase
   - Be more specific in PRP requirements
   - Check for conflicting patterns

2. **PRPs take too long to create**

   - Use templates and examples
   - Reuse patterns from existing ai_docs
   - Start with simple PRPs and iterate
   - Focus on essential requirements first

3. **Generated code doesn't work**

   - Verify ai_docs are up to date
   - Check for missing dependencies
   - Review error handling
   - Test generated code thoroughly

4. **Team adoption is slow**

   - Provide training and examples
   - Start with simple features
   - Show successful implementations
   - Create team-specific ai_docs

5. **Slash commands not working as expected**

   - Verify command syntax and parameters
   - Check for required dependencies or setup
   - Use `/read` to understand current file state
   - Provide clear error messages and context
   - Suggest alternative approaches when commands fail

6. **Long-running tasks lack clear progress**
   - Break down tasks into smaller phases
   - Use progress reporting format consistently
   - Provide regular status updates
   - Always include next steps when completing phases
   - Document any blockers or dependencies

## Success Metrics

Track these metrics to measure AI-assisted development effectiveness:

### Code Quality Metrics

- Reduced bug count
- Improved code consistency
- Faster code reviews
- Higher test coverage

### Development Speed Metrics

- Faster feature delivery
- Reduced development time
- Quicker onboarding
- More efficient debugging

### Team Productivity Metrics

- Increased developer satisfaction
- Reduced knowledge silos
- Better code documentation
- Improved team collaboration

## Future Enhancements

### Advanced AI Features

- Pattern learning from successful code
- Automatic ai_docs updates
- Cross-project pattern sharing
- Intelligent PRP suggestions

### Integration Improvements

- IDE plugin integration
- Real-time AI assistance
- Automated code review
- Performance optimization suggestions

### Team Collaboration

- Shared pattern library
- PRP review workflows
- Pattern versioning
- Team-specific customizations

---

These guidelines ensure that AI-assisted development with Claude and the PRP system produces consistent, high-quality, and maintainable code while maximizing development efficiency and team productivity.
