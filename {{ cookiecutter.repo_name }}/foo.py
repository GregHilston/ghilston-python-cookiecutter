"""Example source code file that leverages our module code"""

import logging

from {{ cookiecutter.repo_name }}.utils.setup_logging import setup_logging
from {{ cookiecutter.repo_name }}.bar.bar import example


setup_logging()
logger = logging.getLogger(__name__)


def foo() -> str:
    """Demonstrates calling a local package's module's function

    Returns:
        Example message
    """
    return example()


if __name__ == "__main__":
    message = foo()
    logger.info(message)

