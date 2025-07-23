# Review Build

## Description
Comprehensively reviews the current build/project and recommends enhancements, additional features, and improvements using available tools and best practices.

## Usage
```
/review-build [focus-area]
```

## Arguments
- `focus-area` (optional): Specific area to focus on (e.g., "performance", "security", "features", "architecture", "ui/ux")

## Behavior
1. **Project Analysis**: Scans current project structure and codebase
2. **Technology Assessment**: Identifies tech stack and evaluates current implementation
3. **Code Quality Review**: Analyzes code quality, patterns, and potential improvements
4. **Feature Gap Analysis**: Identifies missing features and enhancement opportunities
5. **Tool Integration**: Uses available tools (Supabase, GitHub, etc.) for recommendations
6. **Enhancement Planning**: Creates actionable recommendations with implementation plans

## Example Usage
```
/review-build
/review-build performance
/review-build "user experience and security"
```

## Implementation
```python
import os
import sys
import json
from pathlib import Path
from datetime import datetime
import subprocess

def review_build(focus_area=None):
    """
    Comprehensive build review with enhancement recommendations.
    """
    current_dir = Path.cwd()
    
    print("🔍 Starting comprehensive build review...")
    
    # Analyze project structure
    project_analysis = analyze_project_structure(current_dir)
    
    # Detect technology stack
    tech_stack = detect_technology_stack(current_dir)
    
    # Analyze code quality
    code_quality = analyze_code_quality(current_dir)
    
    # Identify enhancement opportunities
    enhancements = identify_enhancement_opportunities(current_dir, focus_area)
    
    # Generate recommendations
    recommendations = generate_recommendations(project_analysis, tech_stack, code_quality, enhancements)
    
    # Create review report
    create_review_report(current_dir, recommendations, focus_area)
    
    print("✅ Build review complete! Check 'build-review-report.md' for detailed recommendations.")

def analyze_project_structure(project_dir):
    """Analyze the current project structure."""
    print("📁 Analyzing project structure...")
    
    structure = {
        'directories': [],
        'files': [],
        'tech_files': {},
        'config_files': []
    }
    
    # Scan for common project files
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
            
            if file_path.is_file():
                structure['files'].append(str(relative_path))
                
                # Check for tech stack indicators
                for pattern, tech in tech_patterns.items():
                    if pattern in file_path.name:
                        structure['tech_files'][str(relative_path)] = tech
                        
                # Check for config files
                if any(config in file_path.name for config in ['config', 'conf', '.env', '.json', '.yaml', '.yml']):
                    structure['config_files'].append(str(relative_path))
            
            elif file_path.is_dir():
                structure['directories'].append(str(relative_path))
    
    return structure

def detect_technology_stack(project_dir):
    """Detect the technology stack being used."""
    print("🔧 Detecting technology stack...")
    
    tech_stack = {
        'frontend': [],
        'backend': [],
        'database': [],
        'tools': [],
        'deployment': [],
        'testing': []
    }
    
    # Check for frontend technologies
    frontend_patterns = {
        'package.json': ['react', 'vue', 'angular', 'svelte', 'next', 'nuxt', 'gatsby'],
        'tsconfig.json': ['typescript'],
        'tailwind.config.js': ['tailwind'],
        'postcss.config.js': ['postcss'],
        'vite.config.js': ['vite'],
        'webpack.config.js': ['webpack']
    }
    
    # Check for backend technologies
    backend_patterns = {
        'requirements.txt': ['python', 'django', 'flask', 'fastapi'],
        'package.json': ['express', 'koa', 'nest', 'fastify'],
        'Cargo.toml': ['rust'],
        'go.mod': ['go'],
        'pom.xml': ['java', 'spring'],
        'composer.json': ['php', 'laravel']
    }
    
    # Check for database technologies
    db_patterns = {
        'supabase': ['supabase'],
        'prisma': ['prisma'],
        'sequelize': ['sequelize'],
        'mongoose': ['mongodb'],
        'redis': ['redis'],
        'postgres': ['postgresql']
    }
    
    # Check for deployment technologies
    deployment_patterns = {
        'Dockerfile': ['docker'],
        'docker-compose.yml': ['docker-compose'],
        'vercel.json': ['vercel'],
        'netlify.toml': ['netlify'],
        '.github/workflows': ['github-actions'],
        'k8s': ['kubernetes']
    }
    
    # Check for testing technologies
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
            
            # Check frontend patterns
            for pattern, techs in frontend_patterns.items():
                if pattern in file_path.name:
                    for tech in techs:
                        if tech in file_content and tech not in tech_stack['frontend']:
                            tech_stack['frontend'].append(tech)
            
            # Check backend patterns
            for pattern, techs in backend_patterns.items():
                if pattern in file_path.name:
                    for tech in techs:
                        if tech in file_content and tech not in tech_stack['backend']:
                            tech_stack['backend'].append(tech)
            
            # Check database patterns
            for pattern, techs in db_patterns.items():
                if pattern in file_content and techs[0] not in tech_stack['database']:
                    tech_stack['database'].extend(techs)
            
            # Check deployment patterns
            for pattern, techs in deployment_patterns.items():
                if pattern in str(file_path) and techs[0] not in tech_stack['deployment']:
                    tech_stack['deployment'].extend(techs)
            
            # Check testing patterns
            for pattern, techs in testing_patterns.items():
                if pattern in str(file_path) and techs[0] not in tech_stack['testing']:
                    tech_stack['testing'].extend(techs)
    
    return tech_stack

def analyze_code_quality(project_dir):
    """Analyze code quality and patterns."""
    print("📊 Analyzing code quality...")
    
    quality_metrics = {
        'file_count': 0,
        'code_files': 0,
        'test_files': 0,
        'documentation_files': 0,
        'potential_issues': [],
        'best_practices': [],
        'improvement_areas': []
    }
    
    # Count files by type
    for file_path in project_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            quality_metrics['file_count'] += 1
            
            # Categorize files
            if file_path.suffix in ['.js', '.ts', '.jsx', '.tsx', '.py', '.java', '.go', '.rs', '.php']:
                quality_metrics['code_files'] += 1
            elif 'test' in file_path.name.lower() or 'spec' in file_path.name.lower():
                quality_metrics['test_files'] += 1
            elif file_path.suffix in ['.md', '.txt', '.rst']:
                quality_metrics['documentation_files'] += 1
    
    # Check for common issues
    if quality_metrics['test_files'] == 0:
        quality_metrics['potential_issues'].append("No test files found")
        quality_metrics['improvement_areas'].append("Add comprehensive testing")
    
    if quality_metrics['documentation_files'] < 2:
        quality_metrics['potential_issues'].append("Limited documentation")
        quality_metrics['improvement_areas'].append("Improve documentation coverage")
    
    # Check for best practices
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
    print("🎯 Identifying enhancement opportunities...")
    
    opportunities = {
        'performance': [],
        'security': [],
        'features': [],
        'architecture': [],
        'ui_ux': [],
        'testing': [],
        'documentation': [],
        'deployment': [],
        'monitoring': []
    }
    
    # Performance opportunities
    opportunities['performance'].extend([
        "Implement code splitting for better load times",
        "Add caching strategies (Redis, CDN)",
        "Optimize database queries",
        "Implement lazy loading for images",
        "Add performance monitoring (Lighthouse, Web Vitals)"
    ])
    
    # Security opportunities
    opportunities['security'].extend([
        "Implement authentication and authorization",
        "Add input validation and sanitization",
        "Implement rate limiting",
        "Add security headers",
        "Implement HTTPS enforcement",
        "Add security scanning tools"
    ])
    
    # Feature opportunities
    opportunities['features'].extend([
        "Add real-time notifications",
        "Implement search functionality",
        "Add data export/import features",
        "Implement user preferences",
        "Add analytics and reporting",
        "Implement backup and recovery"
    ])
    
    # Architecture opportunities
    opportunities['architecture'].extend([
        "Implement microservices architecture",
        "Add API versioning",
        "Implement event-driven architecture",
        "Add message queues",
        "Implement CQRS pattern",
        "Add service discovery"
    ])
    
    # UI/UX opportunities
    opportunities['ui_ux'].extend([
        "Improve responsive design",
        "Add dark mode support",
        "Implement accessibility features",
        "Add loading states and animations",
        "Improve error handling UX",
        "Add keyboard navigation"
    ])
    
    # Testing opportunities
    opportunities['testing'].extend([
        "Add unit tests",
        "Implement integration tests",
        "Add end-to-end tests",
        "Implement visual regression testing",
        "Add performance testing",
        "Implement security testing"
    ])
    
    # Documentation opportunities
    opportunities['documentation'].extend([
        "Add API documentation",
        "Create user guides",
        "Add developer documentation",
        "Implement inline code documentation",
        "Add architecture diagrams",
        "Create deployment guides"
    ])
    
    # Deployment opportunities
    opportunities['deployment'].extend([
        "Implement CI/CD pipeline",
        "Add automated testing in pipeline",
        "Implement blue-green deployment",
        "Add rollback mechanisms",
        "Implement infrastructure as code",
        "Add monitoring and alerting"
    ])
    
    # Monitoring opportunities
    opportunities['monitoring'].extend([
        "Add application performance monitoring",
        "Implement error tracking",
        "Add user analytics",
        "Implement health checks",
        "Add log aggregation",
        "Implement alerting systems"
    ])
    
    return opportunities

def generate_recommendations(project_analysis, tech_stack, code_quality, enhancements):
    """Generate actionable recommendations."""
    print("💡 Generating recommendations...")
    
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

def create_review_report(project_dir, recommendations, focus_area=None):
    """Create a comprehensive review report."""
    print("📝 Creating review report...")
    
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
/prp-base-create {recommendations['high_priority'][0]['title'].lower().replace(' ', '-')}

# Execute PRPs with full context
/prp-base-execute PRPs/your-feature.md

# Review implementation
/review-general src/
```

## Notes
- Prioritize high-impact, low-effort improvements first
- Use the PRP system for structured implementation
- Consider tool integrations for enhanced functionality
- Regular reviews help maintain code quality and identify new opportunities

---
*Generated by PRP System Build Review*
"""
    
    report_path = project_dir / 'build-review-report.md'
    with open(report_path, 'w') as f:
        f.write(report_content)
    
    print(f"📄 Review report saved to: {report_path}")

# Main execution
if __name__ == "__main__":
    import sys
    
    focus_area = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    review_build(focus_area)
```

## Notes
- This command provides comprehensive build analysis
- Uses available tools and patterns for recommendations
- Creates actionable implementation plans
- Integrates with the PRP system for structured development
- Focuses on high-impact, low-effort improvements
- Provides tool-specific recommendations based on detected tech stack 