# AI Documentation (ai_docs) - Project Patterns

## Overview

This directory contains curated documentation that provides AI with deep context about your project's implementation patterns. These documents help ensure consistent, production-ready code generation.

## Documentation Structure

### Technology-Specific Patterns
- `[technology]-patterns.md` - Core patterns for each technology
- `[technology]-conventions.md` - Coding conventions and standards
- `[technology]-best-practices.md` - Best practices and guidelines

### Feature-Specific Patterns
- `[feature]-patterns.md` - Patterns for specific features
- `[feature]-architecture.md` - Architecture patterns for features

### Integration Patterns
- `[service]-integration.md` - External service integration patterns
- `api-patterns.md` - API design and consumption patterns

## Usage in PRPs

Reference these documents in your PRPs:

```markdown
## All Needed Context

### AI Documentation (Recommended)
- **file**: PRPs/ai_docs/react-patterns.md
  **why**: Component structure and state management patterns
- **file**: PRPs/ai_docs/database-patterns.md
  **why**: Database operations and query patterns
```

## Creating New ai_docs

### Template Structure
```markdown
# [Technology/Feature] Patterns

## Overview
Brief description of the patterns covered.

## Core Patterns

### Pattern 1: [Pattern Name]
```[language]
// Code example
```

### Pattern 2: [Pattern Name]
```[language]
// Code example
```

## Best Practices
- [ ] Practice 1
- [ ] Practice 2

## Common Pitfalls
- [ ] Pitfall 1 and how to avoid it
- [ ] Pitfall 2 and how to avoid it
```

### When to Create New ai_docs
1. **New Technology**: When adding a new technology to the stack
2. **New Pattern**: When a successful pattern emerges
3. **Refactoring**: When consolidating multiple similar patterns
4. **Team Growth**: When onboarding new team members

## Maintenance

### Regular Updates
- Review ai_docs monthly
- Update patterns as codebase evolves
- Remove outdated patterns
- Add new successful patterns

### Quality Assurance
- Ensure all code examples work
- Keep patterns consistent with actual codebase
- Cross-reference related patterns
- Validate patterns with team review
