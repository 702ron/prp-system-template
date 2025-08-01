# /token-test

Toggle token optimizations on/off for A/B testing and measuring actual savings.

## Usage
```bash
/token-test [on|off|status|test]
```

## Arguments
- `on` - Enable optimizations for this session
- `off` - Disable optimizations for baseline testing
- `status` - Show current optimization status
- `test` - Run guided A/B test to measure token savings

## What This Command Does

### Default (no args) - Status
Shows whether optimizations are currently enabled or disabled for this session.

### With `off` - Disable for Testing
- ✅ Disables smart caching (fresh reads every time)
- ✅ Disables prompt compression
- ✅ Disables environment optimizations
- ✅ Records baseline token usage for comparison

Perfect for establishing baseline token consumption.

### With `on` - Re-enable Optimizations
- ✅ Re-enables all smart caching
- ✅ Re-enables prompt optimization
- ✅ Re-enables environment optimizations

### With `test` - Guided A/B Testing
Runs a structured test to measure actual token savings:

1. **Phase 1**: Disables optimizations, prompts you to perform tasks
2. **Phase 2**: Enables optimizations, prompts you to repeat same tasks
3. **Comparison**: Shows token usage difference

## Testing Workflow Example

```bash
# Start A/B test
/token-test test

# ... perform your typical Claude Code tasks (caching disabled) ...
# Note the token usage

# Continue to phase 2
/token-test test-phase2

# ... perform the SAME tasks (caching enabled) ...
# Compare token usage - you'll see the savings!

# Check status anytime
/token-test status
```

## Why Use This?

- **Measure real savings** from your actual workflow
- **Validate optimization effectiveness** with concrete numbers
- **Test different scenarios** (file-heavy vs command-heavy workflows)
- **Compare baseline vs optimized** token consumption

The optimizations remain permanently installed - this just toggles them on/off for the current session.