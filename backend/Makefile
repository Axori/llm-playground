.PHONY: help install install-dev clean test lint format type-check all run activate

help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make clean        - Remove build artifacts and caches"
	@echo "  make test         - Run tests with pytest"
	@echo "  make lint         - Run linters (flake8, pylint)"
	@echo "  make format       - Format code with black and isort"
	@echo "  make type-check   - Run mypy type checker"
	@echo "  make run          - Run the application"
	@echo "  make all          - Format, lint, type-check, and test"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:
	pytest

lint:
	flake8 src/ tests/
	pylint src/ tests/

format:
	black src/ tests/
	isort src/ tests/

type-check:
	mypy src/

run:
	cd src && python main.py

all: format lint type-check test
	@echo "All checks passed!"

