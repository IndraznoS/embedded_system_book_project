# Contributing to Embedded System Book Project

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find bugs, errors, or have suggestions:

1. Check if the issue already exists
2. Create a new issue with:
   - Clear description
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior
   - Environment details (OS, versions, etc.)

### Contributing Content

#### Book Chapters

To contribute to the book:

1. Create a new branch: `git checkout -b feature/chapter-name`
2. Add your chapter in `book/chapters/`
3. Include it in `book/main.tex`
4. Test compilation: `cd book && make pdf`
5. Submit a pull request

**Chapter Guidelines:**
- Follow existing chapter structure
- Include practical examples
- Add code listings for Arduino code
- Reference figures properly
- Use consistent terminology

#### Arduino Examples

To add Arduino examples:

1. Create directory in `arduino/examples/`
2. Include clear comments and documentation
3. Test on actual hardware if possible
4. Follow Arduino coding conventions
5. Use descriptive variable names

**Code Style:**
```cpp
// Good
const int LED_PIN = 13;
const unsigned long BLINK_INTERVAL = 1000;

// Not ideal
int p = 13;
int d = 1000;
```

#### Python Scripts

To add or improve Python tools:

1. Follow PEP 8 style guidelines
2. Include docstrings for functions
3. Add usage examples in comments
4. Update `scripts/README.md`
5. Test with various inputs

**Style Guidelines:**
- Use descriptive variable names
- Add type hints where appropriate
- Include error handling
- Write clear documentation

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** with clear messages
6. **Push** to your fork
7. **Submit** a pull request

**Commit Message Format:**
```
Short summary (50 chars or less)

Detailed explanation if needed. Explain what and why,
not how. Wrap at 72 characters.
```

### Code Review

All contributions will be reviewed for:
- Correctness and functionality
- Code quality and style
- Documentation completeness
- Test coverage (if applicable)

## Development Setup

### Prerequisites

```bash
# Install development tools
pip install black flake8 pylint  # Python tools
```

### Testing Your Changes

#### LaTeX Book
```bash
cd book
make clean
make pdf
# Check build/main.pdf for errors
```

#### Arduino Code
```bash
cd arduino
pio run  # Should compile without errors
```

#### Python Scripts
```bash
cd scripts
python -m py_compile **/*.py  # Check syntax
# Run manual tests with your changes
```

## Project Structure

```
embedded_system_book_project/
├── book/          # LaTeX documentation
├── arduino/       # PlatformIO Arduino projects
└── scripts/       # Python analysis tools
```

## Style Guidelines

### LaTeX
- Use semantic commands (e.g., `\code{}`, `\register{}`)
- Keep lines reasonably short
- One sentence per line for easier diff
- Use `\label{}` for all references

### C/C++ (Arduino)
- Follow Arduino style guide
- Use meaningful names
- Comment complex logic
- Initialize variables
- Check return values

### Python
- Follow PEP 8
- Maximum line length: 88 characters (Black default)
- Use type hints
- Write docstrings
- Handle exceptions

## Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Review existing issues and PRs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
