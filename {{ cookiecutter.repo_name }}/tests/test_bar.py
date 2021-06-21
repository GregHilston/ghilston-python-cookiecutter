"""Example test code"""

from {{ cookiecutter.repo_name }}.bar.bar import example


def test_bar():
    """Demonstrates how to test our package source code"""
    assert example() == "bar"
