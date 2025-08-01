#!/bin/bash

# Toggle Token Optimization On/Off for Current Session
# Allows A/B testing to measure actual token savings

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DISABLE_FLAG="$PROJECT_ROOT/.optimization_disabled"

show_usage() {
    echo "Usage: $0 [on|off|status|test]"
    echo ""
    echo "Commands:"
    echo "  on     - Enable optimizations for this session"
    echo "  off    - Disable optimizations for this session"
    echo "  status - Show current optimization status"
    echo "  test   - Run A/B test to measure token savings"
    echo ""
    echo "Examples:"
    echo "  $0 off    # Disable for testing baseline usage"
    echo "  $0 on     # Re-enable optimizations"
    echo "  $0 test   # Compare optimized vs unoptimized performance"
}

enable_optimizations() {
    if [ -f "$DISABLE_FLAG" ]; then
        rm "$DISABLE_FLAG"
    fi
    
    # Re-export optimization environment variables
    source "$PROJECT_ROOT/token_optimize.env"
    
    echo "✅ Token optimizations ENABLED for this session"
    echo "   - Smart caching active"
    echo "   - Prompt compression active"
    echo "   - Token monitoring active"
    echo ""
    echo "💡 All Claude Code operations will use optimizations"
}

disable_optimizations() {
    # Create disable flag that hooks will check
    touch "$DISABLE_FLAG"
    
    # Unset optimization environment variables for this session
    unset DISABLE_NON_ESSENTIAL_MODEL_CALLS
    unset ANTHROPIC_SMALL_FAST_MODEL
    unset CLAUDE_CODE_MAX_OUTPUT_TOKENS
    
    echo "🚫 Token optimizations DISABLED for this session"
    echo "   - No caching (fresh reads every time)"
    echo "   - No prompt compression"
    echo "   - Standard Claude Code behavior"
    echo ""
    echo "⚠️  This will use MORE tokens - good for baseline testing"
    echo ""
    echo "🔄 Run '$0 on' to re-enable optimizations"
}

show_status() {
    echo "📊 Current Token Optimization Status"
    echo "===================================="
    
    if [ -f "$DISABLE_FLAG" ]; then
        echo "Status: 🚫 DISABLED (testing mode)"
        echo ""
        echo "Active Settings:"
        echo "  - Caching: OFF"
        echo "  - Prompt optimization: OFF"  
        echo "  - Environment optimizations: OFF"
        echo ""
        echo "💡 This session will use baseline token consumption"
    else
        echo "Status: ✅ ENABLED (optimized mode)"
        echo ""
        echo "Active Settings:"
        echo "  - Caching: ON"
        echo "  - Prompt optimization: ON"
        echo "  - Environment optimizations: ON"
        echo ""
        
        # Show environment variable status
        if [ "$DISABLE_NON_ESSENTIAL_MODEL_CALLS" = "1" ]; then
            echo "  ✅ Non-essential calls disabled"
        else
            echo "  ❌ Non-essential calls not disabled"
        fi
        
        if [ -n "$ANTHROPIC_SMALL_FAST_MODEL" ]; then
            echo "  ✅ Small model set: $ANTHROPIC_SMALL_FAST_MODEL"
        else
            echo "  ❌ Small model not configured"
        fi
        
        if [ -n "$CLAUDE_CODE_MAX_OUTPUT_TOKENS" ]; then
            echo "  ✅ Output token limit: $CLAUDE_CODE_MAX_OUTPUT_TOKENS"
        else
            echo "  ❌ Output token limit not set"
        fi
    fi
    
    echo ""
    echo "Commands:"
    echo "  $0 off  - Disable for baseline testing"
    echo "  $0 on   - Enable optimizations"
    echo "  $0 test - Run A/B comparison test"
}

run_ab_test() {
    echo "🧪 Token Optimization A/B Test"
    echo "==============================="
    echo ""
    echo "This test will help you measure actual token savings by:"
    echo "1. Running identical operations with optimizations OFF"
    echo "2. Running identical operations with optimizations ON"
    echo "3. Comparing token usage between the two"
    echo ""
    
    read -p "Continue with A/B test? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Test cancelled"
        exit 0
    fi
    
    echo ""
    echo "📋 Test Instructions:"
    echo "===================="
    echo ""
    echo "PHASE 1 - Baseline (No Optimizations):"
    echo "1. Optimizations are now DISABLED"
    echo "2. Perform your typical Claude Code tasks"
    echo "3. Note the token usage from the session"
    echo "4. When done, run: $0 test-phase2"
    echo ""
    
    # Disable optimizations for baseline
    disable_optimizations
    
    echo "🚫 BASELINE MODE ACTIVE - Record your token usage!"
}

run_ab_test_phase2() {
    echo "🧪 A/B Test - Phase 2 (Optimized)"
    echo "=================================="
    echo ""
    echo "PHASE 2 - Optimized Mode:"
    echo "1. Optimizations are now ENABLED"
    echo "2. Perform the SAME tasks you did in Phase 1"
    echo "3. Compare token usage with Phase 1"
    echo "4. Calculate your savings!"
    echo ""
    
    # Enable optimizations for comparison
    enable_optimizations
    
    echo "✅ OPTIMIZED MODE ACTIVE - Compare with baseline!"
    echo ""
    echo "📊 To view token usage comparison:"
    echo "   ../logs/monitoring/token_summary.sh"
}

# Parse command line arguments
case "${1:-status}" in
    "on"|"enable")
        enable_optimizations
        ;;
    "off"|"disable")
        disable_optimizations
        ;;
    "status"|"")
        show_status
        ;;
    "test")
        run_ab_test
        ;;
    "test-phase2")
        run_ab_test_phase2
        ;;
    "-h"|"--help"|"help")
        show_usage
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo ""
        show_usage
        exit 1
        ;;
esac