"""Example source code file that leverages our module code"""

import logging

from {{ cookiecutter.repo_name }}.example_utils_package.setup_logging_module import setup_logging
from {{ cookiecutter.repo_name }}.example_package.example_package.example_module import example_function


setup_logging()
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info(example_function)
