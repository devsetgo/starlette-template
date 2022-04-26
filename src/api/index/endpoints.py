# -*- coding: utf-8 -*-

from loguru import logger
from sqlalchemy.sql.functions import session_user
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse, JSONResponse

# from core import login_required
from resources import templates


async def temp_homepage(request):
    logger.critical(request.session)

    return JSONResponse({"message": "Hello World"},status_code=200)

# @login_required.require_login
async def homepage(request):
    logger.critical(request.session)
    if "user_name" not in request.session:
        return RedirectResponse(url=f"/", status_code=303)

    return RedirectResponse(url=f"/dashboard", status_code=303)

# @login_required.require_login
async def about_page(request):

    template = f"about.html"
    context = {"request": request}
    logger.info(f"page accessed: /{template}")
    return templates.TemplateResponse(template, context)