from pydantic import BaseModel, Field
from ..models.enums import PluginType


class AddFiles(BaseModel):
    name: str = Field(max_length=20, description='项目名称', example="testProject")
    describe: str = Field(max_length=200, default="", description=u"项目描述")
    add_module: str = Field(max_length=255, default="import pyblish.api", description="添加要导入的模块")
    plugin_type: PluginType = PluginType.Collect
    file_type: int = Field(default=0, description=u"0 为嵌入文件, 1 为引用文件")
    path: str = Field(max_length=255, default="", description=u"如果为引用, 引用的位置")
    to_path: str = Field(max_length=255, default="", description=u"部署之后的相对路径, 空为根目录")
    tags: str = Field(default="", max_length=255, description=u"文件标签名称")
    actions: str = Field(default="", max_length=40, description=u"actions list")
    active: int = Field(default=0, description=u"0 启用 1 关闭")
    families: str = Field(default="*", max_length=40, description=u"families list")
    hosts: str = Field(default="*", max_length=40, description=u"hosts list")
    optional: int = Field(default=1, description=u"0 启用 1 关闭")
    order: float = Field(default=0.0, description=u"偏移顺序 0.5 到 -0.5之间")
    targets: str = Field(default="", max_length=40, description=u"targets list")


class AddFileContent(BaseModel):
    process_parameter: str = Field(max_length=40, description='执行模块', example="process(self, instance)")
    process_content: str = Field(max_length=4096, default="", description=u"代码内容")
    repair_parameter: str = Field(max_length=40, description='只能检查模块使用 执行模块', example="repair(self, instance)")
    repair_content: str = Field(max_length=4096, default="", description=u"代码内容")
    other_content: str = Field(max_length=4096, default="", description=u"代码内容")


class AddTagsData(BaseModel):
    name: str = Field(max_length=20, default="", description=u"文件标签名称")
    color: str = Field(max_length=20, default="", description=u"文件标签名称")
    uses_count: int = Field(default=0, description=u"引用次数")

