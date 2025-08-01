# Smart Git Conflict Resolver

Perform intelligent merge conflict resolution with deep codebase understanding and agent-powered analysis. Supports both general conflict resolution and specific file/conflict targeting.

## Arguments: $ARGUMENTS

### Resolution Strategy:
- **General**: Resolve all conflicts automatically with intelligent decision-making
- **Specific**: Target specific files or conflict types mentioned in arguments
- **Safe**: Conservative approach, ask for guidance on complex conflicts
- **Aggressive**: Make best judgment calls on all conflicts
- **Agent-powered**: Use specialized agents for complex analysis (default)

Perform an intelligent merge conflict resolution with deep understanding of our codebase.

## Pre-resolution Analysis with Agent Support:

1. **Branch Analysis with Context Understanding**:
   ```bash
   git log --oneline origin/main..HEAD
   git log --oneline HEAD..origin/main
   git status
   ```

2. **GitHub Integration and PR Context**:
   ```bash
   gh pr list --state open
   gh pr view --json files,additions,deletions
   git log --grep="fix" --grep="feat" --oneline -20
   ```

3. **Agent-Powered Conflict Analysis**:
   - Use **debugger agent** for complex conflict investigation
   - Use **code-quality-analyzer agent** for merge quality assessment
   - Use **security-auditor agent** for security-sensitive conflicts

4. **Conflict Classification**:
   - Feature vs Feature conflicts
   - Fix vs Refactor conflicts  
   - Documentation conflicts
   - Configuration conflicts
   - Lock file conflicts

5. **Strategic Planning**: Think hard about findings and plan agent-assisted resolution

## Resolution strategy:

### For different file types:

**Source code conflicts (.js, .ts, .py, etc.)**:
- Understand the business logic of both changes
- Merge both features if they're complementary
- If conflicting, check which has better test coverage
- Look for related files that might need updates

**Test file conflicts**:
- Usually merge both sets of tests
- Ensure no duplicate test names
- Update test descriptions if needed

**Configuration files**:
- package.json: Merge dependencies, scripts
- .env.example: Include all new variables
- CI/CD configs: Merge all jobs unless duplicate

**Documentation conflicts**:
- Merge both documentation updates
- Ensure consistency in terminology
- Update table of contents if needed

**Lock files (package-lock.json, poetry.lock)**:
- Delete and regenerate after resolving package.json/pyproject.toml

## Post-resolution Verification with Agent Support:

1. **Automated Quality Checks**:
   ```bash
   # Linting and style
   npm run lint || ruff check --fix || echo "No linter configured"
   
   # Type checking
   npm run typecheck || mypy . || echo "No type checker configured"
   
   # Testing
   npm test || pytest || echo "No tests configured"
   ```

2. **Agent-Powered Verification**:
   - **code-quality-analyzer**: Comprehensive merge quality assessment
   - **test-strategist**: Ensure test coverage maintained after merge
   - **security-auditor**: Security implications of merged changes
   - **performance-optimizer**: Performance impact analysis

3. **Semantic Conflict Detection**:
   - Check for code that merges cleanly but breaks functionality
   - Verify API compatibility
   - Ensure no debugging code remains
   - Validate integration points

4. **Automated Fix Application**:
   - Use agents to automatically fix common post-merge issues
   - Apply consistent code formatting
   - Update import statements and dependencies

## Final Steps with Completion Summary:

1. **Resolution Documentation**:
   - Create detailed summary of all resolutions made
   - Document decision rationale for complex conflicts
   - Mark uncertain resolutions with TODO comments
   - Log agent assistance and automated fixes applied

2. **Testing Recommendations**:
   - Suggest additional testing based on conflict complexity
   - Identify integration test scenarios
   - Recommend regression testing areas

3. **File Staging and Commit Preparation**:
   ```bash
   git add -A  # Stage all resolved files
   git status  # Verify staging
   ```

4. **Audio Completion Summary** (if requested):
   - Use **work-completion-summary agent** for audio feedback
   - Provide concise summary of conflicts resolved
   - Suggest next steps for validation

## Execution Instructions:

Begin by analyzing the current conflict situation with git status and understanding both branches. Use agent integration based on conflict complexity and resolution strategy specified in arguments.

### Agent Usage Guidelines:
- **Simple conflicts**: Direct resolution without agents
- **Complex logic conflicts**: Use debugger and code-quality-analyzer agents
- **Security-sensitive files**: Always use security-auditor agent
- **Performance-critical code**: Use performance-optimizer agent
- **Large-scale conflicts**: Coordinate multiple agents for parallel resolution

## Consolidation Notes

### Replaces These Commands:
- `git-operations/conflict-resolver-general.md` → `smart-resolver` (general conflicts)
- `git-operations/conflict-resolver-specific.md` → `smart-resolver [specific files]` (targeted conflicts)

### Agent Integration Benefits:
- **Intelligent Analysis**: Uses debugger agent for complex conflict investigation
- **Quality Assurance**: Continuous quality monitoring during resolution
- **Security Focus**: Automatic security analysis for sensitive file conflicts
- **Performance Awareness**: Performance impact analysis during merge resolution
- **Automated Fixes**: Agents can apply common post-merge fixes automatically
- **Audio Summaries**: Completion feedback for complex resolution workflows

### Enhanced Capabilities:
- **Multi-Strategy Support**: Handles general, specific, safe, and aggressive resolution strategies
- **GitHub Integration**: Deep PR and issue context understanding
- **Agent Coordination**: Multiple agents work together for comprehensive resolution
- **Automated Verification**: Post-merge quality, security, and performance validation
- **Documentation**: Detailed resolution logging and decision rationale
- **Semantic Conflict Detection**: Identifies code that merges cleanly but breaks functionality

### Resolution Strategy by Conflict Type:
- **Feature conflicts**: Agent-assisted logic merging with quality validation
- **Configuration conflicts**: Intelligent merging with dependency analysis
- **Test conflicts**: Test-strategist agent ensures comprehensive coverage
- **Documentation conflicts**: Consistent terminology and structure maintenance
- **Lock file conflicts**: Automated regeneration with dependency validation

This unified resolver provides comprehensive conflict resolution capabilities while reducing command complexity from 3 commands to 1.