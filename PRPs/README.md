# PRP (Product Requirement Prompt) System

## Overview

This project uses a PRP system for AI-assisted development. PRPs are structured prompts that provide comprehensive context to AI for generating production-ready code.

## Quick Start

1. **Create a PRP**: Copy the base template
   ```bash
   cp PRPs/templates/prp_base.md PRPs/my-feature.md
   ```

2. **Edit the PRP**: Fill in your requirements and context

3. **Run with AI**: Execute the PRP
   ```bash
   python PRPs/run_prp.py PRPs/my-feature.md
   ```

## PRP Structure

```
PRPs/
├── templates/
│   └── prp_base.md          # Base template for all PRPs
├── ai_docs/                 # Curated documentation for AI context
│   ├── README.md            # Index and usage guide
│   └── [technology]-patterns.md
├── examples/                # Example PRPs
└── run_prp.py              # Python runner script
```

## Using ai_docs

The `ai_docs/` directory contains curated documentation that provides AI with deep context about your project's implementation patterns.

### Reference ai_docs in PRPs:
```markdown
## All Needed Context

### AI Documentation (Recommended)
- **file**: PRPs/ai_docs/react-patterns.md
  **why**: Component structure and state management patterns
```

## Best Practices

1. **Be specific**: Include exact patterns and function names
2. **Reference ai_docs**: Always include relevant documentation
3. **Iterate**: Refine PRPs based on AI output quality
4. **Document**: Keep PRPs updated as requirements change

## Examples

- [Example PRP with ai_docs](example-with-ai-docs.md)

## Documentation

- [AI Documentation Guide](ai_docs/README.md)
- [Setup Guide](../scripts/setup-guide.md)
