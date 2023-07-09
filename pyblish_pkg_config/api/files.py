from fastapi import APIRouter, Request
from typing import Optional
from ..response import success, fail
from ..models import TemplateFiles
from ..schemas import project, files

FileApi = APIRouter(prefix="/files", tags=[u"文件模块"])


@FileApi.get("/", summary=u"获取全部文件列表")
async def get_all_Filse() -> dict:
    return success(data=list(await TemplateFiles.filter(status=1).all()))


@FileApi.post("/", summary=u"添加文件")
async def get_all_Filse(post: files.AddFiles) -> dict:
    pass

