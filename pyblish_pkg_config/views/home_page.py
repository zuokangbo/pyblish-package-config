import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory=f"{os.getcwd()}/public/templates".replace("\\", "/"))
home_view_api = APIRouter(prefix="/page", tags=[u"视图"])


@home_view_api.get("/home", response_class=HTMLResponse)
async def readme_home_page(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})


