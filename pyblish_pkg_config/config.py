import os


project_root = os.getcwd()

DB_ORM_CONFIG = {
    "connections": {
        "pyblish_pkg_config": {
            "engine": "tortoise.backends.sqlite",
            "credentials": {"file_path": f"{project_root}/database/pyblish_pkg_config.sqlite3"}
        },
    },
    "apps": {
        "pyblish_pkg_config": {"models": ["pyblish_pkg_config.models"],
                         "default_connection": "pyblish_pkg_config"}
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}
