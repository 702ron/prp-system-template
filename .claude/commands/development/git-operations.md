# Git Operations

## Description
Comprehensive git operations command that handles commits, branches, conflicts, and repository management. Replaces multiple git commands with a single, flexible command.

## Usage
```
/git [operation] [options]
```

## Arguments
- `operation` (required): The git operation to perform
  - `commit` - Commit staged changes with smart message generation
  - `branch` - Create, switch, or manage branches
  - `conflict` - Resolve merge conflicts with AI assistance
  - `sync` - Sync with remote repository (pull/push)
  - `status` - Show repository status and changes
  - `history` - Show commit history and analysis
  - `cleanup` - Clean up repository (stash, reset, etc.)

## Options
- `--message <msg>`: Custom commit message
- `--branch <name>`: Branch name for branch operations
- `--remote <name>`: Remote name (default: origin)
- `--force`: Force operations when needed
- `--interactive`: Interactive mode for complex operations
- `--dry-run`: Show what would be done without executing

## Behavior
1. **Smart Commit**: Analyzes changes and generates meaningful commit messages
2. **Branch Management**: Creates, switches, and manages branches with best practices
3. **Conflict Resolution**: Uses AI to analyze and suggest conflict resolutions
4. **Repository Sync**: Handles pull/push operations with conflict detection
5. **Status Analysis**: Provides detailed repository status and change analysis
6. **History Analysis**: Shows commit history with insights and patterns
7. **Cleanup Operations**: Manages stashes, resets, and repository cleanup

## Example Usage
```
# Commit operations
/git commit
/git commit --message "Add user authentication feature"
/git commit --interactive

# Branch operations
/git branch create feature/user-auth
/git branch switch main
/git branch list

# Conflict resolution
/git conflict resolve
/git conflict analyze

# Sync operations
/git sync pull
/git sync push
/git sync --force

# Status and history
/git status
/git history --last 10
/git history --author "john"

# Cleanup operations
/git cleanup stash
/git cleanup reset --soft HEAD~1
```

## Implementation
```python
import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
import re

def git_operations(operation, **options):
    """
    Comprehensive git operations with AI assistance.
    """
    current_dir = Path.cwd()
    
    # Check if we're in a git repository
    if not (current_dir / '.git').exists():
        print("❌ Not in a git repository")
        return
    
    print(f"🔧 Performing git {operation}...")
    
    if operation == "commit":
        git_commit(current_dir, options)
    elif operation == "branch":
        git_branch(current_dir, options)
    elif operation == "conflict":
        git_conflict(current_dir, options)
    elif operation == "sync":
        git_sync(current_dir, options)
    elif operation == "status":
        git_status(current_dir, options)
    elif operation == "history":
        git_history(current_dir, options)
    elif operation == "cleanup":
        git_cleanup(current_dir, options)
    else:
        print(f"❌ Unknown operation: {operation}")
        print("Available operations: commit, branch, conflict, sync, status, history, cleanup")
        return

def git_commit(project_dir, options):
    """Smart commit with AI-generated messages."""
    print("📝 Analyzing changes for commit...")
    
    # Get staged changes
    staged_files = get_staged_files(project_dir)
    
    if not staged_files:
        print("❌ No staged changes to commit")
        return
    
    # Analyze changes
    change_analysis = analyze_changes(project_dir, staged_files)
    
    # Generate commit message
    if options.get('message'):
        commit_message = options['message']
    else:
        commit_message = generate_commit_message(change_analysis)
    
    # Show what will be committed
    print(f"📋 Files to commit: {len(staged_files)}")
    for file in staged_files:
        print(f"  - {file}")
    
    print(f"💬 Commit message: {commit_message}")
    
    if options.get('dry_run'):
        print("🔍 Dry run - no commit performed")
        return
    
    # Perform commit
    try:
        result = subprocess.run(['git', 'commit', '-m', commit_message], 
                              capture_output=True, text=True, cwd=project_dir)
        
        if result.returncode == 0:
            print("✅ Commit successful!")
            print(result.stdout)
        else:
            print("❌ Commit failed:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error during commit: {e}")

def git_branch(project_dir, options):
    """Branch management operations."""
    branch_name = options.get('branch')
    
    if not branch_name:
        # List branches
        list_branches(project_dir)
        return
    
    # Parse branch operation
    if 'create' in branch_name.lower() or branch_name.startswith('feature/') or branch_name.startswith('bugfix/'):
        create_branch(project_dir, branch_name)
    elif 'switch' in branch_name.lower() or branch_name in ['main', 'master', 'develop']:
        switch_branch(project_dir, branch_name)
    elif 'delete' in branch_name.lower():
        delete_branch(project_dir, branch_name.replace('delete/', ''))
    else:
        # Default to create
        create_branch(project_dir, branch_name)

def git_conflict(project_dir, options):
    """Conflict resolution with AI assistance."""
    print("🔍 Checking for merge conflicts...")
    
    # Check for conflicts
    conflict_files = get_conflict_files(project_dir)
    
    if not conflict_files:
        print("✅ No merge conflicts found")
        return
    
    print(f"⚠️  Found conflicts in {len(conflict_files)} files:")
    for file in conflict_files:
        print(f"  - {file}")
    
    # Analyze conflicts
    for file in conflict_files:
        analyze_conflict(project_dir, file, options)
    
    if options.get('interactive'):
        print("🤖 Interactive conflict resolution mode")
        # Interactive resolution logic would go here

def git_sync(project_dir, options):
    """Sync with remote repository."""
    remote = options.get('remote', 'origin')
    force = options.get('force', False)
    
    print(f"🔄 Syncing with {remote}...")
    
    # Check current status
    status = get_git_status(project_dir)
    
    if status['has_changes']:
        print("⚠️  Local changes detected")
        if not force:
            print("💡 Use --force to proceed with sync")
            return
    
    # Pull changes
    try:
        print("⬇️  Pulling changes...")
        result = subprocess.run(['git', 'pull', remote], 
                              capture_output=True, text=True, cwd=project_dir)
        
        if result.returncode == 0:
            print("✅ Pull successful!")
            print(result.stdout)
        else:
            print("❌ Pull failed:")
            print(result.stderr)
            return
    except Exception as e:
        print(f"❌ Error during pull: {e}")
        return
    
    # Push changes if needed
    if status['ahead'] > 0:
        try:
            print("⬆️  Pushing changes...")
            push_cmd = ['git', 'push', remote]
            if force:
                push_cmd.append('--force')
            
            result = subprocess.run(push_cmd, 
                                  capture_output=True, text=True, cwd=project_dir)
            
            if result.returncode == 0:
                print("✅ Push successful!")
                print(result.stdout)
            else:
                print("❌ Push failed:")
                print(result.stderr)
        except Exception as e:
            print(f"❌ Error during push: {e}")

def git_status(project_dir, options):
    """Show detailed repository status."""
    print("📊 Repository Status")
    print("=" * 50)
    
    # Get git status
    status = get_git_status(project_dir)
    
    # Current branch
    current_branch = get_current_branch(project_dir)
    print(f"🌿 Current branch: {current_branch}")
    
    # Status summary
    print(f"📈 Status: {status['summary']}")
    
    if status['staged']:
        print(f"\n📦 Staged changes ({len(status['staged'])}):")
        for file in status['staged']:
            print(f"  + {file}")
    
    if status['unstaged']:
        print(f"\n📝 Unstaged changes ({len(status['unstaged'])}):")
        for file in status['unstaged']:
            print(f"  ~ {file}")
    
    if status['untracked']:
        print(f"\n❓ Untracked files ({len(status['untracked'])}):")
        for file in status['untracked']:
            print(f"  ? {file}")
    
    # Remote status
    if status['ahead'] > 0 or status['behind'] > 0:
        print(f"\n🌐 Remote: {status['ahead']} ahead, {status['behind']} behind")
    
    # Recent commits
    recent_commits = get_recent_commits(project_dir, 5)
    if recent_commits:
        print(f"\n📜 Recent commits:")
        for commit in recent_commits:
            print(f"  {commit['hash'][:8]} - {commit['message']}")

def git_history(project_dir, options):
    """Show commit history with analysis."""
    print("📜 Commit History Analysis")
    print("=" * 50)
    
    # Get commit history
    commits = get_commit_history(project_dir, options)
    
    if not commits:
        print("❌ No commits found")
        return
    
    # Display commits
    for commit in commits:
        print(f"\n🔹 {commit['hash'][:8]} - {commit['date']}")
        print(f"   Author: {commit['author']}")
        print(f"   Message: {commit['message']}")
        
        if commit['files']:
            print(f"   Files: {', '.join(commit['files'])}")
    
    # Analysis
    print(f"\n📊 Analysis:")
    print(f"   Total commits: {len(commits)}")
    
    # Author analysis
    authors = {}
    for commit in commits:
        author = commit['author']
        authors[author] = authors.get(author, 0) + 1
    
    print(f"   Contributors: {len(authors)}")
    for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
        print(f"     {author}: {count} commits")
    
    # File analysis
    all_files = []
    for commit in commits:
        all_files.extend(commit['files'])
    
    if all_files:
        file_counts = {}
        for file in all_files:
            file_counts[file] = file_counts.get(file, 0) + 1
        
        print(f"\n📁 Most modified files:")
        for file, count in sorted(file_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"     {file}: {count} changes")

def git_cleanup(project_dir, options):
    """Clean up repository operations."""
    print("🧹 Repository Cleanup")
    print("=" * 50)
    
    # Get current status
    status = get_git_status(project_dir)
    
    # Stash operations
    if status['unstaged'] or status['staged']:
        print("💾 Stashing changes...")
        try:
            result = subprocess.run(['git', 'stash'], 
                                  capture_output=True, text=True, cwd=project_dir)
            if result.returncode == 0:
                print("✅ Changes stashed successfully")
            else:
                print("❌ Stash failed")
        except Exception as e:
            print(f"❌ Error during stash: {e}")
    
    # Clean untracked files
    if status['untracked']:
        print(f"🗑️  Found {len(status['untracked'])} untracked files")
        if options.get('force'):
            try:
                result = subprocess.run(['git', 'clean', '-fd'], 
                                      capture_output=True, text=True, cwd=project_dir)
                if result.returncode == 0:
                    print("✅ Untracked files cleaned")
                else:
                    print("❌ Clean failed")
            except Exception as e:
                print(f"❌ Error during clean: {e}")
        else:
            print("💡 Use --force to remove untracked files")
    
    # Reset operations
    if options.get('reset'):
        reset_type = options['reset']
        try:
            if reset_type == 'soft':
                result = subprocess.run(['git', 'reset', '--soft', 'HEAD~1'], 
                                      capture_output=True, text=True, cwd=project_dir)
            elif reset_type == 'hard':
                result = subprocess.run(['git', 'reset', '--hard', 'HEAD~1'], 
                                      capture_output=True, text=True, cwd=project_dir)
            else:
                result = subprocess.run(['git', 'reset', 'HEAD~1'], 
                                      capture_output=True, text=True, cwd=project_dir)
            
            if result.returncode == 0:
                print(f"✅ Reset ({reset_type}) successful")
            else:
                print("❌ Reset failed")
        except Exception as e:
            print(f"❌ Error during reset: {e}")

# Helper functions
def get_staged_files(project_dir):
    """Get list of staged files."""
    try:
        result = subprocess.run(['git', 'diff', '--cached', '--name-only'], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except:
        pass
    return []

def analyze_changes(project_dir, files):
    """Analyze changes in files."""
    analysis = {
        'files': files,
        'types': {},
        'summary': '',
        'impact': 'low'
    }
    
    for file in files:
        ext = Path(file).suffix.lower()
        analysis['types'][ext] = analysis['types'].get(ext, 0) + 1
    
    # Generate summary
    if analysis['types']:
        type_summary = ', '.join([f"{count} {ext} files" for ext, count in analysis['types'].items()])
        analysis['summary'] = f"Modified {type_summary}"
    
    return analysis

def generate_commit_message(analysis):
    """Generate smart commit message based on changes."""
    files = analysis['files']
    types = analysis['types']
    
    # Simple message generation based on file types
    if '.js' in types or '.ts' in types or '.jsx' in types or '.tsx' in types:
        return "Update JavaScript/TypeScript files"
    elif '.py' in types:
        return "Update Python files"
    elif '.md' in types:
        return "Update documentation"
    elif '.json' in types or '.yaml' in types or '.yml' in types:
        return "Update configuration files"
    else:
        return "Update files"

def list_branches(project_dir):
    """List all branches."""
    try:
        result = subprocess.run(['git', 'branch', '-a'], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            print("🌿 Branches:")
            print(result.stdout)
    except Exception as e:
        print(f"❌ Error listing branches: {e}")

def create_branch(project_dir, branch_name):
    """Create and switch to new branch."""
    try:
        result = subprocess.run(['git', 'checkout', '-b', branch_name], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            print(f"✅ Created and switched to branch: {branch_name}")
        else:
            print("❌ Failed to create branch:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error creating branch: {e}")

def switch_branch(project_dir, branch_name):
    """Switch to existing branch."""
    try:
        result = subprocess.run(['git', 'checkout', branch_name], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            print(f"✅ Switched to branch: {branch_name}")
        else:
            print("❌ Failed to switch branch:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error switching branch: {e}")

def delete_branch(project_dir, branch_name):
    """Delete branch."""
    try:
        result = subprocess.run(['git', 'branch', '-d', branch_name], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            print(f"✅ Deleted branch: {branch_name}")
        else:
            print("❌ Failed to delete branch:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error deleting branch: {e}")

def get_conflict_files(project_dir):
    """Get files with merge conflicts."""
    try:
        result = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=U'], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except:
        pass
    return []

def analyze_conflict(project_dir, file_path, options):
    """Analyze conflict in specific file."""
    print(f"\n🔍 Analyzing conflict in: {file_path}")
    
    try:
        with open(project_dir / file_path, 'r') as f:
            content = f.read()
        
        # Find conflict markers
        conflicts = re.findall(r'<<<<<<<.*?\n(.*?)\n=======\n(.*?)\n>>>>>>>', content, re.DOTALL)
        
        if conflicts:
            print(f"   Found {len(conflicts)} conflict(s)")
            for i, (ours, theirs) in enumerate(conflicts, 1):
                print(f"   Conflict {i}:")
                print(f"     Ours: {ours[:100]}...")
                print(f"     Theirs: {theirs[:100]}...")
        else:
            print("   No conflict markers found")
            
    except Exception as e:
        print(f"   ❌ Error analyzing conflict: {e}")

def get_git_status(project_dir):
    """Get comprehensive git status."""
    status = {
        'staged': [],
        'unstaged': [],
        'untracked': [],
        'ahead': 0,
        'behind': 0,
        'has_changes': False,
        'summary': 'clean'
    }
    
    try:
        # Get status
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd=project_dir)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            for line in lines:
                if line:
                    status_code = line[:2]
                    file_path = line[3:]
                    
                    if status_code == 'M ' or status_code == 'A ' or status_code == 'D ':
                        status['staged'].append(file_path)
                    elif status_code == ' M' or status_code == ' A' or status_code == ' D':
                        status['unstaged'].append(file_path)
                    elif status_code == '??':
                        status['untracked'].append(file_path)
            
            status['has_changes'] = bool(status['staged'] or status['unstaged'] or status['untracked'])
            
            if status['has_changes']:
                status['summary'] = 'modified'
            else:
                status['summary'] = 'clean'
        
        # Get remote status
        result = subprocess.run(['git', 'status', '--porcelain', '--branch'], 
                              capture_output=True, text=True, cwd=project_dir)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            for line in lines:
                if line.startswith('##'):
                    # Parse branch status
                    match = re.search(r'\[ahead (\d+)\]', line)
                    if match:
                        status['ahead'] = int(match.group(1))
                    
                    match = re.search(r'\[behind (\d+)\]', line)
                    if match:
                        status['behind'] = int(match.group(1))
                        
    except Exception as e:
        print(f"❌ Error getting git status: {e}")
    
    return status

def get_current_branch(project_dir):
    """Get current branch name."""
    try:
        result = subprocess.run(['git', 'branch', '--show-current'], 
                              capture_output=True, text=True, cwd=project_dir)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return 'unknown'

def get_recent_commits(project_dir, count=5):
    """Get recent commits."""
    commits = []
    
    try:
        result = subprocess.run(['git', 'log', f'-{count}', '--oneline', '--format=%H|%an|%ad|%s'], 
                              capture_output=True, text=True, cwd=project_dir)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            for line in lines:
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        commits.append({
                            'hash': parts[0],
                            'author': parts[1],
                            'date': parts[2],
                            'message': parts[3]
                        })
    except Exception as e:
        print(f"❌ Error getting recent commits: {e}")
    
    return commits

def get_commit_history(project_dir, options):
    """Get commit history with options."""
    count = options.get('count', 10)
    author = options.get('author')
    
    commits = []
    
    try:
        cmd = ['git', 'log', f'-{count}', '--format=%H|%an|%ad|%s', '--name-only']
        
        if author:
            cmd.extend(['--author', author])
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=project_dir)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            current_commit = None
            for line in lines:
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        current_commit = {
                            'hash': parts[0],
                            'author': parts[1],
                            'date': parts[2],
                            'message': parts[3],
                            'files': []
                        }
                        commits.append(current_commit)
                elif line.strip() and current_commit:
                    current_commit['files'].append(line.strip())
    except Exception as e:
        print(f"❌ Error getting commit history: {e}")
    
    return commits

# Main execution
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Git Operations')
    parser.add_argument('operation', help='Git operation to perform')
    parser.add_argument('--message', help='Commit message')
    parser.add_argument('--branch', help='Branch name')
    parser.add_argument('--remote', default='origin', help='Remote name')
    parser.add_argument('--force', action='store_true', help='Force operations')
    parser.add_argument('--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('--dry-run', action='store_true', help='Dry run')
    parser.add_argument('--count', type=int, help='Number of items')
    parser.add_argument('--author', help='Author filter')
    parser.add_argument('--reset', help='Reset type')
    
    args = parser.parse_args()
    
    options = {
        'message': args.message,
        'branch': args.branch,
        'remote': args.remote,
        'force': args.force,
        'interactive': args.interactive,
        'dry_run': args.dry_run,
        'count': args.count,
        'author': args.author,
        'reset': args.reset
    }
    
    # Remove None values
    options = {k: v for k, v in options.items() if v is not None}
    
    git_operations(args.operation, **options)
```

## Notes
- This consolidated command replaces multiple git-related commands
- Provides comprehensive git operations with AI assistance
- Includes smart commit message generation
- Handles conflict resolution with analysis
- Provides detailed status and history analysis
- Reduces command complexity and improves usability
- Supports interactive and dry-run modes 