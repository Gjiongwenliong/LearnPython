# GitHub Actions Workflows

This document describes the automated workflows that control file editions in this repository.

## Workflows Overview

### 1. Python Code Quality Check (`python-check.yml`)

This workflow ensures all Python code meets quality standards.

**Trigger Conditions:**
- Push to `main` or `master` branch
- Pull requests targeting `main` or `master` branch
- Only runs when `.py` files are modified

**Checks Performed:**

1. **Syntax Validation (flake8)**
   - Detects Python syntax errors (E9)
   - Finds undefined names (F63, F7, F82)
   - Stops the build if critical errors are found

2. **Code Style Check (flake8)**
   - Maximum line length: 127 characters
   - Maximum cyclomatic complexity: 10
   - Provides warnings (doesn't fail the build)

3. **Code Formatting (black)**
   - Verifies code follows Black formatting standards
   - Shows diff of any formatting issues
   - Fails if formatting is incorrect

**How to Fix Issues:**
```bash
# Install tools
pip install flake8 black

# Check code style
flake8 your_file.py

# Auto-format code
black your_file.py
```

### 2. File Edition Control (`file-control.yml`)

This workflow provides comprehensive file validation for all changes.

**Trigger Conditions:**
- All push events to `main` or `master` branch
- All pull requests targeting `main` or `master` branch

**Checks Performed:**

1. **Large Files Detection**
   - Prevents files larger than 10MB
   - Helps keep repository size manageable
   - Fails the build if large files are found

2. **Sensitive Files Detection**
   - Scans for potentially sensitive files:
     - Private keys (`.pem`, `.key`)
     - Certificates (`.p12`, `.pfx`)
     - Environment files (`.env`)
     - Credential files
   - Warns if sensitive patterns are detected

3. **File Encoding Validation**
   - Ensures text files use UTF-8 encoding
   - Checks `.py`, `.md`, and `.txt` files
   - Warns about non-UTF-8 files

4. **File Permissions Check**
   - Identifies unexpected executable files
   - Shell scripts (`.sh`) are allowed
   - Warns about other executable files

5. **File Change Summary**
   - Displays statistics of changed files
   - Shows additions and deletions
   - Helps reviewers understand the scope

## Benefits

✅ **Automatic Quality Control**: Every change is automatically checked
✅ **Consistent Code Style**: Enforces formatting and style standards
✅ **Security**: Prevents accidental commit of sensitive data
✅ **Early Error Detection**: Finds issues before code review
✅ **Documentation**: Change summaries help understand modifications

## Local Development

Before pushing code, you can run the same checks locally:

```bash
# Install dependencies
pip install flake8 black

# Check Python code
flake8 .
black --check --diff .

# Auto-fix formatting
black .

# Check for large files
find . -type f -size +10M

# Check file encoding
file *.py
```

## Workflow Status

You can view workflow runs in the GitHub Actions tab of this repository. Each run shows:
- ✅ Success: All checks passed
- ❌ Failure: One or more checks failed
- ⚠️ Warning: Non-critical issues detected

## Customization

To modify workflow behavior, edit the files in `.github/workflows/`:
- `python-check.yml`: Adjust Python code quality settings
- `file-control.yml`: Customize file validation rules

## Troubleshooting

**Workflow not running?**
- Ensure you're pushing to `main` or `master` branch
- Check that the workflow file exists in `.github/workflows/`
- Verify YAML syntax is correct

**Checks failing?**
- Read the error messages in the Actions tab
- Run checks locally to reproduce issues
- Fix issues and push again

**Need help?**
- Check the workflow logs in GitHub Actions
- Review this documentation
- Consult GitHub Actions documentation: https://docs.github.com/actions
