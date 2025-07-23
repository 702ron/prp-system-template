# User Authentication System - Product Requirement Prompt

## Overview

Implement a complete user authentication system with login, registration, password reset, and session management for a React TypeScript application using Supabase as the backend.

## Requirements

### Functional Requirements

- [ ] User registration with email/password
- [ ] User login with email/password
- [ ] Password reset functionality
- [ ] Email verification for new accounts
- [ ] Session management and persistence
- [ ] Protected routes for authenticated users
- [ ] User profile management
- [ ] Logout functionality

### Non-Functional Requirements

- Performance: Authentication should complete within 2 seconds
- Security: Passwords must be hashed, JWT tokens for sessions
- Accessibility: WCAG 2.1 AA compliance for all auth forms
- Mobile: Responsive design for mobile devices

## Technical Specifications

### Technology Stack

- Frontend: React with TypeScript
- Backend: Supabase (Auth, Database)
- UI Library: Tailwind CSS
- State Management: React Context + Supabase Auth
- Routing: React Router

### Architecture Patterns

- State Management: Context API for auth state
- API Patterns: Supabase client for auth operations
- Database Patterns: Supabase Auth with PostgreSQL
- Component Patterns: Custom hooks for auth logic

## All Needed Context

### AI Documentation (Recommended)

- **file**: PRPs/ai_docs/react-typescript-conventions.md
  **why**: Component structure, TypeScript patterns, and React best practices
- **file**: PRPs/ai_docs/supabase-patterns.md
  **why**: Supabase authentication patterns, database operations, and client setup

### Project Files

- **file**: src/App.tsx
  **why**: Main application component where auth context will be provided
- **file**: src/components/auth/
  **why**: Directory where auth components will be created
- **file**: src/hooks/useAuth.ts
  **why**: Custom hook for authentication logic

### External Documentation

- **url**: https://supabase.com/docs/guides/auth
  **why**: Supabase authentication setup and configuration
- **url**: https://reactrouter.com/docs/en/v6
  **why**: React Router setup for protected routes

## Implementation Notes

### Critical Requirements

- [ ] CRITICAL: Implement proper error handling for all auth operations
- [ ] CRITICAL: Ensure secure password validation and storage
- [ ] IMPORTANT: Create reusable auth components for consistency
- [ ] IMPORTANT: Implement proper loading states for better UX
- [ ] NOTE: Use TypeScript interfaces for all auth-related data

### Implementation Steps

1. Set up Supabase client configuration
2. Create authentication context and provider
3. Implement custom useAuth hook
4. Create auth components (Login, Register, ResetPassword)
5. Set up protected route wrapper
6. Implement user profile management
7. Add proper error handling and loading states
8. Test all authentication flows

## Expected Output

### Code Quality Standards

- [ ] Follows project TypeScript conventions
- [ ] Implements proper error handling with user-friendly messages
- [ ] Includes comprehensive testing for auth flows
- [ ] Follows accessibility guidelines (ARIA labels, keyboard navigation)
- [ ] Uses proper TypeScript interfaces and types

### Deliverables

- [ ] Authentication context and provider
- [ ] Custom useAuth hook with all auth operations
- [ ] Login, Register, and ResetPassword components
- [ ] ProtectedRoute component for route protection
- [ ] User profile management component
- [ ] TypeScript interfaces for auth data
- [ ] Error handling utilities
- [ ] Unit tests for auth logic

## Success Criteria

- [ ] Users can register, login, and logout successfully
- [ ] Password reset functionality works end-to-end
- [ ] Protected routes redirect unauthenticated users
- [ ] Session persists across browser refreshes
- [ ] All forms are accessible and mobile-responsive
- [ ] Error messages are clear and user-friendly
- [ ] Loading states provide good user feedback
- [ ] TypeScript compilation passes without errors
