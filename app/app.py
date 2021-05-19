"""Example source code file"""

import logging
from logging.config import fileConfig

fileConfig("logging_config.ini")
logger = logging.getLogger(__name__)


def example() -> str:
    """Example function

    Provided purely as an example and should be deleted

    :return: hard coded string
    """
    logger.info("example log message")
    print("bar")
    return "bar"


if __name__ == "__main__":
    example()
