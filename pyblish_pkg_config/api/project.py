from fastapi import APIRouter, Request
from typing import Optional
from ..response import success, fail
from ..models import Project, BuildVersion, ProjectSetting
from ..schemas import project

ProjectApi = APIRouter(prefix="/project", tags=[u"项目模块"])


@ProjectApi.get("/", summary=u"获取全部项目")
async def get_all_projects() -> dict:
    return success(data=list(await Project.filter(status=1).all()))


@ProjectApi.get("/build_url/{project_id}", summary=u"获取build文件的下载地址")
async def get_current_build(project_id: int) -> dict:
    project_data = await Project.get_or_none(id=project_id, status=1).values("name", "use_verison")
    if not project_data:
        return fail(code=301, msg="no find", data="")
    use_verison = project_data.get("use_verison")
    if use_verison == "":
        return fail(code=302, msg="no find build version", data="")

    return success(data=f"static_files/build/{project_data.get('name')}/{project_data.get('use_verison')}.zip")


@ProjectApi.get("/config/{project_id}", summary=u"获取项目全部插件配置")
async def get_all_project_config(project_id: int) -> dict:
    return success(data=list(await ProjectSetting.filter(project_id=project_id).all()))


@ProjectApi.post("/", summary=u"添加项目")
async def add_projects(post: project.AddProject) -> dict:
    if await Project.filter(name=post.name).exists():
        return fail(code=10101, msg=u'当前名已被占用')
    await Project.create(**post.dict())
    return success()


@ProjectApi.post("/build/{project_id}", summary=u"构建当前项目")
async def build_projects(project_id: int, request: Request, note: Optional[str] = "") -> dict:
    client_host = request.client.host
    version_name = "0"
    count = await BuildVersion.filter(project_id=project_id).count()
    if count:
        version_name = str(count)
    await BuildVersion.create(name=version_name, note=note, project_id=project_id, host_name=client_host)
    # Todo: Add background build task, packaged as a zip file

    return success()


@ProjectApi.get("/build/", summary=u"获取全部构建历史")
async def get_build_projects(project_id: Optional[int] = 0) -> dict:
    if project_id:
        build_data = await BuildVersion.filter(project_id=project_id).all()
    else:
        build_data = await BuildVersion.all()
    return success(data=list(build_data))

