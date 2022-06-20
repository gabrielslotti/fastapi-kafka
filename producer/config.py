import logging
import sys
from loguru import logger
from starlette.config import Config

config = Config(".env")

PROJECT_NAME: str = config("PROJECT_NAME",
                           default="kafka-producer")
KAFKA_URI: str = config("KAFKA_URI", default="127.0.0.1")
KAFKA_PORT: str = config("KAFKA_PORT", default="9092")
KAFKA_INSTANCE = f"{KAFKA_URI}:{KAFKA_PORT}"
DEBUG: bool = config("DEBUG", cast=bool, default=False)

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO

logging.basicConfig(level=LOGGING_LEVEL)
logger.configure(handlers=[{"sink": sys.stderr,
                            "level": LOGGING_LEVEL}])
