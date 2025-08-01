# Create Conversation Summary

Generate a comprehensive summary of the current conversation including what was accomplished, technical decisions, and key learnings.

## Usage

```bash
/create-summary [--output-file FILENAME] [--format FORMAT] [--include-context]
```

## Arguments

- `--output-file` (optional): Custom filename for the summary (default: `CONVERSATION_SUMMARY_YYYY-MM-DD_HHMMSS.md`)
- `--format` (optional): Output format - `markdown`, `json`, or `both` (default: `markdown`)
- `--include-context` (optional): Include full conversation context and technical details

## Examples

```bash
# Generate basic summary
/create-summary

# Generate detailed summary with custom filename
/create-summary --output-file "sprint_2_summary.md" --include-context

# Generate both markdown and JSON formats
/create-summary --format both --include-context
```

## What Gets Analyzed

- **Conversation Flow**: Key topics, requests, and outcomes
- **Technical Changes**: Files created, modified, or deleted
- **Problem Solving**: Issues encountered and solutions implemented
- **Tool Usage**: Which tools were used and their effectiveness
- **Code Quality**: Testing, linting, and validation performed
- **Git Activity**: Commits, branches, and repository changes
- **Learning Points**: Key insights and recommendations

## Output Structure

### Markdown Format
- Executive summary
- Detailed accomplishments
- Technical decisions and rationale
- Issues encountered and resolutions
- File changes and code modifications
- Testing and validation results
- Recommendations for future work

### JSON Format
- Structured data for programmatic processing
- Metrics and statistics
- File change lists
- Tool usage analytics
- Timeline of activities

## Implementation

This command uses the conversation logging system to analyze:
- Claude's JSONL conversation logs
- Project-level prompt logs
- Tool usage tracking data
- Git history and file changes
- Error logs and resolution patterns

The summary is generated using AI analysis of the conversation data combined with project context to create actionable documentation for future development sessions.