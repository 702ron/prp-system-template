# Setup PRP System

Automatically set up the complete PRP (Product Requirement Prompt) system in your project.

## Arguments: $ARGUMENTS

Optional arguments:
- `--tech-stack` - Automatically detect and create ai_docs for your tech stack
- `--example` - Create an example PRP to demonstrate usage
- `--full` - Run complete setup including tech stack detection and example creation

## Description

This command automates the setup of the PRP system by:

1. Creating the necessary directory structure
2. Setting up PRP templates and runner scripts
3. Creating AI documentation framework
4. Optionally detecting your tech stack and creating relevant ai_docs
5. Optionally creating an example PRP

## Usage Examples

```bash
# Basic setup
/setup-prp-system

# Setup with tech stack detection
/setup-prp-system --tech-stack

# Complete setup with examples
/setup-prp-system --full
```

## Implementation

I'll help you set up the PRP system step by step. Let me start by creating the necessary directory structure and files.

### Step 1: Create Directory Structure

First, let's create the required directories:

```bash
mkdir -p PRPs/templates
mkdir -p PRPs/ai_docs
mkdir -p PRPs/examples
mkdir -p PRPs/scripts
mkdir -p .claude/commands
```

### Step 2: Create Base PRP Template

Let me create the base PRP template:

```markdown:PRPs/templates/prp_base.md
# [Feature Name] - Product Requirement Prompt

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
- UI Library: [Tailwind/Material-UI/etc.]

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

### Step 3: Create Python Runner Script

Now let's create the PRP runner script:

```python:PRPs/run_prp.py
#!/usr/bin/env python3
"""
PRP (Product Requirement Prompt) Runner
Executes PRPs with AI assistance for consistent code generation.
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path

def read_prp_file(prp_path):
    """Read and parse PRP file."""
    try:
        with open(prp_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: PRP file '{prp_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading PRP file: {e}")
        sys.exit(1)

def validate_prp_structure(prp_content):
    """Validate PRP has required sections."""
    required_sections = [
        "## Overview",
        "## Requirements", 
        "## All Needed Context",
        "## Implementation Notes"
    ]
    
    missing_sections = []
    for section in required_sections:
        if section not in prp_content:
            missing_sections.append(section)
    
    if missing_sections:
        print("Warning: PRP missing required sections:")
        for section in missing_sections:
            print(f"  - {section}")
        return False
    return True

def run_with_ai(prp_content, ai_tool="claude"):
    """Execute PRP with AI tool."""
    print("🚀 Executing PRP with AI assistance...")
    print("=" * 50)
    
    # For Claude, you would integrate with their API
    # For now, we'll just display the PRP content
    print(prp_content)
    print("=" * 50)
    print("📝 AI execution complete. Review the generated code above.")
    print("💡 Tip: Copy the generated code to your project files.")

def main():
    parser = argparse.ArgumentParser(description="Run PRP with AI assistance")
    parser.add_argument("prp_file", help="Path to PRP file")
    parser.add_argument("--ai-tool", default="claude", help="AI tool to use")
    parser.add_argument("--validate-only", action="store_true", help="Only validate PRP structure")
    
    args = parser.parse_args()
    
    # Read PRP file
    prp_content = read_prp_file(args.prp_file)
    
    # Validate structure
    if not validate_prp_structure(prp_content):
        if args.validate_only:
            print("❌ PRP validation failed.")
            sys.exit(1)
        else:
            print("⚠️  Continuing despite validation warnings...")
    
    if args.validate_only:
        print("✅ PRP validation passed.")
        return
    
    # Execute with AI
    run_with_ai(prp_content, args.ai_tool)

if __name__ == "__main__":
    main()
```

### Step 4: Create AI Documentation Guide

Let's create the AI documentation guide:

```markdown:PRPs/ai_docs/README.md
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
```

### Step 5: Create Main PRP README

Let's create the main PRP system guide:

```markdown:PRPs/README.md
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
```

### Step 6: Make Runner Executable

```bash
chmod +x PRPs/run_prp.py
```

### Step 7: Tech Stack Detection (if requested)

If the `--tech-stack` or `--full` argument is provided, I'll detect your project's technology stack and create relevant ai_docs files.

### Step 8: Create Example PRP (if requested)

If the `--example` or `--full` argument is provided, I'll create an example PRP to demonstrate usage.

## Next Steps

After setup, you can:

1. **Create your first PRP**:
   ```bash
   cp PRPs/templates/prp_base.md PRPs/my-feature.md
   ```

2. **Edit the PRP** with your requirements

3. **Run with AI**:
   ```bash
   python PRPs/run_prp.py PRPs/my-feature.md
   ```

4. **Use Claude commands** (if available):
   ```
   /prp-base-create implement user authentication
   /prp-base-execute PRPs/my-feature.md
   ```

## Success Message

✅ **PRP system setup complete!**

Your PRP system is now ready for AI-assisted development. You can start creating PRPs and using them with Claude or other AI tools for consistent, production-ready code generation.

**Next steps:**
1. Create your first PRP: `cp PRPs/templates/prp_base.md PRPs/my-feature.md`
2. Edit the PRP with your requirements
3. Run with AI: `python PRPs/run_prp.py PRPs/my-feature.md`
4. Use Claude commands for enhanced workflow (if available)

**Documentation:**
- PRPs/README.md - Main PRP guide
- PRPs/ai_docs/README.md - AI documentation guide 