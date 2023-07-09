import os
import uvicorn
import logging
from dotenv import load_dotenv, find_dotenv
from pyblish_pkg_config import app


if __name__ == "__main__":
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    main_app = app.main()
    # logger = logging.getLogger("uvicorn.access")
    uvicorn.run(main_app, port=int(os.getenv("START_PORT", 80)))

