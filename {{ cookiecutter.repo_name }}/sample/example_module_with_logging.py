"""Example module that leverages one of our own modules"""

import logging

from sample import example_utils_module

example_utils_module.setup_logging()
logger = logging.getLogger(__name__)


def example_function_with_logging() -> str:
    """Example function leveraging one of our own packages.

    Returns:
        Hard coded message
    """
    message = "example function"
    logger.info(message)
    return message