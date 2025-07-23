#!/usr/bin/env python3
"""
Detect project technology stack and suggest ai_docs to create.
"""

import os
import json
from pathlib import Path


def detect_tech_stack():
    """Detect technology stack from project files."""
    tech_stack = {
        'frontend': [],
        'backend': [],
        'database': [],
        'tools': []
    }

    # Check for package.json (Node.js/React/Vue/Angular)
    if os.path.exists('package.json'):
        with open('package.json', 'r') as f:
            package_data = json.load(f)
            dependencies = package_data.get('dependencies', {})
            dev_dependencies = package_data.get('devDependencies', {})
            all_deps = {**dependencies, **dev_dependencies}

            # Frontend frameworks
            if 'react' in all_deps:
                tech_stack['frontend'].append('React')
            if 'vue' in all_deps:
                tech_stack['frontend'].append('Vue')
            if 'angular' in all_deps:
                tech_stack['frontend'].append('Angular')
            if 'next' in all_deps:
                tech_stack['frontend'].append('Next.js')
            if 'nuxt' in all_deps:
                tech_stack['frontend'].append('Nuxt.js')

            # UI libraries
            if 'tailwindcss' in all_deps:
                tech_stack['frontend'].append('Tailwind CSS')
            if '@mui/material' in all_deps:
                tech_stack['frontend'].append('Material-UI')
            if '@chakra-ui/react' in all_deps:
                tech_stack['frontend'].append('Chakra UI')
            if 'antd' in all_deps:
                tech_stack['frontend'].append('Ant Design')

            # State management
            if 'redux' in all_deps:
                tech_stack['frontend'].append('Redux')
            if 'zustand' in all_deps:
                tech_stack['frontend'].append('Zustand')
            if '@tanstack/react-query' in all_deps:
                tech_stack['frontend'].append('TanStack Query')

            # Backend frameworks
            if 'express' in all_deps:
                tech_stack['backend'].append('Express')
            if 'fastify' in all_deps:
                tech_stack['backend'].append('Fastify')
            if 'koa' in all_deps:
                tech_stack['backend'].append('Koa')
            if 'nest' in all_deps:
                tech_stack['backend'].append('NestJS')

            # TypeScript
            if 'typescript' in all_deps:
                tech_stack['tools'].append('TypeScript')

    # Check for Python files and requirements
    if any(Path('.').glob('*.py')):
        tech_stack['backend'].append('Python')

    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = f.read().lower()
            if 'django' in requirements:
                tech_stack['backend'].append('Django')
            if 'flask' in requirements:
                tech_stack['backend'].append('Flask')
            if 'fastapi' in requirements:
                tech_stack['backend'].append('FastAPI')
            if 'celery' in requirements:
                tech_stack['backend'].append('Celery')

    # Check for pyproject.toml
    if os.path.exists('pyproject.toml'):
        tech_stack['backend'].append('Python')

    # Check for Go files
    if any(Path('.').glob('*.go')):
        tech_stack['backend'].append('Go')

    # Check for Rust files
    if any(Path('.').glob('*.rs')) or os.path.exists('Cargo.toml'):
        tech_stack['backend'].append('Rust')

    # Check for database files
    if os.path.exists('supabase'):
        tech_stack['database'].append('Supabase')
    if os.path.exists('prisma'):
        tech_stack['database'].append('Prisma')
    if os.path.exists('migrations'):
        tech_stack['database'].append('Database Migrations')
    if any(Path('.').glob('*.sql')):
        tech_stack['database'].append('SQL')

    # Check for specific database files
    if os.path.exists('docker-compose.yml'):
        with open('docker-compose.yml', 'r') as f:
            content = f.read().lower()
            if 'postgres' in content:
                tech_stack['database'].append('PostgreSQL')
            if 'mysql' in content:
                tech_stack['database'].append('MySQL')
            if 'mongodb' in content:
                tech_stack['database'].append('MongoDB')
            if 'redis' in content:
                tech_stack['database'].append('Redis')

    # Check for build tools
    if os.path.exists('vite.config.js') or os.path.exists('vite.config.ts'):
        tech_stack['tools'].append('Vite')
    if os.path.exists('webpack.config.js'):
        tech_stack['tools'].append('Webpack')
    if os.path.exists('rollup.config.js'):
        tech_stack['tools'].append('Rollup')

    # Check for testing frameworks
    if os.path.exists('jest.config.js') or 'jest' in tech_stack.get('tools', []):
        tech_stack['tools'].append('Jest')
    if os.path.exists('cypress.config.js'):
        tech_stack['tools'].append('Cypress')
    if os.path.exists('playwright.config.js'):
        tech_stack['tools'].append('Playwright')

    return tech_stack


def suggest_ai_docs(tech_stack):
    """Suggest ai_docs to create based on tech stack."""
    suggestions = []

    # Frontend suggestions
    for frontend in tech_stack['frontend']:
        if frontend == 'React':
            suggestions.extend([
                'react-typescript-conventions.md',
                'react-hooks-patterns.md',
                'react-component-patterns.md'
            ])
        elif frontend == 'Vue':
            suggestions.extend([
                'vue-composition-patterns.md',
                'vue-options-patterns.md'
            ])
        elif frontend == 'Angular':
            suggestions.extend([
                'angular-patterns.md',
                'angular-services-patterns.md'
            ])
        elif frontend == 'Next.js':
            suggestions.extend([
                'nextjs-patterns.md',
                'nextjs-routing-patterns.md'
            ])
        elif frontend == 'Tailwind CSS':
            suggestions.append('tailwind-patterns.md')
        elif frontend == 'Material-UI':
            suggestions.append('mui-patterns.md')
        elif frontend == 'Redux':
            suggestions.append('redux-patterns.md')
        elif frontend == 'Zustand':
            suggestions.append('zustand-patterns.md')
        elif frontend == 'TanStack Query':
            suggestions.append('react-query-patterns.md')

    # Backend suggestions
    for backend in tech_stack['backend']:
        if backend == 'Express':
            suggestions.extend([
                'express-patterns.md',
                'nodejs-patterns.md',
                'express-middleware-patterns.md'
            ])
        elif backend == 'NestJS':
            suggestions.extend([
                'nestjs-patterns.md',
                'nestjs-module-patterns.md'
            ])
        elif backend == 'Django':
            suggestions.extend([
                'django-patterns.md',
                'django-models-patterns.md',
                'django-views-patterns.md'
            ])
        elif backend == 'Flask':
            suggestions.extend([
                'flask-patterns.md',
                'flask-blueprint-patterns.md'
            ])
        elif backend == 'FastAPI':
            suggestions.extend([
                'fastapi-patterns.md',
                'fastapi-dependency-patterns.md'
            ])
        elif backend == 'Go':
            suggestions.extend([
                'go-patterns.md',
                'go-http-patterns.md'
            ])
        elif backend == 'Rust':
            suggestions.extend([
                'rust-patterns.md',
                'rust-web-patterns.md'
            ])

    # Database suggestions
    for database in tech_stack['database']:
        if database == 'Supabase':
            suggestions.extend([
                'supabase-patterns.md',
                'supabase-auth-patterns.md',
                'supabase-realtime-patterns.md'
            ])
        elif database == 'Prisma':
            suggestions.extend([
                'prisma-patterns.md',
                'prisma-migration-patterns.md'
            ])
        elif database == 'PostgreSQL':
            suggestions.append('postgresql-patterns.md')
        elif database == 'MongoDB':
            suggestions.append('mongodb-patterns.md')
        elif database == 'Redis':
            suggestions.append('redis-patterns.md')

    # Tool suggestions
    for tool in tech_stack['tools']:
        if tool == 'TypeScript':
            suggestions.append('typescript-patterns.md')
        elif tool == 'Vite':
            suggestions.append('vite-patterns.md')
        elif tool == 'Jest':
            suggestions.append('jest-testing-patterns.md')
        elif tool == 'Cypress':
            suggestions.append('cypress-testing-patterns.md')

    # Remove duplicates and return
    return list(set(suggestions))


def create_ai_docs_files(suggestions):
    """Create the suggested ai_docs files with basic templates."""
    created_files = []

    for suggestion in suggestions:
        file_path = f"PRPs/ai_docs/{suggestion}"
        if not os.path.exists(file_path):
            # Create basic template based on file name
            template = create_basic_template(suggestion)

            with open(file_path, 'w') as f:
                f.write(template)

            created_files.append(file_path)

    return created_files


def create_basic_template(filename):
    """Create a basic template for ai_docs files."""
    name = filename.replace('.md', '').replace('-', ' ').title()

    return f"""# {name}

## Overview

Brief description of the patterns covered in this document.

## Core Patterns

### Pattern 1: [Pattern Name]
```typescript
// Code example
```

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
"""


def main():
    print("🔍 Detecting technology stack...")
    tech_stack = detect_tech_stack()

    print("\n📋 Detected Technology Stack:")
    for category, technologies in tech_stack.items():
        if technologies:
            print(f"  {category.title()}: {', '.join(technologies)}")

    suggestions = suggest_ai_docs(tech_stack)

    print("\n📝 Suggested ai_docs to create:")
    for suggestion in suggestions:
        print(f"  - PRPs/ai_docs/{suggestion}")

    if suggestions:
        print("\n💡 Would you like to create these ai_docs files? (y/n): ", end="")
        response = input().lower().strip()

        if response in ['y', 'yes']:
            created_files = create_ai_docs_files(suggestions)
            print(f"\n✅ Created {len(created_files)} ai_docs files:")
            for file_path in created_files:
                print(f"  - {file_path}")

            print("\n📝 Next steps:")
            print("  1. Edit the created ai_docs files with your project's patterns")
            print("  2. Create your first PRP: cp PRPs/templates/prp_base.md PRPs/my-feature.md")
            print("  3. Reference the ai_docs in your PRP")
        else:
            print("\n💡 Run this command to create the suggested ai_docs:")
            suggestion_files = ' '.join([f'PRPs/ai_docs/{s}' for s in suggestions])
            print(f"  touch {suggestion_files}")
    else:
        print("\n💡 No specific ai_docs suggestions. Consider creating:")
        print("  - PRPs/ai_docs/general-patterns.md")
        print("  - PRPs/ai_docs/project-conventions.md")


if __name__ == "__main__":
    main()
