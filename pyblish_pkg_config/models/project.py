from tortoise import fields
from tortoise.models import Model
from .model_abc import TimestampMixin


class Project(TimestampMixin):
    name = fields.CharField(max_length=20, description="项目名称")
    build_path = fields.CharField(max_length=60, description="构建的目录")
    use_verison = fields.CharField(default="", max_length=20, description="版本名称")
    describe = fields.CharField(max_length=255, description="项目描述")
    root_name = fields.CharField(max_length=60, description="根目录")


class BuildVersion(Model):
    name = fields.CharField(max_length=20, description="版本名称")
    note = fields.CharField(max_length=255, description="备注")
    project_id = fields.IntField(default=0, description="项目id")
    host_name = fields.CharField(max_length=20, description="发起构建请求的host")


class ProjectSetting(TimestampMixin):
    project_id = fields.IntField(default=0, description="项目id")
    template_id = fields.IntField(default=0, description="模板项id")
    actions = fields.CharField(max_length=40, description="actions list")
    active = fields.IntField(default=0, description="0 启用 1 关闭")
    families = fields.CharField(max_length=40, description="families list")
    hosts = fields.CharField(max_length=40, description="hosts list")
    optional = fields.IntField(default=0, description="0 启用 1 关闭")
    order = fields.FloatField(default=0.0, description="偏移顺序")
    other_attr = fields.JSONField(default="{}", description="附加属性")
    targets = fields.CharField(max_length=40, description="targets list")


class RootPathManager(Model):
    name = fields.CharField(max_length=20, description="名称")
    root_path = fields.CharField(max_length=64, description="根目录")
    describe = fields.CharField(max_length=255, description="项目描述")
