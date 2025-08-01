# Execute PRP

Implement a feature using any PRP file (BASE, SPEC, TASK, or PLANNING). Supports all PRP types with intelligent agent integration and comprehensive validation.

## PRP File: $ARGUMENTS

## Execution Process

1. **Load and Analyze PRP**
   - Read the specified PRP file and detect its type (BASE, SPEC, TASK, PLANNING)
   - Understand all context and requirements specific to PRP type
   - Follow all instructions in the PRP and extend research if needed
   - Ensure comprehensive context for implementation success
   - Perform additional web searches and codebase exploration as needed

2. **ULTRATHINK with Agent Integration**
   - Perform comprehensive planning addressing all PRP requirements
   - Break down the PRP into clear todos using the TodoWrite tool
   - **Agent Spawning**: Use specialized agents and subagents to enhance the process
   - **Context Sharing**: Ensure all subagents read the PRP and understand its context
   - **Pattern Discovery**: Identify implementation patterns from existing code
   - **Validation Strategy**: Plan validation approach based on PRP type
   - Never guess about imports, file names, function names - always gather real context

3. **Execute with Agent Support**
   - **Implementation**: Execute the PRP step by step with agent assistance
   - **Code Generation**: Implement all required code following PRP specifications
   - **Agent Coordination**: Use specialized agents for complex tasks (backend-developer, frontend-developer, etc.)
   - **Quality Assurance**: Apply code-quality-analyzer agent for continuous quality checks
   - **Security Review**: Use security-auditor agent for security-critical implementations

4. **Comprehensive Validation**
   - **Syntax/Style**: Run linting and type checking validation gates
   - **Unit Tests**: Execute all test suites with proper coverage
   - **Integration Tests**: Validate system integration points
   - **Performance Tests**: Run performance validation where applicable
   - **Security Tests**: Execute security validation gates
   - **Iterative Fixing**: Fix failures and re-run until all validation passes
   - **PRP Compliance**: Re-read PRP to ensure full requirement compliance

5. **Completion with Summary**
   - **Checklist Verification**: Ensure all PRP checklist items are completed
   - **Final Validation**: Run complete validation suite one final time
   - **Documentation**: Update any required documentation
   - **Audio Summary**: Generate completion summary using work-completion-summary agent
   - **Status Report**: Provide detailed completion status and metrics

6. **PRP Reference and Feedback Loop**
   - **Continuous Validation**: Reference PRP throughout execution for alignment
   - **Confidence Scoring**: Evaluate implementation success against PRP confidence score
   - **Feedback Integration**: Use findings to improve future PRP execution

## Agent Integration Strategy

### Specialized Agent Usage:
- **backend-developer**: For API, database, and server-side implementations
- **frontend-developer**: For UI, components, and client-side features
- **test-strategist**: For comprehensive testing implementation
- **security-auditor**: For security-critical features and vulnerability assessment
- **performance-optimizer**: For performance-critical implementations
- **code-quality-analyzer**: For continuous code quality monitoring
- **work-completion-summary**: For audio summaries and workflow continuity

### Agent Coordination:
1. **Parallel Execution**: Multiple agents work simultaneously on different aspects
2. **Context Sharing**: All agents maintain shared understanding of PRP requirements
3. **Quality Gates**: Agents validate each other's work through integrated quality checks
4. **Feedback Loops**: Continuous improvement through inter-agent communication

Note: If validation fails, use error patterns in PRP to fix and retry. Agents provide specialized debugging and optimization assistance.

## Consolidation Notes

### Replaces These Commands:
- `PRPs/prp-base-execute.md` → `prp-execute` (any BASE PRP)
- `PRPs/prp-spec-execute.md` → `prp-execute` (SPEC PRPs)
- `PRPs/prp-task-execute.md` → `prp-execute` (TASK PRPs)
- `typescript/TS-execute-base-prp.md` → `prp-execute` (TypeScript PRPs)

### Agent Integration Benefits:
- **Specialized Execution**: Uses appropriate agents based on PRP type and requirements
- **Parallel Processing**: Multiple agents work simultaneously on different implementation aspects
- **Quality Assurance**: Continuous quality monitoring through code-quality-analyzer agent
- **Security Focus**: Automatic security analysis for security-critical features
- **Performance Optimization**: Performance analysis and optimization during implementation
- **Audio Feedback**: Completion summaries for better workflow integration

### Enhanced Execution Capabilities:
- **PRP Type Detection**: Automatically adapts execution strategy based on PRP type
- **Agent Coordination**: Intelligent agent selection and coordination for optimal results
- **Comprehensive Validation**: Multi-layered validation including syntax, tests, security, performance
- **Context Preservation**: Maintains PRP context throughout the entire execution process
- **Feedback Loops**: Continuous improvement through agent communication and validation
- **Documentation Integration**: Automatic documentation updates and maintenance

### Execution Strategy by PRP Type:
- **BASE PRPs**: Full agent integration with comprehensive validation
- **SPEC PRPs**: Focused implementation with specification compliance checking
- **TASK PRPs**: Targeted task execution with minimal overhead
- **PLANNING PRPs**: Architecture-focused execution with system-architect agent integration

This unified execution command provides comprehensive PRP implementation capabilities while reducing command complexity from 4 commands to 1.
