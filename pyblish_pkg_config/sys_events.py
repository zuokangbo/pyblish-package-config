from typing import Callable
from fastapi import FastAPI
from tortoise import Tortoise


def startup(app: FastAPI) -> Callable:
    async def app_start():
        print(u"启动完成")

    return app_start


def stopping(app: FastAPI) -> Callable:
    async def stop_app():
        print(u"应用停止")
        await Tortoise.close_connections()

    return stop_app

