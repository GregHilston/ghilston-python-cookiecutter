"""Example source code file that leverages our package code"""

from loguru import logger

from sample import example_module, example_module_importing_another_module

if __name__ == "__main__":
    logger.info(example_module.example_function())
    logger.info(example_module_importing_another_module.example_function_with_logging())
