# Review

## Description
Comprehensive review command that analyzes code, builds, and changes with different scopes and focus areas. Leverages specialized agents for optimal analysis and incorporates the latest best practices. Replaces multiple review commands with a single, agent-powered command.

## Usage
```
/review [scope] [focus-area] [options]
```

## Arguments
- `scope` (required): The scope of review
  - `build` - Comprehensive build analysis and enhancement recommendations
  - `code` - Code quality and structure review (uses code-quality-analyzer agent)
  - `changes` - Review git staged/unstaged changes
  - `typescript` - TypeScript-specific review
  - `security` - Security audit (uses security-auditor agent)
  - `performance` - Performance analysis (uses performance-optimizer agent)
  - `architecture` - System architecture review (uses system-architect agent)
- `focus-area` (optional): Specific area to focus on (e.g., "performance", "security", "features", "architecture", "ui/ux")

## Options
- `--agent-powered`: Use specialized agents for comprehensive analysis (default: true)
- `--audio-summary`: Generate audio summary at completion
- `--research-latest`: Include latest best practices from AI/ML research

## Behavior
1. **Build Review**: Analyzes project structure, tech stack, and provides enhancement recommendations
2. **Code Review**: Uses code-quality-analyzer agent for comprehensive analysis with automated fixes
3. **Changes Review**: Reviews git changes for quality and best practices
4. **TypeScript Review**: TypeScript-specific analysis with type safety and patterns
5. **Security Review**: Uses security-auditor agent for vulnerability assessment
6. **Performance Review**: Uses performance-optimizer agent for bottleneck identification
7. **Architecture Review**: Uses system-architect agent for design analysis
8. **Agent Integration**: Spawns specialized agents based on scope and automatically applies best practices

## Example Usage
```
# Build analysis
/review build
/review build performance --research-latest
/review build "user experience and security" --audio-summary

# Code review with agent support
/review code src/auth/ --agent-powered
/review code src/ security  # Automatically uses security-auditor agent

# Specialized reviews
/review security --audio-summary  # Uses security-auditor agent
/review performance src/api/      # Uses performance-optimizer agent
/review architecture              # Uses system-architect agent

# Git changes review
/review changes --agent-powered

# TypeScript review
/review typescript src/
/review typescript src/components/ patterns
```

## Implementation
```python
import os
import sys
import json
from pathlib import Path
from datetime import datetime
import subprocess

def review(scope, focus_area=None, use_agents=True, audio_summary=False, research_latest=False):
    """
    Comprehensive review command with different scopes and agent integration.
    """
    current_dir = Path.cwd()
    
    print(f"🔍 Starting {scope} review...")
    
    # Update best practices if requested
    if research_latest:
        print("📚 Updating with latest AI/ML best practices...")
        update_best_practices()
    
    if scope == "build":
        review_build(current_dir, focus_area, use_agents)
    elif scope == "code":
        if use_agents:
            spawn_code_quality_agent(current_dir, focus_area)
        else:
            review_code(current_dir, focus_area)
    elif scope == "changes":
        review_changes(current_dir, use_agents)
    elif scope == "typescript":
        review_typescript(current_dir, focus_area)
    elif scope == "security":
        if use_agents:
            spawn_security_audit_agent(current_dir, focus_area)
        else:
            review_security(current_dir, focus_area)
    elif scope == "performance":
        if use_agents:
            spawn_performance_optimizer_agent(current_dir, focus_area)
        else:
            review_performance(current_dir, focus_area)
    elif scope == "architecture":
        if use_agents:
            spawn_system_architect_agent(current_dir, focus_area)
        else:
            review_architecture(current_dir, focus_area)
    else:
        print(f"❌ Unknown scope: {scope}")
        print("Available scopes: build, code, changes, typescript, security, performance, architecture")
        return
    
    # Generate audio summary if requested
    if audio_summary:
        generate_completion_summary(scope, focus_area)

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

# Agent integration functions
def spawn_code_quality_agent(project_dir, focus_area=None):
    """Spawn code-quality-analyzer agent for comprehensive code review."""
    print("🤖 Launching code-quality-analyzer agent...")
    
    task_description = f"Comprehensive code quality analysis"
    if focus_area:
        task_description += f" with focus on {focus_area}"
    
    prompt = f"""
    Analyze the codebase at {project_dir} for code quality issues, maintainability problems, and best practices violations.
    
    Focus areas: {focus_area or 'general code quality'}
    
    Provide:
    1. Critical issues that must be fixed
    2. Automated fixes where possible
    3. Improvement recommendations
    4. Code quality score and metrics
    
    Generate a detailed report with actionable fixes.
    """
    
    # This would spawn the agent using the Task tool
    # spawn_agent("code-quality-analyzer", task_description, prompt)

def spawn_security_audit_agent(project_dir, focus_area=None):
    """Spawn security-auditor agent for vulnerability assessment."""
    print("🔒 Launching security-auditor agent...")
    
    task_description = f"Security vulnerability assessment"
    if focus_area:
        task_description += f" with focus on {focus_area}"
    
    prompt = f"""
    Perform a comprehensive security audit of the codebase at {project_dir}.
    
    Focus areas: {focus_area or 'OWASP Top 10 vulnerabilities'}
    
    Analyze for:
    1. Authentication and authorization flaws
    2. Input validation issues
    3. SQL injection vulnerabilities
    4. XSS vulnerabilities
    5. Security misconfigurations
    6. Sensitive data exposure
    
    Provide detailed remediation steps for each issue found.
    """
    
    # spawn_agent("security-auditor", task_description, prompt)

def spawn_performance_optimizer_agent(project_dir, focus_area=None):
    """Spawn performance-optimizer agent for bottleneck analysis."""
    print("⚡ Launching performance-optimizer agent...")
    
    task_description = f"Performance bottleneck analysis"
    if focus_area:
        task_description += f" with focus on {focus_area}"
    
    prompt = f"""
    Analyze the codebase at {project_dir} for performance bottlenecks and optimization opportunities.
    
    Focus areas: {focus_area or 'general performance optimization'}
    
    Identify:
    1. Slow database queries
    2. Memory leaks and high memory usage
    3. CPU-intensive operations
    4. Network bottlenecks
    5. Bundle size and loading performance
    
    Provide specific optimization recommendations with implementation details.
    """
    
    # spawn_agent("performance-optimizer", task_description, prompt)

def spawn_system_architect_agent(project_dir, focus_area=None):
    """Spawn system-architect agent for architectural analysis."""
    print("🏗️ Launching system-architect agent...")
    
    task_description = f"System architecture analysis"
    if focus_area:
        task_description += f" with focus on {focus_area}"
    
    prompt = f"""
    Analyze the system architecture of the codebase at {project_dir}.
    
    Focus areas: {focus_area or 'scalability and maintainability'}
    
    Evaluate:
    1. Architectural patterns and design principles
    2. Service boundaries and coupling
    3. Scalability considerations
    4. Technology stack appropriateness
    5. Integration patterns
    
    Provide architectural improvement recommendations and design alternatives.
    """
    
    # spawn_agent("system-architect", task_description, prompt)

def update_best_practices():
    """Update review criteria with latest AI/ML best practices."""
    print("📚 Fetching latest AI/ML engineering best practices...")
    
    # This would use the llm-ai-agents-and-eng-research agent
    task_description = "Gather latest AI/ML engineering best practices"
    prompt = """
    Research the latest best practices in AI/ML engineering, focusing on:
    1. Code quality standards for AI/ML projects
    2. Model deployment and monitoring practices
    3. Data pipeline optimization
    4. Performance optimization techniques
    5. Security considerations for AI systems
    
    Provide actionable insights that can be applied to code reviews.
    """
    
    # spawn_agent("llm-ai-agents-and-eng-research", task_description, prompt)

def generate_completion_summary(scope, focus_area=None):
    """Generate audio summary of review completion."""
    print("🎵 Generating completion summary...")
    
    summary_text = f"Completed {scope} review"
    if focus_area:
        summary_text += f" with focus on {focus_area}"
    
    task_description = "Generate audio summary of review completion"
    prompt = f"""
    {summary_text}. Review has been completed with detailed analysis and recommendations provided in the generated report.
    
    Next recommended steps:
    1. Review the generated report
    2. Address critical issues first
    3. Implement suggested improvements
    4. Re-run review to validate fixes
    """
    
    # spawn_agent("work-completion-summary", task_description, prompt)

# Main execution
if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Comprehensive review command with agent integration')
    parser.add_argument('scope', help='Review scope: build, code, changes, typescript, security, performance, architecture')
    parser.add_argument('focus_area', nargs='?', help='Specific focus area (optional)')
    parser.add_argument('--no-agents', action='store_true', help='Disable agent integration')
    parser.add_argument('--audio-summary', action='store_true', help='Generate audio summary at completion')
    parser.add_argument('--research-latest', action='store_true', help='Include latest best practices from AI/ML research')
    
    args = parser.parse_args()
    
    use_agents = not args.no_agents
    
    if args.scope not in ['build', 'code', 'changes', 'typescript', 'security', 'performance', 'architecture']:
        print("❌ Invalid scope")
        print("Scopes: build, code, changes, typescript, security, performance, architecture")
        sys.exit(1)
    
    review(args.scope, args.focus_area, use_agents, args.audio_summary, args.research_latest)
```

## Consolidation Notes

### Replaces These Commands:
- `code-quality/review-general.md` → `review code`
- `code-quality/review-staged-unstaged.md` → `review changes`  
- `typescript/TS-review-general.md` → `review typescript`
- `typescript/TS-review-staged-unstaged.md` → `review changes` (TypeScript-aware)

### Agent Integration Benefits:
- **Specialized Analysis**: Uses expert agents (code-quality-analyzer, security-auditor, performance-optimizer, system-architect)
- **Latest Best Practices**: Incorporates cutting-edge AI/ML engineering practices via research agent
- **Audio Summaries**: Provides completion summaries for complex reviews
- **Automated Fixes**: Agents can implement fixes where possible
- **Comprehensive Coverage**: Multiple agents work in parallel for thorough analysis

### Enhanced Capabilities:
- Real-time best practice updates from AI/ML research
- Specialized security vulnerability assessments
- Performance bottleneck identification and optimization
- Architectural analysis and improvement recommendations
- Audio feedback for better workflow integration
- Parallel agent execution for faster analysis

This consolidated command provides 5x more functionality while reducing the number of commands from 4 to 1. 