# Contributing to Claude JSONL Converter

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

When creating a bug report, include:
- Clear title and description
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Environment information:
  - OS and version
  - Python version
  - File size (if relevant)
- Sample JSONL file (sanitize sensitive data first!)

### Suggesting Features

Feature requests are welcome! Please:
- Check if a similar request exists
- Explain the use case clearly
- Provide examples if possible
- Consider if it fits the project's scope

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Write/update tests if applicable
5. Ensure the code follows existing style
6. Commit your changes: `git commit -m 'Add some feature'`
7. Push to the branch: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/claude-jsonl-converter.git
cd claude-jsonl-converter

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the package in development mode
pip install -e .
```

## Testing

```bash
# Manual test with sample file
python jsonl_converter.py test.jsonl

# Check the output
cat test_readable.md
```

## Code Style

This project aims to follow:
- **PEP 8** guidelines for Python code
- **Type hints** where appropriate
- **Docstrings** for all public functions
- **Meaningful variable names**
- **Comments** for complex logic

## Project Structure

```
claude-jsonl-converter/
├── jsonl_converter.py      # Main converter script
├── SKILL.md                 # Claude Skill definition
├── README.md                # Project documentation
├── LICENSE                  # MIT License
├── CHANGELOG.md             # Version history
├── CONTRIBUTING.md          # This file
├── setup.py                 # Package setup
└── pyproject.toml          # Modern Python config
```

## Commit Messages

Use clear, descriptive commit messages:
- `"Add support for JSON output format"`
- `"Fix encoding issue on Windows"`
- `"Update README with installation instructions"`

Avoid:
- `"Update files"`
- `"Fix bug"`
- `"Changes"`

## Adding Features

Consider:
- Does it fit the project's goals?
- Is it generally useful or too specific?
- Does it increase dependencies?
- Can it break existing functionality?

## Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in PR comments
- Start a GitHub Discussion (if enabled)

Thank you for contributing! 🎉
