import pytest

from sample import example_module_importing_another_module

from .context import sample


def test_example_package():
    """Demonstrates how to test our package's module"""
    assert example_module_importing_another_module.example_function_with_logging() == "example_function_to_import"
