# Project Template Guide

## Overview

This guide explains how to create reusable project templates with the PRP system and ai_docs infrastructure. Templates allow you to quickly set up new projects with consistent patterns and AI-assisted development capabilities.

## Creating a Project Template

### Step 1: Set Up Base Template

1. **Create template repository**
```bash
# Create new repository for your template
mkdir my-project-template
cd my-project-template

git init
git remote add origin https://github.com/your-username/my-project-template.git
```

2. **Set up PRP system**
```bash
# Copy PRP system files
cp -r /path/to/prp-system-template/PRPs ./
cp -r /path/to/prp-system-template/scripts ./

# Make scripts executable
chmod +x scripts/setup-prp-system.sh
chmod +x PRPs/run_prp.py
```

### Step 2: Customize for Technology Stack

Based on your template's technology stack, create appropriate ai_docs:

**React/TypeScript Template:**
- `PRPs/ai_docs/react-typescript-conventions.md`
- `PRPs/ai_docs/tailwind-patterns.md`
- `PRPs/ai_docs/vite-patterns.md`

**Node.js/Express Template:**
- `PRPs/ai_docs/express-patterns.md`
- `PRPs/ai_docs/nodejs-patterns.md`
- `PRPs/ai_docs/jest-testing-patterns.md`

**Python/Django Template:**
- `PRPs/ai_docs/django-patterns.md`
- `PRPs/ai_docs/python-patterns.md`
- `PRPs/ai_docs/postgresql-patterns.md`

### Step 3: Create Template README

Include comprehensive documentation explaining:
- Template purpose and use cases
- Technology stack
- Setup instructions
- PRP system usage
- Customization options

Create `README.md`:

```markdown
# [Template Name] - Project Template

## Overview
Brief description of what this template provides.

## Technology Stack
- Frontend: [React/Vue/Angular]
- Backend: [Node.js/Python/Go]
- Database: [PostgreSQL/MongoDB]
- UI: [Tailwind/Material-UI]

## Features
- Structured PRP templates
- Technology-specific ai_docs
- Automated setup scripts
- Development guidelines

## Quick Start
```bash
# Use this template
npx create-my-template my-new-project
cd my-new-project

# Set up PRP system
./scripts/setup-prp-system.sh

# Detect tech stack
python scripts/detect-tech-stack.py
```

## Quick PRP Usage
```bash
# Create a new PRP
cp PRPs/templates/prp_base.md PRPs/my-feature.md

# Edit the PRP
nano PRPs/my-feature.md

# Run with AI
python PRPs/run_prp.py PRPs/my-feature.md
```

## Project Structure
```
my-project-template/
├── PRPs/                    # PRP system
├── scripts/                 # Automation scripts
├── src/                     # Template source code
├── docs/                    # Documentation
└── README.md               # Template documentation
```

## Customization

### Adding New Technologies
1. Update `scripts/detect-tech-stack.py`
2. Create corresponding ai_docs
3. Update template documentation

### Modifying Patterns
1. Edit ai_docs files with your patterns
2. Update PRP templates if needed
3. Test with sample PRPs

## License
[Your License]
```

### Step 4: Set Up GitHub Template

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial template setup"
git push -u origin main
```

2. **Enable template option**
- Go to repository settings
- Enable "Template repository" option
- Add template description and topics

### Step 5: Create Template Examples

```bash
# Create example PRPs
mkdir -p PRPs/examples
cp PRPs/templates/prp_base.md PRPs/examples/sample-feature.md
# Edit with template-specific examples
```

### Step 6: Set Up Distribution

#### Option A: NPM Package
```json
{
  "name": "create-my-template",
  "version": "1.0.0",
  "description": "Create new projects with PRP system",
  "bin": {
    "create-my-template": "./bin/create.js"
  },
  "files": [
    "template/",
    "bin/"
  ]
}
```

#### Option B: GitHub Template
- Use GitHub's template feature
- Share template URL with team
- Document usage instructions

## Using Project Templates

### Method 1: GitHub Template

1. Go to template repository
2. Click "Use this template"
3. Fill in repository details
4. Clone new repository
5. Follow setup instructions

### Method 2: Manual Copy

```bash
# Clone template
git clone https://github.com/your-username/my-project-template.git my-new-project
cd my-new-project

# Remove template-specific files
rm -rf .git
rm README.md

# Initialize new repository
git init
git add .
git commit -m "Initial commit"
```

### Method 3: Automated Setup

```bash
# Download and set up PRP system
curl -sSL https://raw.githubusercontent.com/your-username/my-project-template/main/scripts/setup-prp-system.sh | bash

# Detect tech stack
python scripts/detect-tech-stack.py
```

## Template Best Practices

### 1. Keep Templates Focused

- Create specific templates for different use cases
- Don't include unnecessary technologies
- Focus on common patterns and conventions

### 2. Maintain ai_docs Quality

- Include real, working code examples
- Keep patterns consistent with template stack
- Update patterns as technologies evolve

### 3. Provide Clear Documentation

- Explain template purpose and use cases
- Include setup and usage instructions
- Document customization options

### 4. Test Templates Regularly

- Create test projects using templates
- Verify PRP system works correctly
- Update examples and documentation

### 5. Version Templates

- Use semantic versioning for templates
- Maintain changelog of updates
- Provide migration guides

## Advanced Template Features

### 1. CI/CD Integration

```yaml
# .github/workflows/template-test.yml
name: Template Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test-template:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "18"

      - name: Install dependencies
        run: npm install
        
      - name: Test PRP system
        run: |
          python scripts/detect-tech-stack.py
          python PRPs/run_prp.py PRPs/examples/sample-feature.md --validate-only
          
      - name: Run tests
        run: npm test
```

### 2. Template Validation

```python
# scripts/validate-template.py
def validate_template():
    required_files = [
        'PRPs/templates/prp_base.md',
        'PRPs/run_prp.py',
        'scripts/setup-prp-system.sh',
        'README.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required template files:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        return False
    
    print("✅ Template validation passed")
    return True
```

### 3. Package.json Integration

```json
{
  "name": "my-project-template",
  "version": "1.0.0",
  "description": "Project template with PRP system",
  "scripts": {
    "setup-prp": "./scripts/setup-prp-system.sh",
    "detect-stack": "python scripts/detect-tech-stack.py",
    "validate-prp": "python PRPs/run_prp.py PRPs/examples/sample-feature.md --validate-only"
  },
  "files": ["PRPs/", "scripts/"]
}
```

## Troubleshooting

### Common Issues

1. **Template not working in new projects**
   - Check file permissions
   - Verify script paths
   - Test in clean environment

2. **ai_docs not relevant to new project**
   - Update tech stack detection
   - Create more generic patterns
   - Allow easy customization

3. **Setup script fails**
   - Check Python installation
   - Verify file permissions
   - Test script manually

## Distribution Options

### 1. GitHub Template Repository

- Most common approach
- Easy to use and maintain
- Good for team collaboration

### 2. NPM Package

- Good for Node.js projects
- Easy to install and update
- Can include CLI tools

### 3. Docker Image

- Good for complex setups
- Consistent environment
- Easy deployment

### 4. Git Submodules

- Good for shared components
- Version control integration
- Easy updates

## Success Metrics

Track these metrics to measure template effectiveness:

- **Adoption rate**: How many projects use the template
- **Setup time**: Time to get new project running
- **Consistency**: Code quality across projects
- **Maintenance**: Time spent updating templates
- **Team satisfaction**: Developer feedback

---

This systematic approach ensures that every new project can quickly adopt the PRP system and benefit from AI-assisted development while maintaining code quality and consistency across all your projects.