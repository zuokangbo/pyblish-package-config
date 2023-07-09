from tortoise import fields
from tortoise.models import Model


class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description=u"创建时间")
    update_time = fields.DatetimeField(auto_now=True, description=u"更新时间")
    status = fields.IntField(default=1, description=u"0 删除, 1 正常")

    class Meta:
        abstract = True
