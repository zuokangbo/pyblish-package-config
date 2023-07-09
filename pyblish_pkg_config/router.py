from fastapi import APIRouter, FastAPI
from .api.dev_swagger_doc import custom_swagger_ui_html, redoc_html
from .api.project import ProjectApi
from .api.files import FileApi

all_router = APIRouter(prefix="/api")

all_router.include_router(ProjectApi)
all_router.include_router(FileApi)


def open_dev_doc(app: FastAPI):
    app.get("/docs", include_in_schema=False)(custom_swagger_ui_html)
    app.get("/redoc", include_in_schema=False)(redoc_html)
