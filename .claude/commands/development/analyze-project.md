# Analyze Project

## Description
Analyzes an existing project, looks for or creates a `claude.md` file, and helps set up the PRP system for project enhancement and development.

## Usage
```
/analyze-project [project-description]
```

## Arguments
- `project-description` (optional): Brief description of what you want to accomplish with the project

## Behavior
1. **Project Analysis**: Scans the current project structure and identifies existing files
2. **CLAUDE.md Check**: Looks for an existing `claude.md` file
3. **CLAUDE.md Creation**: If no `claude.md` exists, creates one with project context
4. **PRP System Setup**: Sets up the PRP system for the existing project
5. **User Input Integration**: Incorporates any provided project description into the setup

## Example Usage
```
/analyze-project "I want to add user authentication and improve the UI"
```

## Implementation
```python
import os
import sys
from pathlib import Path

def analyze_existing_project(project_description=None):
    """
    Analyze an existing project and set up PRP system for enhancement.
    """
    current_dir = Path.cwd()
    
    # Check if we're in a project directory
    if not (current_dir / ".git").exists() and not any(current_dir.glob("*.md")):
        print("❌ No existing project detected. Use /new-project for starting from scratch.")
        return
    
    print("🔍 Analyzing existing project...")
    
    # Look for existing claude.md
    claude_md_path = current_dir / "claude.md"
    if claude_md_path.exists():
        print("✅ Found existing claude.md")
        with open(claude_md_path, 'r') as f:
            existing_content = f.read()
        print(f"📄 Current claude.md content:\n{existing_content[:500]}...")
    else:
        print("📝 Creating new claude.md for existing project...")
        create_claude_md_for_existing_project(current_dir, project_description)
    
    # Set up PRP system
    setup_prp_system_for_existing_project(current_dir, project_description)
    
    print("✅ Project analysis complete! Ready for enhancement.")

def create_claude_md_for_existing_project(project_dir, description=None):
    """Create a claude.md file for an existing project."""
    content = f"""# Project Enhancement Guide

## Project Overview
This is an existing project that needs enhancement and development.

## Current State
- Project location: {project_dir}
- Analysis date: {datetime.now().strftime('%Y-%m-%d')}

## Enhancement Goals
{f"**User Request:** {description}" if description else "**To be defined by user**"}

## Project Structure
{generate_project_structure(project_dir)}

## Development Guidelines
1. **Preserve Existing Functionality**: Maintain current features while adding new ones
2. **Incremental Enhancement**: Build upon existing codebase
3. **Code Quality**: Follow existing patterns and conventions
4. **Testing**: Ensure new features don't break existing functionality

## PRP System Integration
This project uses the PRP (Product Requirement Prompt) system for structured development:
- Use `/prp` to create new feature requirements
- Use `/analyze` to analyze specific components
- Use `/plan` to create development plans

## Next Steps
1. Review the current project structure
2. Define specific enhancement requirements
3. Create PRPs for new features
4. Implement enhancements incrementally
"""
    
    with open(project_dir / "claude.md", 'w') as f:
        f.write(content)
    print("✅ Created claude.md for existing project")

def setup_prp_system_for_existing_project(project_dir, description=None):
    """Set up PRP system for existing project."""
    # Create PRPs directory if it doesn't exist
    prps_dir = project_dir / "PRPs"
    prps_dir.mkdir(exist_ok=True)
    
    # Create initial.md if it doesn't exist
    initial_md_path = project_dir / "initial.md"
    if not initial_md_path.exists():
        create_initial_md_for_existing_project(project_dir, description)
    
    # Set up PRP templates and runner
    setup_prp_infrastructure(project_dir)
    
    print("✅ PRP system configured for existing project")

def create_initial_md_for_existing_project(project_dir, description=None):
    """Create initial.md for existing project enhancement."""
    content = f"""# Project Enhancement Initialization

## Project Context
This document initializes the enhancement process for an existing project.

## Enhancement Request
{f"**User Description:** {description}" if description else "**To be defined**"}

## Analysis Required
1. **Current Architecture Review**
2. **Feature Gap Analysis**
3. **Technical Debt Assessment**
4. **Enhancement Priority Definition**

## Initial Questions
1. What specific features need to be added or improved?
2. Are there any performance or usability issues to address?
3. What is the timeline for these enhancements?
4. Are there any constraints or requirements to consider?

## Next Actions
1. Create detailed PRPs for each enhancement
2. Analyze existing codebase for integration points
3. Plan implementation strategy
4. Begin incremental development
"""
    
    with open(project_dir / "initial.md", 'w') as f:
        f.write(content)
    print("✅ Created initial.md for project enhancement")

def generate_project_structure(project_dir, max_depth=3):
    """Generate a readable project structure."""
    structure = []
    
    def scan_directory(path, depth=0, prefix=""):
        if depth > max_depth:
            return
        
        items = sorted([item for item in path.iterdir() if item.name not in ['.git', '__pycache__', 'node_modules']])
        
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            next_prefix = "    " if is_last else "│   "
            
            if item.is_dir():
                structure.append(f"{prefix}{current_prefix}{item.name}/")
                scan_directory(item, depth + 1, prefix + next_prefix)
            else:
                structure.append(f"{prefix}{current_prefix}{item.name}")
    
    scan_directory(project_dir)
    return "\n".join(structure)

def setup_prp_infrastructure(project_dir):
    """Set up PRP infrastructure for existing project."""
    # This would integrate with the existing PRP system setup
    # For now, we'll create basic structure
    prps_dir = project_dir / "PRPs"
    
    # Create basic PRP template
    template_content = """# PRP Template for Existing Project

## Feature Enhancement Request
**Description:** [Describe the enhancement needed]

## Current State Analysis
- **Existing Components:** [List relevant existing components]
- **Integration Points:** [Where this enhancement connects to existing code]
- **Dependencies:** [What existing features this depends on]

## Enhancement Requirements
1. **Functional Requirements:**
   - [Requirement 1]
   - [Requirement 2]

2. **Technical Requirements:**
   - [Technical requirement 1]
   - [Technical requirement 2]

3. **Integration Requirements:**
   - [How it integrates with existing features]
   - [Backward compatibility needs]

## Success Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Implementation Notes
[Any specific implementation considerations for existing codebase]
"""
    
    template_path = prps_dir / "enhancement_template.md"
    with open(template_path, 'w') as f:
        f.write(template_content)
    
    print("✅ Created enhancement-focused PRP template")

# Main execution
if __name__ == "__main__":
    import sys
    from datetime import datetime
    
    project_description = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    analyze_existing_project(project_description)
```

## Notes
- This command is designed for existing projects that need enhancement
- It preserves existing project structure and functionality
- Creates enhancement-focused PRP templates
- Integrates with existing codebase patterns 