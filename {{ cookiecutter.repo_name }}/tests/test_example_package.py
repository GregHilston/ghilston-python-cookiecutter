import pytest

from example_package import example_module
from sample import example_module_with_logging


def test_example_package():
    """Demonstrates how to test our package's module"""
    assert example_module.example_function() == "example function"
