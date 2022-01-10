"""Example module that leverages one of our own modules"""

from loguru import logger

from sample import example_module_to_import


def example_function_with_logging() -> str:
    """Example function leveraging one of our own packages.

    Returns:
        Hard coded message
    """
    message = example_module_to_import.example_function_to_import()
    logger.info(message)
    return message
