# LLM Playground - Backend

Backend service for experimenting with Large Language Models.

## Installation

### Prerequisites

- Python 3.13.3 or higher
- uv (fast Python package installer) - [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

### Setup Instructions

1. **Install uv** (if not already installed)

   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Or with Homebrew
   brew install uv

   # Or with pip
   pip install uv
   ```

2. **Navigate to backend directory**

   ```bash
   cd backend
   ```

3. **Create a virtual environment** (optional - uv will create one automatically)

   ```bash
   uv venv
   source .venv/bin/activate  # uv uses .venv by default
   ```

4. **Install dependencies**

   ```bash
   # Recommended: Sync all dependencies (fastest)
   make sync
   # or: uv sync --all-extras

   # Alternative: Install production dependencies only
   make install
   # or: uv pip install -e .

   # Alternative: Install with development dependencies
   make install-dev
   # or: uv pip install -e ".[dev]"
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
# Recommended with uv
make sync

# Or install dev dependencies specifically
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

This project uses **`uv`** for fast dependency management with **`pyproject.toml`** (PEP 518 - modern standard).

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

Then sync:

```bash
make sync                  # Syncs all dependencies
# or: uv sync --all-extras

# Alternative approach
uv pip install -e .           # For production dependencies
uv pip install -e ".[dev]"    # For dev dependencies
```

### Adding Dependencies via CLI

```bash
# Add a production dependency
uv add requests

# Add a development dependency
uv add --dev pytest-asyncio

# Add with version constraint
uv add "fastapi>=0.100.0"
```

### Updating Dependencies

```bash
# Update all dependencies
uv sync --upgrade

# Update specific package
uv pip install --upgrade package-name

# Lock dependencies (creates/updates uv.lock)
uv lock
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
