import pytest

from sample import example_module

from .context import sample


def test_example_package():
    """Demonstrates how to test our package's module"""
    assert example_module.example_function() == "example function"
