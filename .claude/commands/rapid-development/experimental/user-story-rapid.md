# Analyze User Story and Create Implementation Plan

Agent-powered rapid analysis and implementation planning for user stories with specialized backend/frontend coordination.

User Story: $ARGUMENTS

## Task: Create detailed implementation plan for separate backend and frontend projects with agent-powered analysis

**Agent Integration**: Use specialized agents for comprehensive planning:
- `api-designer` agent for API contract design and specification
- `backend-developer` agent for Java/Spring implementation strategy
- `frontend-developer` agent for React/TypeScript implementation strategy
- `test-strategist` agent for comprehensive testing approach
- `work-completion-summary` agent for audio progress updates

1. **Parse user story**:
   - Extract: As a [user], I want [feature], so that [benefit]
   - List explicit and implicit acceptance criteria
   - Identify non-functional requirements (performance, security, UX)
   - Define success metrics

2. **Plan API contract first** (backend/frontend agreement):
   ```yaml
   Endpoints:
     - GET /api/v1/{resources} - List with pagination
     - GET /api/v1/{resources}/{id} - Get single resource
     - POST /api/v1/{resources} - Create new
     - PUT /api/v1/{resources}/{id} - Update existing
     - DELETE /api/v1/{resources}/{id} - Delete
   
   DTOs:
     Request: {field validations}
     Response: {field types}
     Error: {standard error format}
   ```

3. **Backend implementation plan** (Java project):
   ```
   Package structure:
   com.company.feature/
   ├── controller/
   ├── service/
   ├── repository/
   ├── entity/
   ├── dto/
   ├── exception/
   └── mapper/
   ```
   
   Implementation order:
   1. Entity with JPA annotations
   2. Repository interface
   3. DTOs with validation
   4. Mapper interface
   5. Service with business logic
   6. Controller with OpenAPI
   7. Exception handling
   8. Integration tests

4. **Frontend implementation plan** (React project):
   ```
   src/features/{feature}/
   ├── api/          # API client functions
   ├── components/   # UI components
   ├── hooks/        # Custom hooks
   ├── schemas/      # Zod validation
   ├── types/        # TypeScript types
   ├── __tests__/    # Component tests
   └── index.ts      # Public exports
   ```
   
   Implementation order:
   1. Zod schemas matching backend DTOs
   2. TypeScript types
   3. API client functions
   4. Custom hooks with TanStack Query
   5. UI components
   6. Forms with validation
   7. Error handling
   8. Component tests

5. **Integration plan**:
   - CORS configuration on backend
   - Environment variables for API URL
   - Error response handling
   - Loading states
   - Optimistic updates where applicable

6. **Validation commands**:
   ```bash
   # Backend (in Java project)
   ./gradlew clean build test
   
   # Frontend (in React project)
   npm run type-check && npm run lint && npm run test:coverage
   
   # Integration (manual or e2e)
   - Start backend: ./gradlew bootRun
   - Start frontend: npm run dev
   - Test full user flow
   ```

7. **Risk mitigation**:
   - Start with API contract agreement
   - Use API mocking in frontend if backend delayed
   - Implement health check endpoint
   - Add request/response logging
   - Plan for error scenarios

Save this plan as: `PRPs/implementations/{feature}-plan.md`

## Agent Integration Workflow

### Phase 1: Story Analysis with Agent Support
1. **User Story Parsing**: Extract requirements, acceptance criteria, and success metrics
2. **llm-ai-agents-and-eng-research**: Gather latest best practices for similar implementations
3. **Requirements Validation**: Ensure completeness and identify missing elements

### Phase 2: API Contract Design with API Designer Agent
1. **Spawn api-designer agent** for comprehensive API specification:
   - RESTful endpoint design with proper HTTP methods
   - OpenAPI 3.0 specification generation
   - DTO design with validation constraints
   - Error response standardization
   - API versioning strategy

### Phase 3: Backend Implementation Planning with Backend Developer Agent
1. **Spawn backend-developer agent** for Java/Spring implementation:
   - Package structure optimization
   - Entity design with JPA best practices
   - Service layer architecture
   - Repository pattern implementation
   - Exception handling strategy
   - Integration testing approach

### Phase 4: Frontend Implementation Planning with Frontend Developer Agent
1. **Spawn frontend-developer agent** for React/TypeScript implementation:
   - Component architecture design
   - State management strategy (Context/Redux/Zustand)
   - Type-safe API client generation
   - Form validation with Zod schemas
   - Error boundary implementation
   - Testing strategy with React Testing Library

### Phase 5: Testing Strategy with Test Strategist Agent
1. **Spawn test-strategist agent** for comprehensive testing approach:
   - Unit testing strategy for both backend and frontend
   - Integration testing for API endpoints
   - E2E testing for user workflows
   - Test coverage requirements and monitoring
   - Continuous integration testing pipeline

### Phase 6: Integration and Coordination
1. **Cross-team Coordination**: Ensure backend/frontend alignment
2. **Environment Configuration**: Development, staging, production setup
3. **CORS and Security**: Proper security configuration
4. **Deployment Strategy**: Container and orchestration planning

### Phase 7: Completion Summary
1. **work-completion-summary agent**: Generate audio summary of implementation plan
2. **Next Steps**: Clear handoff instructions for development teams
3. **Success Metrics**: Measurable criteria for implementation success

## Enhanced Implementation Benefits

### Agent-Powered Planning:
- **Specialized Expertise**: Each agent brings domain-specific knowledge
- **Latest Best Practices**: Incorporates cutting-edge development patterns
- **Comprehensive Coverage**: Ensures no critical aspects are missed
- **Quality Assurance**: Built-in validation and cross-checking
- **Audio Feedback**: Progress updates and completion summaries

### Team Coordination:
- **Clear API Contracts**: Eliminates backend/frontend integration issues
- **Parallel Development**: Teams can work independently with confidence
- **Risk Mitigation**: Proactive identification and resolution of potential issues
- **Testing Strategy**: Comprehensive testing approach from day one
- **Documentation**: Auto-generated specifications and implementation guides

### Development Velocity:
- **Reduced Planning Time**: Automated analysis and planning generation
- **Fewer Integration Issues**: Clear contracts and interfaces defined upfront
- **Better Code Quality**: Best practices baked into the implementation plan
- **Faster Debugging**: Structured error handling and logging strategies
- **Scalable Architecture**: Future-proof design patterns and practices

This enhanced user story analysis provides enterprise-grade implementation planning with agent-powered expertise and coordination.