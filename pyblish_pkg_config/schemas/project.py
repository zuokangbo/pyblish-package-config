from pydantic import BaseModel, Field


class AddProject(BaseModel):
    name: str = Field(max_length=20, description='项目名称', example="testProject")
    describe: str = Field(max_length=200, default="", description=u"项目描述")
    build_path: str = Field(max_length=60, description="构建的目录")


class AddBuildVersion(BaseModel):
    name: str = Field(max_length=20, description='版本名称')
    note: str = Field(max_length=255, default="", description=u"备注")
    project_id: int = Field(description=u"项目id")


class AddProjectSetting(BaseModel):
    project_id: int = Field(description='项目id')
    template_id: int = Field(description='模板项id')
    actions: str = Field(max_length=40, description='actions list')
    active: int = Field(default=0, description='0 启用 1 关闭')
    families: str = Field(max_length=40, description='families list')
    hosts: str = Field(max_length=40, description='hosts list')
    optional: int = Field(default=1, description='0 启用 1 关闭')
    order: float = Field(default=0.0, description='偏移顺序 +-0.5')
    other_attr: str = Field(max_length=60, description='附加属性')
    targets: str = Field(max_length=40, description='targets list')

