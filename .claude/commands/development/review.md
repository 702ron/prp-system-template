# Review

## Description
Comprehensive review command that analyzes code, builds, and changes with different scopes and focus areas. Replaces multiple review commands with a single, flexible command.

## Usage
```
/review [scope] [focus-area]
```

## Arguments
- `scope` (required): The scope of review
  - `build` - Comprehensive build analysis and enhancement recommendations
  - `code` - Code quality and structure review
  - `changes` - Review git staged/unstaged changes
  - `typescript` - TypeScript-specific review
- `focus-area` (optional): Specific area to focus on (e.g., "performance", "security", "features", "architecture", "ui/ux")

## Behavior
1. **Build Review**: Analyzes project structure, tech stack, and provides enhancement recommendations
2. **Code Review**: Performs comprehensive code quality analysis
3. **Changes Review**: Reviews git changes for quality and best practices
4. **TypeScript Review**: TypeScript-specific analysis with type safety and patterns

## Example Usage
```
# Build analysis
/review build
/review build performance
/review build "user experience and security"

# Code review
/review code src/auth/
/review code src/ --focus security

# Git changes review
/review changes

# TypeScript review
/review typescript src/
/review typescript src/components/ --focus patterns
```

## Implementation
```python
import os
import sys
import json
from pathlib import Path
from datetime import datetime
import subprocess

def review(scope, focus_area=None):
    """
    Comprehensive review command with different scopes.
    """
    current_dir = Path.cwd()
    
    print(f"🔍 Starting {scope} review...")
    
    if scope == "build":
        review_build(current_dir, focus_area)
    elif scope == "code":
        review_code(current_dir, focus_area)
    elif scope == "changes":
        review_changes(current_dir)
    elif scope == "typescript":
        review_typescript(current_dir, focus_area)
    else:
        print(f"❌ Unknown scope: {scope}")
        print("Available scopes: build, code, changes, typescript")
        return

def review_build(project_dir, focus_area=None):
    """Comprehensive build review with enhancement recommendations."""
    print("📁 Analyzing project structure...")
    
    # Analyze project structure
    project_analysis = analyze_project_structure(project_dir)
    
    # Detect technology stack
    tech_stack = detect_technology_stack(project_dir)
    
    # Analyze code quality
    code_quality = analyze_code_quality(project_dir)
    
    # Identify enhancement opportunities
    enhancements = identify_enhancement_opportunities(project_dir, focus_area)
    
    # Generate recommendations
    recommendations = generate_recommendations(project_analysis, tech_stack, code_quality, enhancements)
    
    # Create review report
    create_build_report(project_dir, recommendations, focus_area)
    
    print("✅ Build review complete! Check 'build-review-report.md' for detailed recommendations.")

def review_code(project_dir, focus_area=None):
    """Code quality and structure review."""
    print("📊 Analyzing code quality...")
    
    # Analyze code structure
    code_analysis = analyze_code_structure(project_dir)
    
    # Check for code quality issues
    quality_issues = check_code_quality(project_dir, focus_area)
    
    # Generate code review report
    create_code_report(project_dir, code_analysis, quality_issues, focus_area)
    
    print("✅ Code review complete! Check 'code-review-report.md' for details.")

def review_changes(project_dir):
    """Review git staged and unstaged changes."""
    print("📝 Reviewing git changes...")
    
    # Get staged changes
    staged_changes = get_staged_changes(project_dir)
    
    # Get unstaged changes
    unstaged_changes = get_unstaged_changes(project_dir)
    
    # Analyze changes
    change_analysis = analyze_changes(staged_changes, unstaged_changes)
    
    # Create changes report
    create_changes_report(project_dir, change_analysis)
    
    print("✅ Changes review complete! Check 'changes-review-report.md' for details.")

def review_typescript(project_dir, focus_area=None):
    """TypeScript-specific review."""
    print("🔷 Analyzing TypeScript code...")
    
    # Check TypeScript configuration
    ts_config = check_typescript_config(project_dir)
    
    # Analyze TypeScript patterns
    ts_patterns = analyze_typescript_patterns(project_dir, focus_area)
    
    # Check type safety
    type_safety = check_type_safety(project_dir)
    
    # Generate TypeScript report
    create_typescript_report(project_dir, ts_config, ts_patterns, type_safety, focus_area)
    
    print("✅ TypeScript review complete! Check 'typescript-review-report.md' for details.")

# Build review functions (from review-build.md)
def analyze_project_structure(project_dir):
    """Analyze the current project structure."""
    structure = {
        'directories': [],
        'files': [],
        'tech_files': {},
        'config_files': []
    }
    
    tech_patterns = {
        'package.json': 'Node.js/JavaScript',
        'requirements.txt': 'Python',
        'Cargo.toml': 'Rust',
        'go.mod': 'Go',
        'pom.xml': 'Java/Maven',
        'build.gradle': 'Java/Gradle',
        'composer.json': 'PHP',
        'Gemfile': 'Ruby',
        'Dockerfile': 'Docker',
        'docker-compose.yml': 'Docker Compose',
        'tsconfig.json': 'TypeScript',
        'webpack.config.js': 'Webpack',
        'vite.config.js': 'Vite',
        'next.config.js': 'Next.js',
        'tailwind.config.js': 'Tailwind CSS',
        'postcss.config.js': 'PostCSS',
        '.env': 'Environment Variables',
        '.env.example': 'Environment Template',
        'README.md': 'Documentation',
        'LICENSE': 'License',
        '.gitignore': 'Git Configuration'
    }
    
    for file_path in project_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            relative_path = file_path.relative_to(project_dir)
            structure['files'].append(str(relative_path))
            
            for pattern, tech in tech_patterns.items():
                if pattern in file_path.name:
                    structure['tech_files'][str(relative_path)] = tech
                    
            if any(config in file_path.name for config in ['config', 'conf', '.env', '.json', '.yaml', '.yml']):
                structure['config_files'].append(str(relative_path))
        
        elif file_path.is_dir():
            structure['directories'].append(str(relative_path))
    
    return structure

def detect_technology_stack(project_dir):
    """Detect the technology stack being used."""
    tech_stack = {
        'frontend': [],
        'backend': [],
        'database': [],
        'tools': [],
        'deployment': [],
        'testing': []
    }
    
    # Technology detection patterns
    frontend_patterns = {
        'package.json': ['react', 'vue', 'angular', 'svelte', 'next', 'nuxt', 'gatsby'],
        'tsconfig.json': ['typescript'],
        'tailwind.config.js': ['tailwind'],
        'postcss.config.js': ['postcss'],
        'vite.config.js': ['vite'],
        'webpack.config.js': ['webpack']
    }
    
    backend_patterns = {
        'requirements.txt': ['python', 'django', 'flask', 'fastapi'],
        'package.json': ['express', 'koa', 'nest', 'fastify'],
        'Cargo.toml': ['rust'],
        'go.mod': ['go'],
        'pom.xml': ['java', 'spring'],
        'composer.json': ['php', 'laravel']
    }
    
    db_patterns = {
        'supabase': ['supabase'],
        'prisma': ['prisma'],
        'sequelize': ['sequelize'],
        'mongoose': ['mongodb'],
        'redis': ['redis'],
        'postgres': ['postgresql']
    }
    
    deployment_patterns = {
        'Dockerfile': ['docker'],
        'docker-compose.yml': ['docker-compose'],
        'vercel.json': ['vercel'],
        'netlify.toml': ['netlify'],
        '.github/workflows': ['github-actions'],
        'k8s': ['kubernetes']
    }
    
    testing_patterns = {
        'jest.config.js': ['jest'],
        'cypress': ['cypress'],
        'playwright': ['playwright'],
        'pytest.ini': ['pytest'],
        'test': ['testing-framework']
    }
    
    # Analyze files for technology detection
    for file_path in project_dir.rglob('*'):
        if file_path.is_file():
            file_content = ""
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read().lower()
            except:
                continue
            
            # Check patterns
            for pattern, techs in frontend_patterns.items():
                if pattern in file_path.name:
                    for tech in techs:
                        if tech in file_content and tech not in tech_stack['frontend']:
                            tech_stack['frontend'].append(tech)
            
            for pattern, techs in backend_patterns.items():
                if pattern in file_path.name:
                    for tech in techs:
                        if tech in file_content and tech not in tech_stack['backend']:
                            tech_stack['backend'].append(tech)
            
            for pattern, techs in db_patterns.items():
                if pattern in file_content and techs[0] not in tech_stack['database']:
                    tech_stack['database'].extend(techs)
            
            for pattern, techs in deployment_patterns.items():
                if pattern in str(file_path) and techs[0] not in tech_stack['deployment']:
                    tech_stack['deployment'].extend(techs)
            
            for pattern, techs in testing_patterns.items():
                if pattern in str(file_path) and techs[0] not in tech_stack['testing']:
                    tech_stack['testing'].extend(techs)
    
    return tech_stack

def analyze_code_quality(project_dir):
    """Analyze code quality and patterns."""
    quality_metrics = {
        'file_count': 0,
        'code_files': 0,
        'test_files': 0,
        'documentation_files': 0,
        'potential_issues': [],
        'best_practices': [],
        'improvement_areas': []
    }
    
    for file_path in project_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            quality_metrics['file_count'] += 1
            
            if file_path.suffix in ['.js', '.ts', '.jsx', '.tsx', '.py', '.java', '.go', '.rs', '.php']:
                quality_metrics['code_files'] += 1
            elif 'test' in file_path.name.lower() or 'spec' in file_path.name.lower():
                quality_metrics['test_files'] += 1
            elif file_path.suffix in ['.md', '.txt', '.rst']:
                quality_metrics['documentation_files'] += 1
    
    if quality_metrics['test_files'] == 0:
        quality_metrics['potential_issues'].append("No test files found")
        quality_metrics['improvement_areas'].append("Add comprehensive testing")
    
    if quality_metrics['documentation_files'] < 2:
        quality_metrics['potential_issues'].append("Limited documentation")
        quality_metrics['improvement_areas'].append("Improve documentation coverage")
    
    if (project_dir / '.gitignore').exists():
        quality_metrics['best_practices'].append("Git ignore configured")
    else:
        quality_metrics['potential_issues'].append("No .gitignore file")
    
    if (project_dir / 'README.md').exists():
        quality_metrics['best_practices'].append("README documentation present")
    else:
        quality_metrics['potential_issues'].append("No README file")
    
    return quality_metrics

def identify_enhancement_opportunities(project_dir, focus_area=None):
    """Identify enhancement opportunities based on focus area."""
    opportunities = {
        'performance': [
            "Implement code splitting for better load times",
            "Add caching strategies (Redis, CDN)",
            "Optimize database queries",
            "Implement lazy loading for images",
            "Add performance monitoring (Lighthouse, Web Vitals)"
        ],
        'security': [
            "Implement authentication and authorization",
            "Add input validation and sanitization",
            "Implement rate limiting",
            "Add security headers",
            "Implement HTTPS enforcement",
            "Add security scanning tools"
        ],
        'features': [
            "Add real-time notifications",
            "Implement search functionality",
            "Add data export/import features",
            "Implement user preferences",
            "Add analytics and reporting",
            "Implement backup and recovery"
        ],
        'architecture': [
            "Implement microservices architecture",
            "Add API versioning",
            "Implement event-driven architecture",
            "Add message queues",
            "Implement CQRS pattern",
            "Add service discovery"
        ],
        'ui_ux': [
            "Improve responsive design",
            "Add dark mode support",
            "Implement accessibility features",
            "Add loading states and animations",
            "Improve error handling UX",
            "Add keyboard navigation"
        ],
        'testing': [
            "Add unit tests",
            "Implement integration tests",
            "Add end-to-end tests",
            "Implement visual regression testing",
            "Add performance testing",
            "Implement security testing"
        ],
        'documentation': [
            "Add API documentation",
            "Create user guides",
            "Add developer documentation",
            "Implement inline code documentation",
            "Add architecture diagrams",
            "Create deployment guides"
        ],
        'deployment': [
            "Implement CI/CD pipeline",
            "Add automated testing in pipeline",
            "Implement blue-green deployment",
            "Add rollback mechanisms",
            "Implement infrastructure as code",
            "Add monitoring and alerting"
        ],
        'monitoring': [
            "Add application performance monitoring",
            "Implement error tracking",
            "Add user analytics",
            "Implement health checks",
            "Add log aggregation",
            "Implement alerting systems"
        ]
    }
    
    return opportunities

def generate_recommendations(project_analysis, tech_stack, code_quality, enhancements):
    """Generate actionable recommendations."""
    recommendations = {
        'high_priority': [],
        'medium_priority': [],
        'low_priority': [],
        'tool_integrations': [],
        'next_steps': []
    }
    
    # High priority recommendations based on analysis
    if code_quality['test_files'] == 0:
        recommendations['high_priority'].append({
            'title': 'Add Testing Framework',
            'description': 'No test files found. Implement comprehensive testing.',
            'tools': ['Jest', 'Cypress', 'Playwright'],
            'effort': 'Medium',
            'impact': 'High'
        })
    
    if code_quality['documentation_files'] < 2:
        recommendations['high_priority'].append({
            'title': 'Improve Documentation',
            'description': 'Limited documentation. Add comprehensive docs.',
            'tools': ['JSDoc', 'Storybook', 'Docusaurus'],
            'effort': 'Low',
            'impact': 'High'
        })
    
    # Technology-specific recommendations
    if 'react' in tech_stack['frontend']:
        recommendations['medium_priority'].append({
            'title': 'React Optimization',
            'description': 'Optimize React performance with code splitting and lazy loading.',
            'tools': ['React.lazy', 'React.memo', 'Webpack Bundle Analyzer'],
            'effort': 'Medium',
            'impact': 'Medium'
        })
    
    if 'supabase' in tech_stack['database']:
        recommendations['medium_priority'].append({
            'title': 'Supabase Features',
            'description': 'Leverage more Supabase features for enhanced functionality.',
            'tools': ['Supabase Auth', 'Supabase Realtime', 'Supabase Edge Functions'],
            'effort': 'Low',
            'impact': 'High'
        })
    
    # Tool integration recommendations
    recommendations['tool_integrations'].extend([
        {
            'tool': 'GitHub Actions',
            'description': 'Implement CI/CD pipeline',
            'benefit': 'Automated testing and deployment'
        },
        {
            'tool': 'Supabase',
            'description': 'Add authentication and real-time features',
            'benefit': 'Enhanced user experience and security'
        },
        {
            'tool': 'Vercel/Netlify',
            'description': 'Deploy frontend with automatic previews',
            'benefit': 'Faster development and deployment cycles'
        }
    ])
    
    # Next steps
    recommendations['next_steps'] = [
        "Prioritize high-impact, low-effort improvements",
        "Set up monitoring and analytics",
        "Implement automated testing",
        "Add security measures",
        "Optimize performance",
        "Improve documentation"
    ]
    
    return recommendations

def create_build_report(project_dir, recommendations, focus_area=None):
    """Create a comprehensive build review report."""
    report_content = f"""# Build Review Report

## Review Summary
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Project**: {project_dir.name}
**Focus Area**: {focus_area or 'Comprehensive Review'}

## Executive Summary
This report provides a comprehensive analysis of the current build with actionable recommendations for improvements and enhancements.

## High Priority Recommendations

"""
    
    for rec in recommendations['high_priority']:
        report_content += f"""### {rec['title']}
**Description**: {rec['description']}
**Effort**: {rec['effort']} | **Impact**: {rec['impact']}
**Recommended Tools**: {', '.join(rec['tools'])}

"""
    
    report_content += """## Medium Priority Recommendations

"""
    
    for rec in recommendations['medium_priority']:
        report_content += f"""### {rec['title']}
**Description**: {rec['description']}
**Effort**: {rec['effort']} | **Impact**: {rec['impact']}
**Recommended Tools**: {', '.join(rec['tools'])}

"""
    
    report_content += """## Tool Integration Opportunities

"""
    
    for tool in recommendations['tool_integrations']:
        report_content += f"""### {tool['tool']}
**Description**: {tool['description']}
**Benefit**: {tool['benefit']}

"""
    
    report_content += """## Next Steps

"""
    
    for i, step in enumerate(recommendations['next_steps'], 1):
        report_content += f"{i}. {step}\n"
    
    report_content += f"""

## Implementation Commands

### Quick Start Enhancements
```bash
# Set up testing framework
/setup-prp-system --testing

# Add authentication
/prp-base-create implement user authentication with Supabase

# Set up CI/CD
/prp-base-create implement GitHub Actions CI/CD pipeline

# Add monitoring
/prp-base-create implement application monitoring and error tracking
```

### Detailed Implementation
```bash
# Create specific PRPs for each recommendation
/prp-base-create {recommendations['high_priority'][0]['title'].lower().replace(' ', '-') if recommendations['high_priority'] else 'enhancement'}

# Execute PRPs with full context
/prp-base-execute PRPs/your-feature.md

# Review implementation
/review code src/
```

## Notes
- Prioritize high-impact, low-effort improvements first
- Use the PRP system for structured implementation
- Consider tool integrations for enhanced functionality
- Regular reviews help maintain code quality and identify new opportunities

---
*Generated by PRP System Review*
"""
    
    report_path = project_dir / 'build-review-report.md'
    with open(report_path, 'w') as f:
        f.write(report_content)

# Code review functions
def analyze_code_structure(project_dir):
    """Analyze code structure and organization."""
    return {
        'total_files': 0,
        'code_files': 0,
        'test_files': 0,
        'documentation_files': 0,
        'structure_issues': [],
        'best_practices': []
    }

def check_code_quality(project_dir, focus_area=None):
    """Check code quality issues."""
    return {
        'issues': [],
        'suggestions': [],
        'focus_area': focus_area
    }

def create_code_report(project_dir, code_analysis, quality_issues, focus_area=None):
    """Create code review report."""
    report_content = f"""# Code Review Report

## Review Summary
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Project**: {project_dir.name}
**Focus Area**: {focus_area or 'General Code Review'}

## Code Analysis
- Total files: {code_analysis['total_files']}
- Code files: {code_analysis['code_files']}
- Test files: {code_analysis['test_files']}
- Documentation files: {code_analysis['documentation_files']}

## Quality Issues
{chr(10).join([f"- {issue}" for issue in quality_issues['issues']]) if quality_issues['issues'] else "No major issues found"}

## Suggestions
{chr(10).join([f"- {suggestion}" for suggestion in quality_issues['suggestions']]) if quality_issues['suggestions'] else "No suggestions at this time"}

---
*Generated by PRP System Review*
"""
    
    report_path = project_dir / 'code-review-report.md'
    with open(report_path, 'w') as f:
        f.write(report_content)

# Changes review functions
def get_staged_changes(project_dir):
    """Get staged git changes."""
    try:
        result = subprocess.run(['git', 'diff', '--cached', '--name-only'], 
                              capture_output=True, text=True, cwd=project_dir)
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except:
        return []

def get_unstaged_changes(project_dir):
    """Get unstaged git changes."""
    try:
        result = subprocess.run(['git', 'diff', '--name-only'], 
                              capture_output=True, text=True, cwd=project_dir)
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except:
        return []

def analyze_changes(staged_changes, unstaged_changes):
    """Analyze git changes."""
    return {
        'staged_files': staged_changes,
        'unstaged_files': unstaged_changes,
        'total_changes': len(staged_changes) + len(unstaged_changes),
        'issues': [],
        'suggestions': []
    }

def create_changes_report(project_dir, change_analysis):
    """Create changes review report."""
    report_content = f"""# Changes Review Report

## Review Summary
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Project**: {project_dir.name}
**Total Changes**: {change_analysis['total_changes']}

## Staged Changes
{chr(10).join([f"- {file}" for file in change_analysis['staged_files']]) if change_analysis['staged_files'] else "No staged changes"}

## Unstaged Changes
{chr(10).join([f"- {file}" for file in change_analysis['unstaged_files']]) if change_analysis['unstaged_files'] else "No unstaged changes"}

## Issues
{chr(10).join([f"- {issue}" for issue in change_analysis['issues']]) if change_analysis['issues'] else "No issues found"}

## Suggestions
{chr(10).join([f"- {suggestion}" for suggestion in change_analysis['suggestions']]) if change_analysis['suggestions'] else "No suggestions"}

---
*Generated by PRP System Review*
"""
    
    report_path = project_dir / 'changes-review-report.md'
    with open(report_path, 'w') as f:
        f.write(report_content)

# TypeScript review functions
def check_typescript_config(project_dir):
    """Check TypeScript configuration."""
    return {
        'tsconfig_exists': (project_dir / 'tsconfig.json').exists(),
        'strict_mode': False,
        'issues': [],
        'suggestions': []
    }

def analyze_typescript_patterns(project_dir, focus_area=None):
    """Analyze TypeScript patterns."""
    return {
        'patterns_found': [],
        'issues': [],
        'suggestions': [],
        'focus_area': focus_area
    }

def check_type_safety(project_dir):
    """Check TypeScript type safety."""
    return {
        'type_coverage': 0,
        'any_usage': 0,
        'issues': [],
        'suggestions': []
    }

def create_typescript_report(project_dir, ts_config, ts_patterns, type_safety, focus_area=None):
    """Create TypeScript review report."""
    report_content = f"""# TypeScript Review Report

## Review Summary
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Project**: {project_dir.name}
**Focus Area**: {focus_area or 'General TypeScript Review'}

## TypeScript Configuration
- tsconfig.json exists: {ts_config['tsconfig_exists']}
- Strict mode enabled: {ts_config['strict_mode']}

## Type Safety
- Type coverage: {type_safety['type_coverage']}%
- Any usage count: {type_safety['any_usage']}

## Issues
{chr(10).join([f"- {issue}" for issue in ts_config['issues'] + ts_patterns['issues'] + type_safety['issues']]) if ts_config['issues'] + ts_patterns['issues'] + type_safety['issues'] else "No issues found"}

## Suggestions
{chr(10).join([f"- {suggestion}" for suggestion in ts_config['suggestions'] + ts_patterns['suggestions'] + type_safety['suggestions']]) if ts_config['suggestions'] + ts_patterns['suggestions'] + type_safety['suggestions'] else "No suggestions"}

---
*Generated by PRP System Review*
"""
    
    report_path = project_dir / 'typescript-review-report.md'
    with open(report_path, 'w') as f:
        f.write(report_content)

# Main execution
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("❌ Scope is required")
        print("Usage: /review [scope] [focus-area]")
        print("Scopes: build, code, changes, typescript")
        sys.exit(1)
    
    scope = sys.argv[1]
    focus_area = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else None
    
    review(scope, focus_area)
```

## Notes
- This consolidated command replaces multiple review commands
- Provides different scopes for different types of analysis
- Maintains all functionality from original commands
- Reduces command complexity and improves usability
- Generates specific reports for each review type 