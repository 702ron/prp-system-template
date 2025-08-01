# /token-optimize

Quick command to apply token optimization settings and check current usage.

## Usage
```bash
/token-optimize [--setup|--status|--reset]
```

## Arguments
- `--setup` - Run initial setup and enable all optimizations
- `--status` - Show current token usage and optimization status  
- `--reset` - Reset optimization settings to defaults

## What This Command Does

### Default (no args)
- Sources optimization environment variables
- Shows current token usage summary
- Reports cache effectiveness
- Displays optimization statistics

### With --setup
- Runs complete token optimization setup
- Enables all hooks and caching
- Creates monitoring dashboard
- Sets environment variables

### With --status  
- Shows detailed token usage breakdown
- Cache hit rates and effectiveness
- Prompt optimization statistics
- Recommendations for further savings

### With --reset
- Disables optimization hooks
- Clears caches
- Resets environment variables
- Returns to default Claude Code behavior

## Token Savings Expected
- **File Caching**: 50-80% reduction in redundant reads
- **Prompt Compression**: 5-15% reduction in length
- **Smart Routing**: 60-70% savings on simple queries  
- **Command Caching**: 40-60% reduction in repeated executions

**Total Expected Savings: 30-50% for typical development workflows**