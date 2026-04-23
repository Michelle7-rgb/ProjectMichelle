# Contributing Guide

Thank you for your interest in contributing to Logement!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch for your changes

## Code Standards

### Python
- Follow PEP 8
- Use type hints when appropriate
- Add docstrings to all functions and classes
- Write descriptive commit messages

### Django
- Use Django ORM exclusively
- Implement permission checks on sensitive views
- Optimize queries with select_related() and prefetch_related()
- Test all views and models

### Templates
- Use semantic HTML5
- Keep templates DRY with extends and includes
- Add comments for complex logic
- Ensure mobile responsiveness

## Testing

Before submitting a PR:
```bash
python manage.py test
python manage.py check
python manage.py makemigrations --check
```

## Pull Request Process

1. Ensure code follows our standards
2. Update README.md if needed
3. Write a clear PR description
4. Link related issues
5. Request review from maintainers

## Reporting Issues

- Use descriptive titles
- Include reproduction steps
- Specify your environment
- Attach screenshots if relevant

## Code Review

PRs will be reviewed for:
- Code quality and style
- Security implications
- Performance considerations
- Compatibility with existing code
- Test coverage

Thank you for helping make Logement better!
