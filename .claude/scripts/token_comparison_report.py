#!/usr/bin/env python3

"""
Token Usage Comparison Report Generator
Analyzes logs to show optimization effectiveness and token savings.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any
import argparse

def load_prompt_logs(logs_dir: Path, days_back: int = 7) -> List[Dict[str, Any]]:
    """Load prompt logs from the last N days."""
    all_logs = []
    
    for i in range(days_back):
        date = datetime.now() - timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        log_file = logs_dir / f"user_prompts_{date_str}.json"
        
        if log_file.exists():
            try:
                with open(log_file, 'r') as f:
                    daily_logs = json.load(f)
                    all_logs.extend(daily_logs)
            except (json.JSONDecodeError, IOError):
                continue
    
    return all_logs

def analyze_optimization_effectiveness(logs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze the effectiveness of optimizations."""
    optimized_sessions = []
    baseline_sessions = []
    
    for log in logs:
        if log.get('optimization_disabled') or log.get('baseline_mode'):
            baseline_sessions.append(log)
        else:
            optimized_sessions.append(log)
    
    analysis = {
        'total_prompts': len(logs),
        'optimized_prompts': len(optimized_sessions),
        'baseline_prompts': len(baseline_sessions),
        'optimization_stats': {},
        'baseline_stats': {},
        'comparison': {}
    }
    
    # Analyze optimized sessions
    if optimized_sessions:
        total_original = sum(log.get('original_length', 0) for log in optimized_sessions)
        total_compressed = sum(log.get('compressed_length', 0) for log in optimized_sessions)
        total_savings = sum(log.get('token_savings', 0) for log in optimized_sessions)
        simple_queries = sum(1 for log in optimized_sessions if log.get('is_simple_query', False))
        
        analysis['optimization_stats'] = {
            'total_original_chars': total_original,
            'total_compressed_chars': total_compressed,
            'total_savings': total_savings,
            'avg_original_length': total_original / len(optimized_sessions),
            'avg_compressed_length': total_compressed / len(optimized_sessions),
            'avg_savings_per_prompt': total_savings / len(optimized_sessions),
            'compression_ratio': (total_savings / max(total_original, 1)) * 100,
            'simple_queries': simple_queries,
            'simple_query_rate': (simple_queries / len(optimized_sessions)) * 100
        }
    
    # Analyze baseline sessions
    if baseline_sessions:
        total_baseline = sum(log.get('original_length', 0) for log in baseline_sessions)
        
        analysis['baseline_stats'] = {
            'total_chars': total_baseline,
            'avg_length': total_baseline / len(baseline_sessions)
        }
    
    # Compare if we have both
    if optimized_sessions and baseline_sessions:
        opt_avg = analysis['optimization_stats']['avg_compressed_length']
        baseline_avg = analysis['baseline_stats']['avg_length']
        
        if baseline_avg > 0:
            savings_pct = ((baseline_avg - opt_avg) / baseline_avg) * 100
            analysis['comparison'] = {
                'baseline_avg_length': baseline_avg,
                'optimized_avg_length': opt_avg,
                'savings_percentage': savings_pct,
                'chars_saved_per_prompt': baseline_avg - opt_avg
            }
    
    return analysis

def load_conversation_data() -> Dict[str, Any]:
    """Load recent conversation data to get token usage."""
    try:
        script_dir = Path(__file__).parent
        logger_script = script_dir / "claude_jsonl_logger.py"
        
        if logger_script.exists():
            import subprocess
            result = subprocess.run([
                'python3', str(logger_script), '--json'
            ], capture_output=True, text=True, cwd=os.getcwd())
            
            if result.returncode == 0 and result.stdout:
                return json.loads(result.stdout)
    except Exception:
        pass
    
    return {}

def generate_report(logs_dir: Path, days_back: int = 7) -> str:
    """Generate a comprehensive token optimization report."""
    prompt_logs = load_prompt_logs(logs_dir, days_back)
    analysis = analyze_optimization_effectiveness(prompt_logs)
    conversation_data = load_conversation_data()
    
    report = []
    report.append("# Token Optimization Effectiveness Report")
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Analysis Period: Last {days_back} days")
    report.append("")
    
    # Summary
    report.append("## Summary")
    report.append(f"- Total prompts analyzed: {analysis['total_prompts']:,}")
    report.append(f"- Optimized prompts: {analysis['optimized_prompts']:,}")
    report.append(f"- Baseline prompts: {analysis['baseline_prompts']:,}")
    
    if conversation_data and 'total_tokens' in conversation_data:
        tokens = conversation_data['total_tokens']
        report.append(f"- Current session tokens: {tokens.get('total', 0):,}")
        
        # Estimate cost savings
        if 'comparison' in analysis and analysis['comparison']:
            savings_pct = analysis['comparison']['savings_percentage']
            estimated_token_savings = int(tokens.get('total', 0) * (savings_pct / 100))
            report.append(f"- Estimated token savings: {estimated_token_savings:,} ({savings_pct:.1f}%)")
    
    report.append("")
    
    # Optimization Performance
    if analysis['optimization_stats']:
        stats = analysis['optimization_stats']
        report.append("## Optimization Performance")
        report.append(f"- Average original prompt length: {stats['avg_original_length']:.0f} chars")
        report.append(f"- Average compressed prompt length: {stats['avg_compressed_length']:.0f} chars")
        report.append(f"- Average savings per prompt: {stats['avg_savings_per_prompt']:.1f} chars")
        report.append(f"- Overall compression ratio: {stats['compression_ratio']:.1f}%")
        report.append(f"- Simple queries detected: {stats['simple_queries']} ({stats['simple_query_rate']:.1f}%)")
        report.append("")
    
    # A/B Comparison
    if 'comparison' in analysis and analysis['comparison']:
        comp = analysis['comparison']
        report.append("## A/B Test Results")
        report.append(f"- Baseline average prompt: {comp['baseline_avg_length']:.0f} chars")
        report.append(f"- Optimized average prompt: {comp['optimized_avg_length']:.0f} chars")
        report.append(f"- **Characters saved per prompt: {comp['chars_saved_per_prompt']:.0f}**")
        report.append(f"- **Savings percentage: {comp['savings_percentage']:.1f}%**")
        report.append("")
    
    # Token Usage Breakdown
    if conversation_data and 'total_tokens' in conversation_data:
        tokens = conversation_data['total_tokens']
        report.append("## Current Session Token Usage")
        report.append(f"- Input tokens: {tokens.get('input_tokens', 0):,}")
        report.append(f"- Output tokens: {tokens.get('output_tokens', 0):,}")
        report.append(f"- Cache creation: {tokens.get('cache_creation_input_tokens', 0):,}")
        report.append(f"- Cache read: {tokens.get('cache_read_input_tokens', 0):,}")
        report.append(f"- **Total: {tokens.get('total', 0):,}**")
        
        # Estimate cost
        total_tokens = tokens.get('total', 0)
        estimated_cost = (total_tokens * 3.0) / 1_000_000  # ~$3 per 1M tokens
        report.append(f"- Estimated cost: ${estimated_cost:.6f}")
        report.append("")
    
    # Recommendations
    report.append("## Recommendations")
    
    if analysis['baseline_prompts'] == 0:
        report.append("- Run A/B testing to measure baseline vs optimized performance")
        report.append("- Use `/token-test off` to disable optimizations temporarily")
        report.append("- Use `/token-test test` for guided A/B testing")
    
    if analysis['optimization_stats'] and analysis['optimization_stats']['simple_query_rate'] > 20:
        report.append("- Consider routing simple queries to Haiku model for additional savings")
    
    if analysis['optimization_stats'] and analysis['optimization_stats']['compression_ratio'] < 5:
        report.append("- Prompt compression is minimal - consider more aggressive optimization")
    
    report.append("- Enable OpenTelemetry for detailed token tracking")
    report.append("- Monitor cache hit rates to optimize caching strategy")
    
    return '\n'.join(report)

def main():
    parser = argparse.ArgumentParser(description='Generate token optimization effectiveness report')
    parser.add_argument('--days', '-d', type=int, default=7, help='Days of logs to analyze')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    # Find logs directory
    logs_dir = Path(os.getcwd()) / "logs"
    if not logs_dir.exists():
        logs_dir = Path(os.getcwd()).parent / "logs"
        
    if not logs_dir.exists():
        print("Error: Could not find logs directory", file=sys.stderr)
        sys.exit(1)
    
    # Generate report
    report = generate_report(logs_dir, args.days)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main()