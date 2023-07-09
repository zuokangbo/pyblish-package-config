from enum import IntEnum


class PluginType(IntEnum):
    Collect = 0
    Validate = 1
    Extract = 2
    Integrate = 3
    Action = 4
