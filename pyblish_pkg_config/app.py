import os
from fastapi import FastAPI, Request
from tortoise.contrib.fastapi import register_tortoise
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from .config import DB_ORM_CONFIG
from .sys_events import startup, stopping
from .router import all_api_router, open_dev_doc

_root: str = os.getcwd().replace("\\", "/")


def main() -> FastAPI:
    is_debug = os.getenv("APP_DEBUG") == "True" or False
    application = FastAPI(
        debug=is_debug,
        docs_url=None,
        redoc_url=None,
    )

    # event listeners
    application.add_event_handler("startup", startup(application))
    application.add_event_handler("shutdown", stopping(application))

    application.include_router(all_api_router)
    if os.getenv("APP_DEBUG") == "True":
        open_dev_doc(application)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Static resource directory
    application.mount('/', StaticFiles(directory=f"{_root}/public"), name="public")
    application.mount('/build/', StaticFiles(directory=f"{_root}/static_files/build"), name="build")

    register_tortoise(application, config=DB_ORM_CONFIG, generate_schemas=is_debug, add_exception_handlers=True)

    return application

