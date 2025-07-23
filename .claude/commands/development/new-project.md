# New Project

## Description
Creates a new project from scratch with a `claude.md` file and `initial.md` file based on user input describing what they want the project to do.

## Usage
```
/new-project [project-description]
```

## Arguments
- `project-description` (optional): Description of what you want the project to do

## Behavior
1. **Project Validation**: Ensures we're starting fresh (no existing project files)
2. **User Input Collection**: Prompts for project description if not provided
3. **CLAUDE.md Creation**: Creates a comprehensive `claude.md` file for the new project
4. **INITIAL.md Creation**: Creates an `initial.md` file with project initialization details
5. **PRP System Setup**: Sets up the PRP system for the new project
6. **Project Structure**: Creates basic project structure and documentation

## Example Usage
```
/new-project "A web application for task management with user authentication"
```

## Implementation
```python
import os
import sys
from pathlib import Path
from datetime import datetime

def create_new_project(project_description=None):
    """
    Create a new project from scratch with PRP system setup.
    """
    current_dir = Path.cwd()
    
    # Check if directory is empty or has minimal content
    existing_files = [f for f in current_dir.iterdir() if f.name not in ['.git', '.gitignore']]
    if existing_files:
        print("⚠️  Directory contains files. Consider using /analyze-project for existing projects.")
        response = input("Continue with new project setup? (y/N): ")
        if response.lower() != 'y':
            print("❌ New project setup cancelled.")
            return
    
    # Get project description if not provided
    if not project_description:
        print("🎯 Let's create a new project!")
        print("Please describe what you want your project to do:")
        project_description = input("Project description: ").strip()
        
        if not project_description:
            print("❌ Project description is required.")
            return
    
    print(f"🚀 Creating new project: {project_description}")
    
    # Create claude.md
    create_claude_md_for_new_project(current_dir, project_description)
    
    # Create initial.md
    create_initial_md_for_new_project(current_dir, project_description)
    
    # Set up PRP system
    setup_prp_system_for_new_project(current_dir, project_description)
    
    # Create basic project structure
    create_basic_project_structure(current_dir, project_description)
    
    print("✅ New project created successfully!")
    print("📁 Next steps:")
    print("   1. Review claude.md for project guidelines")
    print("   2. Check initial.md for project initialization")
    print("   3. Use /prp to create your first feature requirement")
    print("   4. Start building your project!")

def create_claude_md_for_new_project(project_dir, description):
    """Create a comprehensive claude.md file for a new project."""
    content = f"""# Project Development Guide

## Project Overview
**Project Goal:** {description}

## Project Context
- **Project Type:** New Development
- **Start Date:** {datetime.now().strftime('%Y-%m-%d')}
- **Development Approach:** PRP (Product Requirement Prompt) System

## Development Philosophy
This project follows a structured development approach using the PRP system:

### Core Principles
1. **Requirement-Driven Development**: Every feature starts with a clear PRP
2. **Incremental Building**: Build features one at a time with clear success criteria
3. **Documentation-First**: Maintain clear documentation throughout development
4. **Quality Assurance**: Test each feature before moving to the next

### PRP System Workflow
1. **Create PRP**: Use `/prp` to define a new feature requirement
2. **Plan Implementation**: Use `/plan` to create development plans
3. **Build Feature**: Implement the feature according to the PRP
4. **Validate**: Ensure the feature meets all success criteria
5. **Document**: Update documentation and create next PRP

## Project Structure
```
{project_dir.name}/
├── claude.md          # This file - project guidelines
├── initial.md         # Project initialization details
├── README.md          # Project overview and setup
├── PRPs/              # Product Requirement Prompts
│   ├── templates/     # PRP templates
│   ├── examples/      # Example PRPs
│   └── ai_docs/       # AI documentation
├── src/               # Source code
├── docs/              # Documentation
├── tests/             # Test files
└── scripts/           # Utility scripts
```

## Technology Stack
**To be determined based on project requirements**

## Development Guidelines
1. **Code Quality**: Write clean, maintainable code
2. **Testing**: Include tests for all features
3. **Documentation**: Keep documentation up to date
4. **Version Control**: Use meaningful commit messages
5. **Incremental Development**: Build and test features incrementally

## Available Commands
- `/prp` - Create a new Product Requirement Prompt
- `/plan` - Create development plans
- `/analyze` - Analyze code or requirements
- `/test` - Run tests and validation
- `/docs` - Generate or update documentation

## Success Metrics
- [ ] Project requirements clearly defined
- [ ] Core features implemented
- [ ] Documentation complete
- [ ] Tests passing
- [ ] Ready for deployment

## Next Steps
1. Review and refine project requirements
2. Create first PRP for core functionality
3. Set up development environment
4. Begin implementation
"""
    
    with open(project_dir / "claude.md", 'w') as f:
        f.write(content)
    print("✅ Created comprehensive claude.md")

def create_initial_md_for_new_project(project_dir, description):
    """Create initial.md for new project setup."""
    content = f"""# Project Initialization

## Project Description
**Goal:** {description}

## Initial Requirements Gathering
Before starting development, we need to gather more specific requirements:

### Functional Requirements
1. **Core Features:**
   - [ ] [Define core feature 1]
   - [ ] [Define core feature 2]
   - [ ] [Define core feature 3]

2. **User Stories:**
   - As a [user type], I want [feature] so that [benefit]
   - As a [user type], I want [feature] so that [benefit]

### Technical Requirements
1. **Technology Stack:**
   - Frontend: [To be determined]
   - Backend: [To be determined]
   - Database: [To be determined]
   - Hosting: [To be determined]

2. **Performance Requirements:**
   - [ ] [Performance requirement 1]
   - [ ] [Performance requirement 2]

3. **Security Requirements:**
   - [ ] [Security requirement 1]
   - [ ] [Security requirement 2]

### Non-Functional Requirements
1. **Usability:**
   - [ ] [Usability requirement 1]
   - [ ] [Usability requirement 2]

2. **Scalability:**
   - [ ] [Scalability requirement 1]
   - [ ] [Scalability requirement 2]

## Project Scope
- **MVP Features:** [List minimum viable product features]
- **Future Enhancements:** [List future features]
- **Out of Scope:** [List what's not included]

## Timeline
- **Phase 1:** [Define phase 1 goals and timeline]
- **Phase 2:** [Define phase 2 goals and timeline]
- **Phase 3:** [Define phase 3 goals and timeline]

## Resources Needed
- **Development Tools:** [List required tools]
- **External Services:** [List external services]
- **Team Skills:** [List required skills]

## Risk Assessment
- **Technical Risks:** [List potential technical challenges]
- **Timeline Risks:** [List potential timeline issues]
- **Resource Risks:** [List potential resource constraints]

## Success Criteria
- [ ] [Success criterion 1]
- [ ] [Success criterion 2]
- [ ] [Success criterion 3]

## Next Actions
1. **Refine Requirements:** Complete the requirements gathering above
2. **Create First PRP:** Use `/prp` to create the first feature requirement
3. **Set Up Environment:** Configure development environment
4. **Begin Development:** Start with MVP features
"""
    
    with open(project_dir / "initial.md", 'w') as f:
        f.write(content)
    print("✅ Created detailed initial.md")

def setup_prp_system_for_new_project(project_dir, description):
    """Set up PRP system for new project."""
    # Create PRPs directory structure
    prps_dir = project_dir / "PRPs"
    prps_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    (prps_dir / "templates").mkdir(exist_ok=True)
    (prps_dir / "examples").mkdir(exist_ok=True)
    (prps_dir / "ai_docs").mkdir(exist_ok=True)
    
    # Create new project PRP template
    template_content = """# New Project PRP Template

## Feature Request
**Description:** [Describe the feature to be built]

## User Story
As a [user type], I want [feature] so that [benefit]

## Requirements
### Functional Requirements
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

### Technical Requirements
- [ ] [Technical requirement 1]
- [ ] [Technical requirement 2]

### UI/UX Requirements
- [ ] [UI requirement 1]
- [ ] [UX requirement 2]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Technical Design
### Architecture
[Describe the technical architecture for this feature]

### Data Models
[Describe any new data models or changes to existing ones]

### API Endpoints
[Describe any new API endpoints needed]

### Database Changes
[Describe any database schema changes]

## Implementation Plan
1. **Step 1:** [Implementation step 1]
2. **Step 2:** [Implementation step 2]
3. **Step 3:** [Implementation step 3]

## Testing Strategy
- **Unit Tests:** [What to unit test]
- **Integration Tests:** [What to integration test]
- **User Acceptance Tests:** [What to UAT]

## Dependencies
- [ ] [Dependency 1]
- [ ] [Dependency 2]

## Success Metrics
- [ ] [Metric 1]
- [ ] [Metric 2]

## Notes
[Any additional notes or considerations]
"""
    
    template_path = prps_dir / "templates" / "new_project_template.md"
    with open(template_path, 'w') as f:
        f.write(template_content)
    
    # Create example PRP
    example_content = f"""# Example PRP: Project Setup

## Feature Request
**Description:** Set up the basic project structure and development environment

## User Story
As a developer, I want a well-organized project structure so that I can efficiently build the {description}

## Requirements
### Functional Requirements
- [ ] Create basic project directory structure
- [ ] Set up version control
- [ ] Configure development environment
- [ ] Create initial documentation

### Technical Requirements
- [ ] Choose appropriate technology stack
- [ ] Set up build/deployment pipeline
- [ ] Configure linting and formatting
- [ ] Set up testing framework

### UI/UX Requirements
- [ ] Design basic UI wireframes
- [ ] Define color scheme and typography
- [ ] Plan user flow

## Acceptance Criteria
- [ ] Project structure is organized and scalable
- [ ] Development environment is ready for coding
- [ ] Basic documentation is in place
- [ ] Technology stack is chosen and configured

## Technical Design
### Architecture
Basic project architecture with clear separation of concerns

### Data Models
Initial data models based on core features

### API Endpoints
Basic API structure for core functionality

### Database Changes
Initial database schema design

## Implementation Plan
1. **Step 1:** Research and choose technology stack
2. **Step 2:** Set up project structure
3. **Step 3:** Configure development tools
4. **Step 4:** Create initial documentation

## Testing Strategy
- **Unit Tests:** Basic test setup
- **Integration Tests:** Core functionality tests
- **User Acceptance Tests:** Basic user flow tests

## Dependencies
- [ ] Technology stack selection
- [ ] Development tools installation
- [ ] Documentation templates

## Success Metrics
- [ ] Project builds successfully
- [ ] Tests pass
- [ ] Documentation is clear and complete

## Notes
This is the foundational PRP for the project. All subsequent features will build upon this setup.
"""
    
    example_path = prps_dir / "examples" / "project_setup_example.md"
    with open(example_path, 'w') as f:
        f.write(example_content)
    
    print("✅ Set up PRP system for new project")

def create_basic_project_structure(project_dir, description):
    """Create basic project structure."""
    # Create main directories
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "docs").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / "scripts").mkdir(exist_ok=True)
    
    # Create README.md
    readme_content = f"""# {project_dir.name}

## Project Description
{description}

## Getting Started
This project uses the PRP (Product Requirement Prompt) system for structured development.

### Prerequisites
- [List prerequisites]

### Installation
1. Clone the repository
2. Install dependencies
3. Set up environment variables
4. Run the application

### Development
- Use `/prp` to create new feature requirements
- Use `/plan` to create development plans
- Use `/analyze` to analyze code or requirements

## Project Structure
- `claude.md` - Project development guidelines
- `initial.md` - Project initialization details
- `PRPs/` - Product Requirement Prompts
- `src/` - Source code
- `docs/` - Documentation
- `tests/` - Test files
- `scripts/` - Utility scripts

## Contributing
Follow the PRP system for all feature development.

## License
[Add license information]
"""
    
    with open(project_dir / "README.md", 'w') as f:
        f.write(readme_content)
    
    # Create .gitignore
    gitignore_content = """# Dependencies
node_modules/
venv/
__pycache__/

# Build outputs
dist/
build/
*.pyc

# Environment variables
.env
.env.local

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log

# Temporary files
*.tmp
*.temp
"""
    
    with open(project_dir / ".gitignore", 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Created basic project structure")

# Main execution
if __name__ == "__main__":
    import sys
    
    project_description = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    create_new_project(project_description)
```

## Notes
- This command is designed for starting completely new projects
- It creates a comprehensive project foundation
- Includes detailed templates for new project development
- Sets up the PRP system for structured development
- Provides clear next steps for project initiation 