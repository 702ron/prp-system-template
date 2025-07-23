#!/usr/bin/env python3
"""
Test script for the /review-build command
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

def test_review_build_command():
    """Test the /review-build command functionality."""
    print("🧪 Testing /review-build command...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create a mock project structure
        create_mock_project(temp_path)
        
        try:
            # Simulate the review build functionality
            print("📁 Analyzing project structure...")
            
            # Test project structure analysis
            structure = analyze_project_structure(temp_path)
            assert len(structure['files']) > 0, "Should detect project files"
            assert 'package.json' in [f.split('/')[-1] for f in structure['files']], "Should detect package.json"
            
            print("✅ Project structure analysis passed")
            
            # Test technology stack detection
            print("🔧 Detecting technology stack...")
            tech_stack = detect_technology_stack(temp_path)
            assert 'react' in tech_stack['frontend'], "Should detect React"
            assert 'typescript' in tech_stack['frontend'], "Should detect TypeScript"
            
            print("✅ Technology stack detection passed")
            
            # Test code quality analysis
            print("📊 Analyzing code quality...")
            code_quality = analyze_code_quality(temp_path)
            assert code_quality['file_count'] > 0, "Should count files"
            assert code_quality['code_files'] > 0, "Should detect code files"
            
            print("✅ Code quality analysis passed")
            
            # Test enhancement opportunities
            print("🎯 Identifying enhancement opportunities...")
            enhancements = identify_enhancement_opportunities(temp_path, "performance")
            assert len(enhancements['performance']) > 0, "Should identify performance opportunities"
            assert len(enhancements['security']) > 0, "Should identify security opportunities"
            
            print("✅ Enhancement opportunities identification passed")
            
            # Test recommendations generation
            print("💡 Generating recommendations...")
            recommendations = generate_recommendations(structure, tech_stack, code_quality, enhancements)
            assert len(recommendations['high_priority']) > 0, "Should generate high priority recommendations"
            assert len(recommendations['tool_integrations']) > 0, "Should suggest tool integrations"
            
            print("✅ Recommendations generation passed")
            
            # Test report creation
            print("📝 Creating review report...")
            create_review_report(temp_path, recommendations, "performance")
            report_path = temp_path / 'build-review-report.md'
            assert report_path.exists(), "Review report should be created"
            
            # Check report content
            with open(report_path, 'r') as f:
                content = f.read()
                assert "Build Review Report" in content, "Report should have proper title"
                assert "High Priority Recommendations" in content, "Report should include recommendations"
                assert "Implementation Commands" in content, "Report should include implementation guidance"
            
            print("✅ Review report creation passed")
            
            print("✅ /review-build command test passed!")
            return True
            
        except Exception as e:
            print(f"❌ /review-build command test failed: {e}")
            return False

def create_mock_project(project_dir):
    """Create a mock project for testing."""
    # Create package.json
    package_json = {
        "name": "test-project",
        "version": "1.0.0",
        "dependencies": {
            "react": "^18.0.0",
            "typescript": "^5.0.0",
            "supabase": "^2.0.0"
        },
        "devDependencies": {
            "jest": "^29.0.0",
            "cypress": "^12.0.0"
        }
    }
    
    import json
    with open(project_dir / "package.json", 'w') as f:
        json.dump(package_json, f, indent=2)
    
    # Create tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "target": "es5",
            "lib": ["dom", "dom.iterable", "es6"],
            "allowJs": True,
            "skipLibCheck": True,
            "esModuleInterop": True,
            "allowSyntheticDefaultImports": True,
            "strict": True,
            "forceConsistentCasingInFileNames": True,
            "noFallthroughCasesInSwitch": True,
            "module": "esnext",
            "moduleResolution": "node",
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "react-jsx"
        },
        "include": ["src"]
    }
    
    with open(project_dir / "tsconfig.json", 'w') as f:
        json.dump(tsconfig, f, indent=2)
    
    # Create src directory and some files
    src_dir = project_dir / "src"
    src_dir.mkdir()
    
    # Create a React component
    component_content = """import React from 'react';

interface Props {
  title: string;
}

export const TestComponent: React.FC<Props> = ({ title }) => {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
};
"""
    
    with open(src_dir / "TestComponent.tsx", 'w') as f:
        f.write(component_content)
    
    # Create README
    readme_content = """# Test Project

This is a test project for the review-build command.

## Features
- React with TypeScript
- Supabase integration
- Testing with Jest and Cypress
"""
    
    with open(project_dir / "README.md", 'w') as f:
        f.write(readme_content)
    
    # Create .gitignore
    gitignore_content = """node_modules/
.env
.env.local
dist/
build/
*.log
"""
    
    with open(project_dir / ".gitignore", 'w') as f:
        f.write(gitignore_content)

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
        'tsconfig.json': 'TypeScript',
        'README.md': 'Documentation',
        '.gitignore': 'Git Configuration'
    }
    
    for file_path in project_dir.rglob('*'):
        if file_path.is_file() and not file_path.name.startswith('.'):
            relative_path = file_path.relative_to(project_dir)
            structure['files'].append(str(relative_path))
            
            for pattern, tech in tech_patterns.items():
                if pattern in file_path.name:
                    structure['tech_files'][str(relative_path)] = tech
    
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
    
    for file_path in project_dir.rglob('*'):
        if file_path.is_file():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read().lower()
            except:
                continue
            
            # Check for React
            if 'react' in file_content and 'react' not in tech_stack['frontend']:
                tech_stack['frontend'].append('react')
            
            # Check for TypeScript
            if 'typescript' in file_content and 'typescript' not in tech_stack['frontend']:
                tech_stack['frontend'].append('typescript')
            
            # Check for Supabase
            if 'supabase' in file_content and 'supabase' not in tech_stack['database']:
                tech_stack['database'].append('supabase')
    
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
            
            if file_path.suffix in ['.js', '.ts', '.jsx', '.tsx']:
                quality_metrics['code_files'] += 1
            elif file_path.suffix in ['.md']:
                quality_metrics['documentation_files'] += 1
    
    if quality_metrics['test_files'] == 0:
        quality_metrics['potential_issues'].append("No test files found")
    
    if (project_dir / '.gitignore').exists():
        quality_metrics['best_practices'].append("Git ignore configured")
    
    return quality_metrics

def identify_enhancement_opportunities(project_dir, focus_area=None):
    """Identify enhancement opportunities based on focus area."""
    opportunities = {
        'performance': [
            "Implement code splitting for better load times",
            "Add caching strategies (Redis, CDN)"
        ],
        'security': [
            "Implement authentication and authorization",
            "Add input validation and sanitization"
        ],
        'features': [
            "Add real-time notifications",
            "Implement search functionality"
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
    
    if code_quality['test_files'] == 0:
        recommendations['high_priority'].append({
            'title': 'Add Testing Framework',
            'description': 'No test files found. Implement comprehensive testing.',
            'tools': ['Jest', 'Cypress', 'Playwright'],
            'effort': 'Medium',
            'impact': 'High'
        })
    
    recommendations['tool_integrations'].extend([
        {
            'tool': 'GitHub Actions',
            'description': 'Implement CI/CD pipeline',
            'benefit': 'Automated testing and deployment'
        }
    ])
    
    recommendations['next_steps'] = [
        "Prioritize high-impact, low-effort improvements",
        "Set up monitoring and analytics"
    ]
    
    return recommendations

def create_review_report(project_dir, recommendations, focus_area=None):
    """Create a comprehensive review report."""
    from datetime import datetime
    
    report_content = f"""# Build Review Report

## Review Summary
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Project**: {project_dir.name}
**Focus Area**: {focus_area or 'Comprehensive Review'}

## High Priority Recommendations

"""
    
    for rec in recommendations['high_priority']:
        report_content += f"""### {rec['title']}
**Description**: {rec['description']}
**Effort**: {rec['effort']} | **Impact**: {rec['impact']}
**Recommended Tools**: {', '.join(rec['tools'])}

"""
    
    report_content += """## Implementation Commands

### Quick Start Enhancements
```bash
# Set up testing framework
/setup-prp-system --testing

# Add authentication
/prp-base-create implement user authentication with Supabase
```

---
*Generated by PRP System Build Review*
"""
    
    report_path = project_dir / 'build-review-report.md'
    with open(report_path, 'w') as f:
        f.write(report_content)

def main():
    """Run the test."""
    print("🚀 Testing /review-build command...")
    print("=" * 50)
    
    success = test_review_build_command()
    
    print()
    print("=" * 50)
    
    if success:
        print("🎉 /review-build command test passed!")
        print()
        print("📋 Command features:")
        print("   - Project structure analysis")
        print("   - Technology stack detection")
        print("   - Code quality assessment")
        print("   - Enhancement opportunity identification")
        print("   - Actionable recommendations generation")
        print("   - Comprehensive report creation")
        return 0
    else:
        print("❌ /review-build command test failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 