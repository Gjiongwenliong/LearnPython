# LearnPython
This repository goals at my learning pace of Python steady and calm

## Automated Quality Controls

This repository uses GitHub Actions to automatically control and validate file changes:

### Python Code Quality Check
- **Triggers**: Runs on push and pull requests when `.py` files are modified
- **Checks**:
  - Python syntax errors and undefined names (flake8)
  - Code style and complexity (flake8)
  - Code formatting compliance (black)

### File Edition Control
- **Triggers**: Runs on all push and pull requests
- **Checks**:
  - Large files detection (> 10MB)
  - Sensitive files detection (credentials, keys, etc.)
  - File encoding validation (UTF-8)
  - File permissions check
  - File change summary

These automated checks ensure code quality and security standards are maintained with every update.
