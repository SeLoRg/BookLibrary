from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from src.backend.common.exceptions.exceptions import ServiceError
from src.backend.common.logging.logger import logger


async def service_exception_handler(request: Request, exc: ServiceError):
    logger.warning(f"[ServiceError] {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"[DBError] {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error"},
    )


async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"[UnhandledError] {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
