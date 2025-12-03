# LLM Playground - Backend

Backend service for experimenting with Large Language Models.

## Installation

### Prerequisites

- Python 3.13.3 or higher
- pip (Python package installer)

### Setup Instructions

1. **Navigate to backend directory**

   ```bash
   cd backend
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   # Install production dependencies
   make install
   # or: pip install -e .

   # Install with development dependencies
   make install-dev
   # or: pip install -e ".[dev]"
   ```

## Usage

### Run the application

```bash
# Using make
make run
```

## Development

### Installing Development Dependencies

```bash
make install-dev
```

### Running Tests

```bash
make test
# or
pytest
```

### Code Formatting

```bash
make format
# This runs:
# - black src/ tests/
# - isort src/ tests/
```

### Linting

```bash
make lint
# This runs:
# - flake8 src/ tests/
# - pylint src/ tests/
```

### Type Checking

```bash
make type-check
# This runs:
# - mypy src/
```

### Run All Checks

```bash
make all
# Runs: format, lint, type-check, and test
```

## Dependency Management

This project uses **`pyproject.toml`** for all dependency management (PEP 518 - modern standard).

### Adding New Dependencies

Edit `pyproject.toml`:

**Production dependencies:**

```toml
[project]
dependencies = [
    "requests>=2.31.0",
    "your-new-package>=1.0.0",
]
```

**Development dependencies:**

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "your-dev-tool>=1.0.0",
]
```

Then reinstall:

```bash
pip install -e .           # For production dependencies
pip install -e ".[dev]"    # For dev dependencies
```

### Updating Dependencies

```bash
# Reinstall with latest versions
pip install --upgrade -e ".[dev]"

# Update specific package
pip install --upgrade package-name
```

## Project Configuration

The project uses **`pyproject.toml`** as the single source of truth for:

- Project metadata (name, version, authors)
- Production dependencies (`[project.dependencies]`)
- Development dependencies (`[project.optional-dependencies]`)
- Tool configurations (black, pytest, mypy, isort, pylint)

## Environment Variables

Create a `.env` file in the backend directory:

```env
# API Keys
OPENAI_API_KEY=your_api_key_here
ANTHROPIC_API_KEY=your_api_key_here

# Application Settings
DEBUG=False
LOG_LEVEL=INFO
```
