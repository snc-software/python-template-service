import os
from dotenv import load_dotenv
import logging

load_dotenv()


def get_env_value(key: str) -> str:
    value = os.getenv(key)

    if not value:
        error = f"Missing required environment variable: {key}"
        logging.error(error)
        raise ValueError(error)
    return value


PG_HOST = get_env_value("PG_HOST")
PG_PORT = get_env_value("PG_PORT")
PG_USER = get_env_value("PG_USER")
PG_PASSWORD = get_env_value("PG_PASSWORD")
PG_DATABASE = get_env_value("PG_DATABASE")
