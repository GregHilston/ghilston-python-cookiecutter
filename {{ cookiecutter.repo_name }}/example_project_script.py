"""Example source code file that leverages our package code"""

import logging

from sample import example_module
from sample import example_module_with_logging
from sample import example_utils_module


example_utils_module.setup_logging()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(example_module.example_function())
    logger.info(example_module_with_logging.example_function_with_logging())
