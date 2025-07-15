# src/backend/common/logger.py
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
