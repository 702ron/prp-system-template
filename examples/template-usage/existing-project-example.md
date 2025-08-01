# Existing Project Example

This example shows how to integrate the PRP System Template into an existing Python Django project.

## 🎯 Scenario

You have an existing Django REST API project and want to:
- Add the PRP system for structured feature development
- Implement token optimization to reduce Claude costs
- Add comprehensive logging and monitoring
- Enhance the project with AI-assisted development

## 📁 Starting Point

```
existing-django-project/
├── manage.py
├── requirements.txt
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   ├── products/
│   └── orders/
└── tests/
```

## 🚀 Integration Steps

### 1. Template Integration

```bash
# Navigate to existing project
cd existing-django-project

# Copy template files
cp -r ../prp-system-template/.claude ./
cp -r ../prp-system-template/PRPs ./
cp -r ../prp-system-template/template-docs ./

# Run setup
bash .claude/scripts/one_time_setup.sh
```

### 2. Project Analysis and Configuration

```bash
# Analyze existing project structure
/analyze-project --tech-stack --structure --create-prps

# This detects Django and creates appropriate AI docs
ls PRPs/ai_docs/
# Output: django-patterns.md, drf-patterns.md, python-conventions.md
```

### 3. Customize for Django

```bash
# Review and customize Django patterns
edit PRPs/ai_docs/django-patterns.md

# Create Django-specific PRP template
cp PRPs/templates/prp_base.md PRPs/templates/prp_django.md
# Customize for Django patterns, models, views, serializers
```

### 4. Verification

```bash
# Test optimizations
/token-test status              # Should show ENABLED

# Test logging
claude-status                   # Should show session info

# Test commands
/review code apps/users/        # Should analyze Django app
```

## 🎯 First Enhancement: API Rate Limiting

### Create PRP

```bash
/prp-create "implement API rate limiting with Redis backend" --language python
```

**Generated PRP Preview:**
```markdown
# Goal
Implement comprehensive API rate limiting system using Redis backend with Django REST framework.

# Context
- Existing Django REST API with multiple endpoints
- Redis available for caching layer
- Need different rate limits for authenticated vs anonymous users
- Must integrate with existing authentication system

# Implementation Blueprint
1. Install django-ratelimit and redis dependencies
2. Configure Redis connection in settings
3. Create rate limiting middleware
4. Apply rate limits to ViewSets
5. Add rate limit headers to responses
6. Create monitoring dashboard for rate limit metrics

# Validation Loop
```bash
# Level 1: Syntax & Dependencies
pip install django-ratelimit redis
python manage.py check

# Level 2: Unit Tests  
python manage.py test apps.core.tests.test_rate_limiting

# Level 3: Integration Tests
curl -X GET http://localhost:8000/api/users/ -H "Authorization: Bearer $TOKEN"
# Should include X-RateLimit-* headers
```
```

### Execute PRP

```bash
# Interactive execution with validation
uv run PRPs/scripts/prp_runner.py --prp api-rate-limiting --interactive
```

**Implementation Results:**
- ✅ Redis rate limiting configured
- ✅ Different limits for user types  
- ✅ Rate limit headers added
- ✅ Monitoring dashboard created
- ✅ All tests passing

## 📊 Token Usage Analysis

### Before Optimization (Baseline)

```bash
# Measure baseline usage
/token-test off
# Work session: Adding rate limiting feature
# - Read 15 Django files: 3,200 tokens
# - Run 8 commands: 1,100 tokens  
# - Context building: 1,800 tokens
# Total: 6,100 tokens
```

### After Optimization

```bash
# Enable optimizations  
/token-test on
# Same work session: Adding rate limiting feature
# - Read 15 Django files: 1,280 tokens (60% cached)
# - Run 8 commands: 440 tokens (60% cached)
# - Context building: 720 tokens (60% compressed)
# Total: 2,440 tokens (60% savings)
```

### Savings Breakdown

| Operation | Before | After | Savings |
|-----------|--------|-------|---------|
| File reads | 3,200 | 1,280 | 60% |
| Commands | 1,100 | 440 | 60% |
| Context | 1,800 | 720 | 60% |
| **Total** | **6,100** | **2,440** | **60%** |

## 🔄 Ongoing Development Workflow

### Feature Development

```bash
# Create feature branch
/new-dev-branch --type feature --name websocket-notifications

# Create comprehensive PRP
/prp-create "real-time notifications with WebSocket and Celery" --language python

# Execute with validation
uv run PRPs/scripts/prp_runner.py --prp websocket-notifications --interactive

# Review implementation
/review code apps/notifications/ python performance

# Create PR
/create-pr --title "Add real-time notification system"
```

### Code Quality Workflow

```bash
# Regular code reviews
/review build python django
/review changes

# Debug issues
/debug-RCA --issue "WebSocket connection drops"

# Refactor when needed  
/refactor-component NotificationManager --extract-services
```

### Monitoring and Analytics

```bash
# Daily usage check
claude-tokens

# Weekly session archive
claude-archive "Added notification system and payment webhooks"

# Monthly usage analysis
bash .claude/scripts/token_comparison_report.py --days 30
```

## 📈 Results After 3 Months

### Development Metrics
- **18 features** implemented using PRPs
- **92% first-pass success rate** (vs 65% previously)
- **50% faster** feature delivery
- **Zero production bugs** from PRP-implemented features

### Cost Metrics
- **Baseline costs**: $450/month
- **Optimized costs**: $180/month (60% savings)
- **Annual savings**: $3,240

### Code Quality Metrics
- **100% test coverage** for new PRP features
- **Comprehensive documentation** for all enhancements
- **Consistent Django patterns** across team
- **Security best practices** built into all PRPs

### Team Benefits
- **Faster onboarding**: New developers productive in 2 days vs 2 weeks
- **Knowledge sharing**: PRPs serve as feature specifications and documentation
- **Consistent quality**: Standardized patterns prevent common mistakes
- **Reduced debugging**: Validation loops catch issues early

## 🎯 Key Integration Patterns

### 1. Respect Existing Structure
```bash
# Don't disrupt existing patterns
# Enhance with PRPs rather than replace
/analyze-project --enhance-existing
```

### 2. Gradual Enhancement
```bash
# Start with high-impact, low-risk features
# Build confidence with the PRP system
# Expand usage as team adopts patterns
```

### 3. Team Training
```bash
# Create onboarding materials
/onboarding --team django-developers --prp-system

# Document new workflows
# Share success stories and metrics
```

### 4. Continuous Improvement
```bash
# Regular optimization reviews
/token-test test

# Refine PRPs based on outcomes
# Update ai_docs with learned patterns
```

## 📁 Final Enhanced Structure

```
existing-django-project/
├── .claude/                    # Template system (new)
│   ├── commands/              # Development commands
│   ├── hooks/                 # Optimization hooks
│   └── scripts/               # Automation scripts
├── PRPs/                      # Feature specifications (new)
│   ├── api-rate-limiting.md   # Rate limiting PRP
│   ├── websocket-notifications.md # Notifications PRP
│   └── ai_docs/
│       ├── django-patterns.md # Django-specific patterns
│       └── drf-patterns.md    # DRF patterns
├── logs/                      # Usage analytics (new)
├── template-docs/             # Template documentation (new)
├── manage.py                  # Existing Django files
├── requirements.txt
├── myproject/
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── notifications/         # New: WebSocket notifications
│   └── core/                  # New: Rate limiting middleware
└── tests/
    └── integration/           # New: PRP validation tests
```

---

**🎉 Success!** The existing Django project is now enhanced with structured AI-assisted development, comprehensive logging, and significant cost optimizations while maintaining all existing functionality.