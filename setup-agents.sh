#!/bin/bash

# setup-agents.sh - Install Claude Code agents to user-level directory
# Part of PRP System Template

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_AGENTS_DIR="$SCRIPT_DIR/.claude/agents"
USER_AGENTS_DIR="$HOME/.claude/agents"

print_info "Setting up Claude Code agents..."

# Check if project agents directory exists
if [ ! -d "$PROJECT_AGENTS_DIR" ]; then
    print_error "Project agents directory not found: $PROJECT_AGENTS_DIR"
    exit 1
fi

# Create user agents directory if it doesn't exist
if [ ! -d "$USER_AGENTS_DIR" ]; then
    print_info "Creating user agents directory: $USER_AGENTS_DIR"
    mkdir -p "$USER_AGENTS_DIR"
fi

# Function to copy agents
copy_agents() {
    local force_copy=false
    
    if [ "$1" = "--force" ] || [ "$1" = "-f" ]; then
        force_copy=true
        print_warning "Force mode enabled - will overwrite existing agents"
    fi
    
    print_info "Copying agents from project to user directory..."
    
    # Count agents to be copied
    agent_count=$(find "$PROJECT_AGENTS_DIR" -name "*.md" -not -name "README.md" | wc -l)
    print_info "Found $agent_count agent(s) to install"
    
    # Copy each agent file
    for agent_file in "$PROJECT_AGENTS_DIR"/*.md; do
        if [ "$(basename "$agent_file")" = "README.md" ]; then
            continue
        fi
        
        agent_name=$(basename "$agent_file")
        target_file="$USER_AGENTS_DIR/$agent_name"
        
        if [ -f "$target_file" ] && [ "$force_copy" = false ]; then
            print_warning "Agent already exists: $agent_name (use --force to overwrite)"
            continue
        fi
        
        cp "$agent_file" "$target_file"
        print_success "Installed agent: $agent_name"
    done
    
    # Copy README if it doesn't exist
    if [ -f "$PROJECT_AGENTS_DIR/README.md" ] && [ ! -f "$USER_AGENTS_DIR/README.md" ]; then
        cp "$PROJECT_AGENTS_DIR/README.md" "$USER_AGENTS_DIR/README.md"
        print_success "Installed agents README"
    fi
}

# Function to list available agents
list_agents() {
    print_info "Available agents in project:"
    echo
    for agent_file in "$PROJECT_AGENTS_DIR"/*.md; do
        if [ "$(basename "$agent_file")" = "README.md" ]; then
            continue
        fi
        
        agent_name=$(basename "$agent_file" .md)
        
        # Try to extract description from the agent file
        description=""
        if [ -f "$agent_file" ]; then
            # Look for a description line in the first few lines
            description=$(head -10 "$agent_file" | grep -E "^(#|Description:|Use this agent)" | head -1 | sed 's/^[#*-] *//' | cut -c1-80)
        fi
        
        printf "  %-25s %s\n" "$agent_name" "$description"
    done
    echo
}

# Function to show status
show_status() {
    print_info "Agent installation status:"
    echo
    
    if [ ! -d "$USER_AGENTS_DIR" ]; then
        print_warning "User agents directory does not exist: $USER_AGENTS_DIR"
        return
    fi
    
    for agent_file in "$PROJECT_AGENTS_DIR"/*.md; do
        if [ "$(basename "$agent_file")" = "README.md" ]; then
            continue
        fi
        
        agent_name=$(basename "$agent_file")
        target_file="$USER_AGENTS_DIR/$agent_name"
        
        if [ -f "$target_file" ]; then
            print_success "✓ $agent_name"
        else
            print_warning "✗ $agent_name (not installed)"
        fi
    done
    echo
}

# Function to remove agents
remove_agents() {
    print_warning "This will remove all project agents from your user directory"
    read -p "Are you sure? (y/N): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "Operation cancelled"
        return
    fi
    
    print_info "Removing project agents from user directory..."
    
    for agent_file in "$PROJECT_AGENTS_DIR"/*.md; do
        agent_name=$(basename "$agent_file")
        target_file="$USER_AGENTS_DIR/$agent_name"
        
        if [ -f "$target_file" ]; then
            rm "$target_file"
            print_success "Removed: $agent_name"
        fi
    done
}

# Function to show help
show_help() {
    echo "setup-agents.sh - Install Claude Code agents to user-level directory"
    echo
    echo "Usage:"
    echo "  ./setup-agents.sh [command] [options]"
    echo
    echo "Commands:"
    echo "  install, -i       Install agents to user directory (default)"
    echo "  list, -l          List available agents"
    echo "  status, -s        Show installation status"
    echo "  remove, -r        Remove project agents from user directory"
    echo "  help, -h          Show this help message"
    echo
    echo "Options:"
    echo "  --force, -f       Force overwrite existing agents (install only)"
    echo
    echo "Examples:"
    echo "  ./setup-agents.sh                    # Install agents"
    echo "  ./setup-agents.sh install --force    # Force install all agents"
    echo "  ./setup-agents.sh list               # List available agents"
    echo "  ./setup-agents.sh status             # Check installation status"
    echo
}

# Main script logic
case "${1:-install}" in
    install|-i)
        copy_agents "$2"
        print_success "Agent installation completed!"
        echo
        print_info "Agents are now available in Claude Code. You can use them by running:"
        print_info "  claude --agent <agent-name>"
        ;;
    list|-l)
        list_agents
        ;;
    status|-s)
        show_status
        ;;
    remove|-r)
        remove_agents
        ;;
    help|-h|--help)
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        echo
        show_help
        exit 1
        ;;
esac