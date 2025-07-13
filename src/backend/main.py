from fastapi import FastAPI
from src.backend.common.exceptions.handlers import *
from src.backend.library_catalog.app.LibraryCatalogRouter import router

app = FastAPI()
app = FastAPI(
    title="LibraryBook",
    description="API documentation for library_book",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",  # Путь для Swagger UI
    redoc_url="/api/redoc",  # Путь для Redoc UI
)
app.include_router(router)
app.add_exception_handler(ServiceError, service_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)
