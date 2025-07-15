from src.backend.common.logging.logger import logger


def log_route(fn):
    async def wrapper(*args, **kwargs):
        logger.info(f"Calling {fn.__name__}")
        return await fn(*args, **kwargs)

    return wrapper
