from tortoise import fields
from .model_abc import TimestampMixin
from .enums import PluginType


class TemplateFiles(TimestampMixin):
    name = fields.CharField(max_length=20, description="模板名称")
    label = fields.CharField(max_length=20, description="显示名称")
    add_module = fields.CharField(default="", max_length=255, description="添加要导入的模块")
    plugin_type = fields.IntEnumField(PluginType, default=PluginType.Collect, description="0 c, 1 v, 2 e, 3 i, 4, a")
    describe = fields.CharField(max_length=255, description="当前脚本的描述")
    file_type = fields.IntField(default=0, description="0 为嵌入文件, 1 为引用文件")
    path = fields.CharField(default="", max_length=255, description="如果为引用, 引用的位置")
    to_path = fields.CharField(default="", max_length=255, description="部署之后的相对路径, 空为根目录")
    tags = fields.CharField(default="", max_length=255, description="文件标签名称")
    template_id = fields.IntField(default=0, description="关联的模板内容")
    actions = fields.CharField(max_length=40, description="actions list")
    active = fields.IntField(default=0, description="0 启用 1 关闭")
    families = fields.CharField(max_length=40, description="families list")
    hosts = fields.CharField(max_length=40, description="hosts list")
    optional = fields.IntField(default=0, description="0 启用 1 关闭")
    order = fields.FloatField(default=0.0, description="偏移顺序")
    other_attr = fields.JSONField(default="{}", description="附加属性")
    targets = fields.CharField(max_length=40, description="targets list")


class TemplateContent(TimestampMixin):
    run_parameter = fields.CharField(max_length=20, description="传入参数")
    run_content = fields.TextField(default="")
    other_content = fields.TextField(default="")


class TagsData(TimestampMixin):
    name = fields.CharField(max_length=20, description="文件标签名称")
    color = fields.CharField(max_length=20, description="标签颜色")
    uses_count = fields.IntField(default=0, description="使用的数量")

