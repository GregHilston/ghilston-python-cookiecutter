"""Example source code file that leverages our package code"""

import logging

from example_package import example_module
from example_package_with_logging import example_module_with_logging
from example_utils_package import example_utils_module


example_utils_module.setup_logging()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(example_module.example_function())
    logger.info(example_module_with_logging.example_function_with_logging())
