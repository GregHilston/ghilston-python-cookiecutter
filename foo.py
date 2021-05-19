"""Example source code file"""

import logging

from ghilston_python_cookiecutter.utils.setup_logging import setup_logging
from ghilston_python_cookiecutter.bar.bar import example

setup_logging()
logger = logging.getLogger(__name__)


def foo():
    """Demonstrates calling a local package's module's function"""
    return example()


if __name__ == "__main__":
    message = foo()
    logger.info(message)
