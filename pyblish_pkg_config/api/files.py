from fastapi import APIRouter, Request
from typing import Optional
from ..response import success, fail
from ..models import TemplateFiles, TemplateContent
from ..schemas import project, files

FileApi = APIRouter(prefix="/files", tags=[u"文件模块"])


@FileApi.get("/", summary=u"获取全部文件列表")
async def get_all_Filse() -> dict:
    return success(data=list(await TemplateFiles.filter(status=1).all()))


@FileApi.post("/", summary=u"添加新文件")
async def add_new_Filse(post: files.AddFiles) -> dict:
    if await TemplateFiles.filter(name=post.name).exists():
        return fail(code=10101, msg=u'当前名已被占用')
    await TemplateFiles.create(**post.dict())
    return success()


@FileApi.post("/content/{file_id}", summary=u"添加脚本内容")
async def add_content(file_id: int, post: files.AddFileContent) -> dict:
    if await TemplateFiles.filter(id=file_id).exists():
        return fail(code=1002, msg=u'当前文件的不存在')
    
    if await TemplateContent.filter(template_id=file_id).exists():
        return fail(code=10101, msg=u'文件已经存在')

    await TemplateContent.create(**post.dict(), template_id=file_id)
    return success()

@FileApi.get("/content/{file_id}", summary=u"获取脚本内容")
async def get_content(file_id: int) -> dict:
    TemplateContent.get
    content_data = await TemplateContent.get_or_none(template_id=file_id, status=1).values("process_parameter", 
                                                                                           "process_content", 
                                                                                           "repair_parameter", 
                                                                                           "repair_content", 
                                                                                           "other_content")
    if not content_data:
        return fail(code=1001, msg=u"内容不存在")
    return success(data=content_data)
