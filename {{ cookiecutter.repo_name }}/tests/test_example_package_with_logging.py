import pytest

from .context import sample
from sample import example_module_with_logging


def test_example_package():
    """Demonstrates how to test our package's module"""
    assert example_module_with_logging.example_function_with_logging() == "example function"
