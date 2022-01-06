"""Python logging utility functions"""
import json
import logging.config
import os


def setup_logging(default_path: str = "logging.json", default_level: int = logging.INFO, env_key: str = "LOG_CFG"):
    """Sets up logging configuration

    Configures our logging in a pleasant to view output.

    Args:
        default_path: Path to logging json file. used if a valid env_key is not provided.
        default_level: Level of logging to set.
        env_key: Environment variable key that holds the path to a logging json file. This takes precedence to the
            default_path.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt", encoding="utf8") as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        logging.getLogger(__name__).warning("Unable to load logging configuration file %s", default_path)
