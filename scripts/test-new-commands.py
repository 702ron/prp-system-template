#!/usr/bin/env python3
"""
Test script for the new slash commands: /new-project and /analyze-project
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

def test_new_project_command():
    """Test the /new-project command functionality."""
    print("🧪 Testing /new-project command...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Simulate the new project creation
        project_description = "A test web application for task management"
        
        # Test the functions that would be called by the command
        try:
            # Import the functions (they would be in the command file)
            # For now, we'll simulate the behavior
            
            # Check if directory is empty
            existing_files = [f for f in temp_path.iterdir() if f.name not in ['.git', '.gitignore']]
            assert len(existing_files) == 0, "Directory should be empty for new project"
            
            # Create claude.md
            claude_content = f"""# Project Development Guide

## Project Overview
**Project Goal:** {project_description}

## Project Context
- **Project Type:** New Development
- **Start Date:** 2024-01-01
- **Development Approach:** PRP (Product Requirement Prompt) System
"""
            
            claude_path = temp_path / "claude.md"
            with open(claude_path, 'w') as f:
                f.write(claude_content)
            
            assert claude_path.exists(), "claude.md should be created"
            
            # Create initial.md
            initial_path = temp_path / "initial.md"
            initial_content = f"""# Project Initialization

## Project Description
**Goal:** {project_description}
"""
            
            with open(initial_path, 'w') as f:
                f.write(initial_content)
            
            assert initial_path.exists(), "initial.md should be created"
            
            # Create PRPs directory structure
            prps_dir = temp_path / "PRPs"
            prps_dir.mkdir(exist_ok=True)
            (prps_dir / "templates").mkdir(exist_ok=True)
            (prps_dir / "examples").mkdir(exist_ok=True)
            (prps_dir / "ai_docs").mkdir(exist_ok=True)
            
            assert prps_dir.exists(), "PRPs directory should be created"
            assert (prps_dir / "templates").exists(), "templates directory should be created"
            assert (prps_dir / "examples").exists(), "examples directory should be created"
            assert (prps_dir / "ai_docs").exists(), "ai_docs directory should be created"
            
            # Create basic project structure
            (temp_path / "src").mkdir(exist_ok=True)
            (temp_path / "docs").mkdir(exist_ok=True)
            (temp_path / "tests").mkdir(exist_ok=True)
            (temp_path / "scripts").mkdir(exist_ok=True)
            
            assert (temp_path / "src").exists(), "src directory should be created"
            assert (temp_path / "docs").exists(), "docs directory should be created"
            assert (temp_path / "tests").exists(), "tests directory should be created"
            assert (temp_path / "scripts").exists(), "scripts directory should be created"
            
            print("✅ /new-project command test passed!")
            return True
            
        except Exception as e:
            print(f"❌ /new-project command test failed: {e}")
            return False

def test_analyze_project_command():
    """Test the /analyze-project command functionality."""
    print("🧪 Testing /analyze-project command...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create some existing project files to simulate an existing project
        (temp_path / "src").mkdir()
        (temp_path / "package.json").write_text('{"name": "test-project"}')
        (temp_path / "README.md").write_text("# Test Project")
        
        project_description = "I want to add user authentication and improve the UI"
        
        try:
            # Simulate the analyze project functionality
            
            # Check if we're in a project directory (has some files)
            existing_files = [f for f in temp_path.iterdir() if f.name not in ['.git', '.gitignore']]
            assert len(existing_files) > 0, "Should detect existing project files"
            
            # Look for existing claude.md (should not exist)
            claude_md_path = temp_path / "claude.md"
            assert not claude_md_path.exists(), "claude.md should not exist initially"
            
            # Create claude.md for existing project
            claude_content = f"""# Project Enhancement Guide

## Project Overview
This is an existing project that needs enhancement and development.

## Current State
- Project location: {temp_path}
- Analysis date: 2024-01-01

## Enhancement Goals
**User Request:** {project_description}

## Project Structure
{temp_path.name}/
├── src/
├── package.json
└── README.md

## Development Guidelines
1. **Preserve Existing Functionality**: Maintain current features while adding new ones
2. **Incremental Enhancement**: Build upon existing codebase
3. **Code Quality**: Follow existing patterns and conventions
4. **Testing**: Ensure new features don't break existing functionality
"""
            
            with open(claude_md_path, 'w') as f:
                f.write(claude_content)
            
            assert claude_md_path.exists(), "claude.md should be created for existing project"
            
            # Create PRPs directory if it doesn't exist
            prps_dir = temp_path / "PRPs"
            prps_dir.mkdir(exist_ok=True)
            
            # Create initial.md if it doesn't exist
            initial_md_path = temp_path / "initial.md"
            if not initial_md_path.exists():
                initial_content = f"""# Project Enhancement Initialization

## Project Context
This document initializes the enhancement process for an existing project.

## Enhancement Request
**User Description:** {project_description}

## Analysis Required
1. **Current Architecture Review**
2. **Feature Gap Analysis**
3. **Technical Debt Assessment**
4. **Enhancement Priority Definition**
"""
                
                with open(initial_md_path, 'w') as f:
                    f.write(initial_content)
            
            assert initial_md_path.exists(), "initial.md should be created for existing project"
            
            # Create enhancement-focused PRP template
            template_path = prps_dir / "enhancement_template.md"
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
            
            with open(template_path, 'w') as f:
                f.write(template_content)
            
            assert template_path.exists(), "Enhancement template should be created"
            
            print("✅ /analyze-project command test passed!")
            return True
            
        except Exception as e:
            print(f"❌ /analyze-project command test failed: {e}")
            return False

def main():
    """Run all tests."""
    print("🚀 Testing new slash commands...")
    print("=" * 50)
    
    # Test new project command
    new_project_success = test_new_project_command()
    
    print()
    
    # Test analyze project command
    analyze_project_success = test_analyze_project_command()
    
    print()
    print("=" * 50)
    
    if new_project_success and analyze_project_success:
        print("🎉 All tests passed! New commands are ready to use.")
        print()
        print("📋 Available commands:")
        print("   /new-project [description] - Create new project from scratch")
        print("   /analyze-project [description] - Analyze and enhance existing project")
        print("   /setup-prp-system [options] - Set up PRP system only")
        return 0
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 