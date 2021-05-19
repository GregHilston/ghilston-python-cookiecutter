"""Example source code file"""

import logging

from ghilston_python_cookiecutter.utils.setup_logging import setup_logging
from ghilston_python_cookiecutter.bar.bar import example

setup_logging()
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    message = example()
    logger.info(message)
