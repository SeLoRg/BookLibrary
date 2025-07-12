from fastapi import FastAPI

app = FastAPI()
app = FastAPI(
    title="LibraryBook",
    description="API documentation for library_book",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",  # Путь для Swagger UI
    redoc_url="/api/redoc",  # Путь для Redoc UI
)
