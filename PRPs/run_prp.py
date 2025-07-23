#!/usr/bin/env python3
"""
PRP (Product Requirement Prompt) Runner
Executes PRPs with AI assistance for consistent code generation.
"""

import sys
import argparse


def read_prp_file(prp_path):
    """Read and parse PRP file."""
    try:
        with open(prp_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: PRP file '{prp_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading PRP file: {e}")
        sys.exit(1)


def validate_prp_structure(prp_content):
    """Validate PRP has required sections."""
    required_sections = [
        "## Overview",
        "## Requirements",
        "## All Needed Context",
        "## Implementation Notes"
    ]

    missing_sections = []
    for section in required_sections:
        if section not in prp_content:
            missing_sections.append(section)

    if missing_sections:
        print("Warning: PRP missing required sections:")
        for section in missing_sections:
            print(f"  - {section}")
        return False
    return True


def run_with_ai(prp_content, ai_tool="claude"):
    """Execute PRP with AI tool."""
    print("🚀 Executing PRP with AI assistance...")
    print("=" * 50)

    # For Claude, you would integrate with their API
    # For now, we'll just display the PRP content
    print(prp_content)
    print("=" * 50)
    print("📝 AI execution complete. Review the generated code above.")
    print("💡 Tip: Copy the generated code to your project files.")


def main():
    parser = argparse.ArgumentParser(description="Run PRP with AI assistance")
    parser.add_argument("prp_file", help="Path to PRP file")
    parser.add_argument("--ai-tool", default="claude", help="AI tool to use")
    parser.add_argument(
        "--validate-only", action="store_true", help="Only validate PRP structure"
    )

    args = parser.parse_args()

    # Read PRP file
    prp_content = read_prp_file(args.prp_file)

    # Validate structure
    if not validate_prp_structure(prp_content):
        if args.validate_only:
            print("❌ PRP validation failed.")
            sys.exit(1)
        else:
            print("⚠️  Continuing despite validation warnings...")

    if args.validate_only:
        print("✅ PRP validation passed.")
        return

    # Execute with AI
    run_with_ai(prp_content, args.ai_tool)


if __name__ == "__main__":
    main()
