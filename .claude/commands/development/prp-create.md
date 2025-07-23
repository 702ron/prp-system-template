# PRP Create

## Description
Create Product Requirement Prompts (PRPs) with language-specific templates and patterns. Replaces multiple PRP commands with a single, flexible command that supports different languages and frameworks.

## Usage
```
/prp-create [feature] [options]
```

## Arguments
- `feature` (required): The feature or functionality to implement
- `options` (optional): Additional options and flags

## Options
- `--language <lang>`: Specify programming language (js, ts, python, go, rust, php, java)
- `--framework <framework>`: Specify framework (react, vue, angular, next, express, django, flask, etc.)
- `--template <template>`: Use specific template (base, auth, api, ui, testing, deployment)
- `--output <path>`: Specify output path for PRP file
- `--ai-docs`: Include AI documentation patterns
- `--examples`: Include implementation examples
- `--testing`: Include testing requirements
- `--deployment`: Include deployment considerations

## Behavior
1. **Language Detection**: Automatically detects project language if not specified
2. **Template Selection**: Chooses appropriate template based on feature and language
3. **Pattern Integration**: Integrates language-specific patterns and best practices
4. **AI Documentation**: Includes AI documentation patterns when requested
5. **File Generation**: Creates comprehensive PRP file with all necessary sections

## Example Usage
```
# Basic feature creation
/prp-create implement user authentication
/prp-create add real-time notifications

# Language-specific creation
/prp-create implement API endpoints --language python --framework fastapi
/prp-create add form validation --language ts --framework react

# Template-specific creation
/prp-create implement database models --template api
/prp-create add unit tests --template testing

# Comprehensive creation
/prp-create implement payment system --language ts --framework next --ai-docs --testing --deployment
```

## Implementation
```python
import os
import sys
import json
from pathlib import Path
from datetime import datetime
import re

def create_prp(feature, **options):
    """
    Create a Product Requirement Prompt (PRP) with language-specific templates.
    """
    current_dir = Path.cwd()
    
    # Detect project language and framework if not specified
    language = options.get('language') or detect_language(current_dir)
    framework = options.get('framework') or detect_framework(current_dir, language)
    template = options.get('template') or select_template(feature, language, framework)
    
    print(f"🔧 Creating PRP for: {feature}")
    print(f"📝 Language: {language}, Framework: {framework}, Template: {template}")
    
    # Generate PRP content
    prp_content = generate_prp_content(feature, language, framework, template, options)
    
    # Determine output path
    output_path = options.get('output') or generate_output_path(feature, current_dir)
    
    # Write PRP file
    write_prp_file(output_path, prp_content)
    
    print(f"✅ PRP created: {output_path}")
    print(f"🚀 Run with: /prp-execute {output_path}")

def detect_language(project_dir):
    """Detect the primary programming language of the project."""
    language_patterns = {
        'js': ['package.json', 'node_modules'],
        'ts': ['tsconfig.json', '*.ts', '*.tsx'],
        'python': ['requirements.txt', '*.py', 'Pipfile'],
        'go': ['go.mod', '*.go'],
        'rust': ['Cargo.toml', '*.rs'],
        'php': ['composer.json', '*.php'],
        'java': ['pom.xml', 'build.gradle', '*.java']
    }
    
    for lang, patterns in language_patterns.items():
        for pattern in patterns:
            if '*' in pattern:
                # Handle glob patterns
                if list(project_dir.glob(pattern)):
                    return lang
            else:
                # Handle exact file matches
                if (project_dir / pattern).exists():
                    return lang
    
    return 'js'  # Default to JavaScript

def detect_framework(project_dir, language):
    """Detect the framework being used."""
    framework_patterns = {
        'js': {
            'react': ['react', 'react-dom'],
            'vue': ['vue', '@vue'],
            'angular': ['@angular'],
            'next': ['next'],
            'nuxt': ['nuxt'],
            'express': ['express'],
            'koa': ['koa'],
            'fastify': ['fastify']
        },
        'ts': {
            'react': ['react', 'react-dom'],
            'vue': ['vue', '@vue'],
            'angular': ['@angular'],
            'next': ['next'],
            'nuxt': ['nuxt'],
            'express': ['express'],
            'koa': ['koa'],
            'fastify': ['fastify']
        },
        'python': {
            'django': ['django'],
            'flask': ['flask'],
            'fastapi': ['fastapi', 'uvicorn']
        },
        'go': {
            'gin': ['gin'],
            'echo': ['echo'],
            'fiber': ['fiber']
        },
        'rust': {
            'actix': ['actix'],
            'rocket': ['rocket'],
            'warp': ['warp']
        }
    }
    
    if language in framework_patterns:
        # Check package.json or requirements.txt
        config_file = project_dir / ('package.json' if language in ['js', 'ts'] else 'requirements.txt')
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    content = f.read().lower()
                    for framework, patterns in framework_patterns[language].items():
                        if any(pattern in content for pattern in patterns):
                            return framework
            except:
                pass
    
    return 'base'  # Default framework

def select_template(feature, language, framework):
    """Select the most appropriate template based on feature and context."""
    feature_lower = feature.lower()
    
    # Template selection logic
    if any(word in feature_lower for word in ['auth', 'login', 'register', 'user']):
        return 'auth'
    elif any(word in feature_lower for word in ['api', 'endpoint', 'route', 'controller']):
        return 'api'
    elif any(word in feature_lower for word in ['ui', 'component', 'form', 'button', 'page']):
        return 'ui'
    elif any(word in feature_lower for word in ['test', 'spec', 'unit', 'integration']):
        return 'testing'
    elif any(word in feature_lower for word in ['deploy', 'ci', 'cd', 'pipeline']):
        return 'deployment'
    else:
        return 'base'

def generate_prp_content(feature, language, framework, template, options):
    """Generate comprehensive PRP content with language-specific patterns."""
    
    # Base template structure
    content = f"""# Product Requirement Prompt: {feature}

## Overview
Implement {feature} with best practices for {language.upper()} and {framework}.

## Requirements

### Functional Requirements
- [ ] Define specific functionality requirements
- [ ] List user stories and acceptance criteria
- [ ] Specify input/output expectations
- [ ] Define error handling requirements

### Technical Requirements
- [ ] Specify technology stack and dependencies
- [ ] Define performance requirements
- [ ] Specify security requirements
- [ ] Define scalability requirements

### Non-Functional Requirements
- [ ] Define accessibility requirements
- [ ] Specify browser/device compatibility
- [ ] Define performance benchmarks
- [ ] Specify monitoring and logging requirements

## Implementation Plan

### Phase 1: Setup and Foundation
- [ ] Set up development environment
- [ ] Configure project structure
- [ ] Install necessary dependencies
- [ ] Set up version control

### Phase 2: Core Implementation
- [ ] Implement core functionality
- [ ] Add error handling
- [ ] Implement validation
- [ ] Add logging and monitoring

### Phase 3: Testing and Quality Assurance
- [ ] Write unit tests
- [ ] Implement integration tests
- [ ] Perform code review
- [ ] Conduct security review

### Phase 4: Deployment and Documentation
- [ ] Prepare deployment configuration
- [ ] Create documentation
- [ ] Perform deployment
- [ ] Monitor and optimize

## Technical Specifications

### Architecture
- **Language**: {language.upper()}
- **Framework**: {framework}
- **Pattern**: {get_architecture_pattern(language, framework)}

### Dependencies
```
{get_dependencies(language, framework, template)}
```

### File Structure
```
{get_file_structure(language, framework, template)}
```

## Code Examples

### Basic Implementation
```{get_file_extension(language)}
{get_basic_example(language, framework, template)}
```

### Advanced Implementation
```{get_file_extension(language)}
{get_advanced_example(language, framework, template)}
```

## Testing Strategy

### Unit Tests
```{get_file_extension(language)}
{get_unit_test_example(language, framework)}
```

### Integration Tests
```{get_file_extension(language)}
{get_integration_test_example(language, framework)}
```

## Deployment Considerations

### Environment Configuration
- [ ] Set up development environment
- [ ] Configure staging environment
- [ ] Set up production environment
- [ ] Configure environment variables

### CI/CD Pipeline
- [ ] Set up automated testing
- [ ] Configure build process
- [ ] Set up deployment automation
- [ ] Configure monitoring and alerting

## Success Criteria
- [ ] All functional requirements met
- [ ] Performance benchmarks achieved
- [ ] Security requirements satisfied
- [ ] Documentation complete
- [ ] Tests passing with good coverage
- [ ] Deployment successful

## Notes
- Follow {language.upper()} best practices
- Use {framework} conventions and patterns
- Implement proper error handling
- Add comprehensive logging
- Ensure code is well-documented
- Maintain good test coverage

---
*Generated by PRP System - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    # Add language-specific patterns
    if options.get('ai_docs'):
        content += f"""

## AI Documentation Patterns

### Code Documentation
```{get_file_extension(language)}
{get_ai_doc_patterns(language, framework)}
```

### API Documentation
```{get_file_extension(language)}
{get_api_doc_patterns(language, framework)}
```
"""
    
    # Add examples if requested
    if options.get('examples'):
        content += f"""

## Implementation Examples

### Complete Example
```{get_file_extension(language)}
{get_complete_example(language, framework, template)}
```

### Usage Examples
```{get_file_extension(language)}
{get_usage_examples(language, framework)}
```
"""
    
    return content

def get_architecture_pattern(language, framework):
    """Get architecture pattern for language and framework."""
    patterns = {
        'js': {'react': 'Component-based', 'vue': 'Component-based', 'angular': 'Component-based', 'express': 'MVC'},
        'ts': {'react': 'Component-based', 'vue': 'Component-based', 'angular': 'Component-based', 'express': 'MVC'},
        'python': {'django': 'MVT', 'flask': 'MVC', 'fastapi': 'API-first'},
        'go': {'gin': 'MVC', 'echo': 'MVC', 'fiber': 'MVC'},
        'rust': {'actix': 'Actor-based', 'rocket': 'MVC', 'warp': 'Functional'}
    }
    
    return patterns.get(language, {}).get(framework, 'MVC')

def get_dependencies(language, framework, template):
    """Get dependencies for language and framework."""
    deps = {
        'js': {
            'react': ['react', 'react-dom'],
            'vue': ['vue'],
            'angular': ['@angular/core', '@angular/common'],
            'express': ['express'],
            'next': ['next', 'react', 'react-dom']
        },
        'ts': {
            'react': ['react', 'react-dom', '@types/react'],
            'vue': ['vue', '@vue/runtime-core'],
            'angular': ['@angular/core', '@angular/common'],
            'express': ['express', '@types/express'],
            'next': ['next', 'react', 'react-dom', '@types/react']
        },
        'python': {
            'django': ['django'],
            'flask': ['flask'],
            'fastapi': ['fastapi', 'uvicorn']
        }
    }
    
    base_deps = deps.get(language, {}).get(framework, [])
    
    # Add template-specific dependencies
    if template == 'auth':
        base_deps.extend(['bcrypt', 'jwt'] if language in ['js', 'ts'] else ['passlib', 'python-jose'])
    elif template == 'testing':
        base_deps.extend(['jest'] if language in ['js', 'ts'] else ['pytest'])
    
    return '\n'.join([f'"{dep}": "^latest"' if language in ['js', 'ts'] else dep for dep in base_deps])

def get_file_structure(language, framework, template):
    """Get recommended file structure."""
    structures = {
        'js': {
            'react': 'src/components/Feature/\n  ├── Feature.jsx\n  ├── Feature.test.js\n  └── index.js',
            'express': 'src/routes/feature.js\nsrc/controllers/featureController.js\nsrc/models/feature.js',
            'next': 'pages/feature/\n  ├── index.js\n  └── [id].js\ncomponents/Feature/\n  └── Feature.jsx'
        },
        'ts': {
            'react': 'src/components/Feature/\n  ├── Feature.tsx\n  ├── Feature.test.tsx\n  └── index.ts',
            'express': 'src/routes/feature.ts\nsrc/controllers/featureController.ts\nsrc/models/feature.ts',
            'next': 'pages/feature/\n  ├── index.tsx\n  └── [id].tsx\ncomponents/Feature/\n  └── Feature.tsx'
        },
        'python': {
            'django': 'app/\n  ├── models.py\n  ├── views.py\n  ├── urls.py\n  └── tests.py',
            'flask': 'app/\n  ├── models.py\n  ├── routes.py\n  └── tests.py',
            'fastapi': 'app/\n  ├── models.py\n  ├── routes.py\n  └── tests.py'
        }
    }
    
    return structures.get(language, {}).get(framework, 'src/feature/')

def get_file_extension(language):
    """Get file extension for language."""
    extensions = {
        'js': 'javascript',
        'ts': 'typescript',
        'python': 'python',
        'go': 'go',
        'rust': 'rust',
        'php': 'php',
        'java': 'java'
    }
    return extensions.get(language, 'javascript')

def get_basic_example(language, framework, template):
    """Get basic implementation example."""
    examples = {
        'js': {
            'react': 'import React from "react";\n\nconst Feature = () => {\n  return <div>Feature Component</div>;\n};\n\nexport default Feature;',
            'express': 'const express = require("express");\nconst router = express.Router();\n\nrouter.get("/", (req, res) => {\n  res.json({ message: "Feature endpoint" });\n});\n\nmodule.exports = router;'
        },
        'ts': {
            'react': 'import React from "react";\n\ninterface FeatureProps {\n  // Define props\n}\n\nconst Feature: React.FC<FeatureProps> = () => {\n  return <div>Feature Component</div>;\n};\n\nexport default Feature;',
            'express': 'import express from "express";\nconst router = express.Router();\n\nrouter.get("/", (req, res) => {\n  res.json({ message: "Feature endpoint" });\n});\n\nexport default router;'
        },
        'python': {
            'django': 'from django.shortcuts import render\nfrom django.http import JsonResponse\n\ndef feature_view(request):\n    return JsonResponse({"message": "Feature endpoint"})',
            'flask': 'from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route("/feature")\ndef feature():\n    return jsonify({"message": "Feature endpoint"})',
            'fastapi': 'from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/feature")\ndef feature():\n    return {"message": "Feature endpoint"}'
        }
    }
    
    return examples.get(language, {}).get(framework, '// Basic implementation example')

def get_advanced_example(language, framework, template):
    """Get advanced implementation example."""
    examples = {
        'js': {
            'react': 'import React, { useState, useEffect } from "react";\n\nconst Feature = () => {\n  const [data, setData] = useState(null);\n  \n  useEffect(() => {\n    // Fetch data\n  }, []);\n  \n  return <div>Advanced Feature</div>;\n};',
            'express': 'const express = require("express");\nconst router = express.Router();\n\nrouter.get("/", async (req, res) => {\n  try {\n    // Implementation\n    res.json({ success: true });\n  } catch (error) {\n    res.status(500).json({ error: error.message });\n  }\n});'
        },
        'ts': {
            'react': 'import React, { useState, useEffect } from "react";\n\ninterface FeatureData {\n  // Define interface\n}\n\nconst Feature: React.FC = () => {\n  const [data, setData] = useState<FeatureData | null>(null);\n  \n  useEffect(() => {\n    // Fetch data\n  }, []);\n  \n  return <div>Advanced Feature</div>;\n};',
            'express': 'import express from "express";\nconst router = express.Router();\n\nrouter.get("/", async (req, res) => {\n  try {\n    // Implementation\n    res.json({ success: true });\n  } catch (error) {\n    res.status(500).json({ error: error.message });\n  }\n});'
        }
    }
    
    return examples.get(language, {}).get(framework, '// Advanced implementation example')

def get_unit_test_example(language, framework):
    """Get unit test example."""
    examples = {
        'js': {
            'react': 'import { render, screen } from "@testing-library/react";\nimport Feature from "./Feature";\n\ntest("renders feature", () => {\n  render(<Feature />);\n  expect(screen.getByText(/feature/i)).toBeInTheDocument();\n});',
            'express': 'const request = require("supertest");\nconst app = require("../app");\n\ntest("GET /feature", async () => {\n  const response = await request(app).get("/feature");\n  expect(response.status).toBe(200);\n});'
        },
        'ts': {
            'react': 'import { render, screen } from "@testing-library/react";\nimport Feature from "./Feature";\n\ntest("renders feature", () => {\n  render(<Feature />);\n  expect(screen.getByText(/feature/i)).toBeInTheDocument();\n});',
            'express': 'import request from "supertest";\nimport app from "../app";\n\ntest("GET /feature", async () => {\n  const response = await request(app).get("/feature");\n  expect(response.status).toBe(200);\n});'
        },
        'python': {
            'django': 'from django.test import TestCase\nfrom django.urls import reverse\n\nclass FeatureTestCase(TestCase):\n    def test_feature_view(self):\n        response = self.client.get(reverse("feature"))\n        self.assertEqual(response.status_code, 200)',
            'flask': 'import pytest\nfrom app import app\n\n@pytest.fixture\ndef client():\n    app.config["TESTING"] = True\n    with app.test_client() as client:\n        yield client\n\ndef test_feature(client):\n    response = client.get("/feature")\n    assert response.status_code == 200',
            'fastapi': 'from fastapi.testclient import TestClient\nfrom app import app\n\nclient = TestClient(app)\n\ndef test_feature():\n    response = client.get("/feature")\n    assert response.status_code == 200'
        }
    }
    
    return examples.get(language, {}).get(framework, '// Unit test example')

def get_integration_test_example(language, framework):
    """Get integration test example."""
    examples = {
        'js': {
            'react': 'import { render, screen, fireEvent } from "@testing-library/react";\nimport Feature from "./Feature";\n\ntest("feature integration", async () => {\n  render(<Feature />);\n  \n  // Test user interaction\n  const button = screen.getByRole("button");\n  fireEvent.click(button);\n  \n  // Assert expected behavior\n});',
            'express': 'const request = require("supertest");\nconst app = require("../app");\n\ndescribe("Feature Integration", () => {\n  test("full feature flow", async () => {\n    // Test complete flow\n  });\n});'
        }
    }
    
    return examples.get(language, {}).get(framework, '// Integration test example')

def get_ai_doc_patterns(language, framework):
    """Get AI documentation patterns."""
    patterns = {
        'js': '/**\n * @description Feature component for handling user interactions\n * @param {Object} props - Component props\n * @param {string} props.title - Feature title\n * @returns {JSX.Element} Rendered component\n */',
        'ts': '/**\n * Feature component for handling user interactions\n * @param props - Component props\n * @returns Rendered component\n */',
        'python': '"""\nFeature module for handling user interactions.\n\nThis module provides functionality for processing user input\nand generating appropriate responses.\n\nArgs:\n    param1: Description of param1\n    param2: Description of param2\n\nReturns:\n    Description of return value\n\nRaises:\n    ValueError: Description of when this error occurs\n"""'
    }
    
    return patterns.get(language, '// AI documentation pattern')

def get_api_doc_patterns(language, framework):
    """Get API documentation patterns."""
    patterns = {
        'js': '/**\n * @api {get} /feature Get feature data\n * @apiName GetFeature\n * @apiGroup Feature\n * @apiSuccess {Object} data Feature data\n */',
        'ts': '/**\n * Get feature data\n * @param req - Express request object\n * @param res - Express response object\n */',
        'python': '"""\nGet feature data.\n\nEndpoint: GET /feature\n\nReturns:\n    JSON response with feature data\n\nExample:\n    GET /feature\n    Response: {"data": "feature_value"}\n"""'
    }
    
    return patterns.get(language, '// API documentation pattern')

def get_complete_example(language, framework, template):
    """Get complete implementation example."""
    return f"// Complete {template} implementation for {framework} in {language.upper()}"

def get_usage_examples(language, framework):
    """Get usage examples."""
    return f"// Usage examples for {framework} in {language.upper()}"

def generate_output_path(feature, project_dir):
    """Generate output path for PRP file."""
    # Create PRPs directory if it doesn't exist
    prps_dir = project_dir / 'PRPs'
    prps_dir.mkdir(exist_ok=True)
    
    # Generate filename
    filename = feature.lower().replace(' ', '-').replace('_', '-')
    filename = re.sub(r'[^a-z0-9-]', '', filename)
    
    return prps_dir / f'{filename}.md'

def write_prp_file(output_path, content):
    """Write PRP content to file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Main execution
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Create Product Requirement Prompt')
    parser.add_argument('feature', help='Feature to implement')
    parser.add_argument('--language', help='Programming language')
    parser.add_argument('--framework', help='Framework')
    parser.add_argument('--template', help='Template type')
    parser.add_argument('--output', help='Output path')
    parser.add_argument('--ai-docs', action='store_true', help='Include AI documentation')
    parser.add_argument('--examples', action='store_true', help='Include examples')
    parser.add_argument('--testing', action='store_true', help='Include testing')
    parser.add_argument('--deployment', action='store_true', help='Include deployment')
    
    args = parser.parse_args()
    
    options = {
        'language': args.language,
        'framework': args.framework,
        'template': args.template,
        'output': args.output,
        'ai_docs': args.ai_docs,
        'examples': args.examples,
        'testing': args.testing,
        'deployment': args.deployment
    }
    
    # Remove None values
    options = {k: v for k, v in options.items() if v is not None}
    
    create_prp(args.feature, **options)
```

## Notes
- This consolidated command replaces multiple PRP creation commands
- Supports multiple languages and frameworks
- Provides template-specific content
- Includes AI documentation patterns when requested
- Generates comprehensive PRP files with examples
- Reduces command complexity and improves usability 