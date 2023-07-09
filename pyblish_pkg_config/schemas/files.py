from pydantic import BaseModel, Field
from ..models.enums import PluginType


class AddFiles(BaseModel):
    name: str = Field(max_length=20, description='项目名称', example="testProject")
    describe: str = Field(max_length=200, default="", description=u"项目描述")
    build_path: str = Field(max_length=60, description="构建的目录")
    plugin_type: PluginType = PluginType.Collect
