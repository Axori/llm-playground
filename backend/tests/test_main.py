"""
Tests for the main module
"""

import pytest
from src.main import main


def test_main_runs_without_error() -> None:
    """Test that main function runs without errors."""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")
