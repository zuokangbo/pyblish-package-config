from fastapi import Request
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

__all__ = ["custom_swagger_ui_html", "redoc_html"]


def custom_swagger_ui_html(req: Request):
    return get_swagger_ui_html(
        openapi_url=req.app.openapi_url,
        title=req.app.title + " - Swagger UI",
        oauth2_redirect_url=req.app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/swagger/swagger-ui-bundle.js",
        swagger_css_url="/swagger/swagger-ui.css"
    )


def redoc_html(req: Request):
    return get_redoc_html(
        openapi_url=req.app.openapi_url,
        title=req.app.title + "- ReDoc",
        redoc_js_url="/redoc/redoc.standalone.js"
    )

