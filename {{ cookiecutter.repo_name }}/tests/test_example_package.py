import pytest

from .context import sample
from sample import example_module


def test_example_package():
    """Demonstrates how to test our package's module"""
    assert example_module.example_function() == "example function"
