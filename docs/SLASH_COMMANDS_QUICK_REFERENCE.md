# Slash Commands Quick Reference

## 🚀 Essential Commands

### File Operations

| Command   | Purpose             | Example                           |
| --------- | ------------------- | --------------------------------- |
| `/read`   | Read file contents  | `/read src/components/Button.tsx` |
| `/edit`   | Make precise edits  | `/edit src/components/Button.tsx` |
| `/search` | Search for patterns | `/search "useState"`              |
| `/grep`   | Find exact text     | `/grep "export default"`          |
| `/list`   | Explore directories | `/list src/components/`           |

### Development Tools

| Command           | Purpose                   | Example                            |
| ----------------- | ------------------------- | ---------------------------------- |
| `/run`            | Execute terminal commands | `/run npm test`                    |
| `/mcp_supabase_*` | Database operations       | `/mcp_supabase_list_tables`        |
| `/mcp_github_*`   | Repository management     | `/mcp_github_create_issue`         |
| `/mcp_context7_*` | Library documentation     | `/mcp_context7_resolve-library-id` |

### AI-Assisted Development

| Command            | Purpose              | Example                             |
| ------------------ | -------------------- | ----------------------------------- |
| `/codebase_search` | Semantic code search | `/codebase_search "authentication"` |
| `/file_search`     | Fuzzy file search    | `/file_search "Button"`             |

## 📋 Task Management

### Progress Reporting Format

```markdown
## ✅ Task Phase Complete: [Phase Name]

### What was accomplished:

- [ ] Specific achievement 1
- [ ] Specific achievement 2

### Next Steps:

1. **Immediate Next Action**: [Action with command if applicable]
2. **Follow-up Tasks**: [List of related tasks]

### Commands Used:

- `/command1` - [purpose]
- `/command2` - [purpose]
```

### Task Completion Template

```markdown
## 🎯 Task Complete: [Task Name]

### Summary of Accomplishments:

- [ ] [Specific achievement with impact]

### Files Modified:

- `path/to/file` - [what was changed]

### Commands Executed:

- `/command` - [purpose and outcome]

### Next Steps:

1. **Immediate Actions**: [if any]
2. **Follow-up Tasks**: [related tasks]
3. **Testing & Validation**: [test commands]
4. **Documentation Updates**: [docs to update]
```

## 🔧 Best Practices

### 1. Always Use Available Tools

- Check available commands before manual work
- Use `/read` to understand current file state
- Use `/search` to find relevant patterns
- Use `/run` for terminal operations

### 2. Be Specific with Commands

- Provide clear parameters for each command
- Explain the purpose of each command used
- Use appropriate flags and options

### 3. Handle Errors Gracefully

- When commands fail, provide clear error analysis
- Suggest alternative approaches
- Document any workarounds needed

### 4. Maintain Context

- Keep track of which files have been modified
- Note any configuration changes made
- Document any new dependencies added

## 🎯 Common Workflows

### Creating a New Component

```bash
# 1. Read existing patterns
/read src/components/Button.tsx

# 2. Search for similar components
/search "interface Props"

# 3. Create new component
/edit src/components/NewComponent.tsx

# 4. Run tests
/run npm test NewComponent

# 5. Update documentation
/edit README.md
```

### Database Operations

```bash
# 1. List current tables
/mcp_supabase_list_tables

# 2. Apply migration
/mcp_supabase_apply_migration

# 3. Execute SQL
/mcp_supabase_execute_sql

# 4. Check logs
/mcp_supabase_get_logs
```

### GitHub Operations

```bash
# 1. Create issue
/mcp_github_create_issue

# 2. Create PR
/mcp_github_create_pull_request

# 3. Push files
/mcp_github_push_files

# 4. Review PR
/mcp_github_create_pull_request_review
```

## 🚨 Troubleshooting

### Common Issues

1. **Command not found**: Check command syntax and parameters
2. **Permission errors**: Verify file permissions and access
3. **Missing dependencies**: Check if required tools are installed
4. **Network issues**: Verify internet connection for external services

### Error Handling

- Use `/read` to understand current state
- Provide clear error messages and context
- Suggest alternative approaches when commands fail
- Document workarounds for future reference

## 📚 Related Documentation

- **Full Guidelines**: `/read docs/CLAUDE.md`
- **PRP Templates**: `/list PRPs/templates/`
- **AI Documentation**: `/list PRPs/ai_docs/`
- **Examples**: `/list PRPs/examples/`

---

**Remember**: Always use slash commands when available to maximize efficiency and maintain consistency in your development workflow.
