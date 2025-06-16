import logging
import logging.config

from app.core.config import settings

logger = logging.getLogger("intern")

def init_logging() -> None:
    """Initialize logging configuration."""
    logger.setLevel(logging.DEBUG)
    logging.config.dictConfig(settings.LOGGING_CONFIG)
    logger.debug("Logger initialized")