# -*- coding: utf-8 -*-

from loguru import logger
from sqlalchemy.sql.functions import session_user
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, RedirectResponse
from settings import config_settings

# from core import login_required
from resources import templates


async def temp_homepage(request):

    template = f"home.html"
    context = {"request": request}
    logger.info(f"page '{request.url.path}' accessed")
    logger.critical(config_settings.release_env)
    return templates.TemplateResponse(template, context)


# @login_required.require_login
async def homepage(request):

    logger.info(request.session)
    # if "user_name" not in request.session:
    #     logger.info(f"page '{request.url.path}' accessed")
    #     return RedirectResponse(url=f"/", status_code=303)
    logger.info(f"page '{request.url.path}' accessed")
    return RedirectResponse(url=f"/pages/index", status_code=303)


# @login_required.require_login
async def about_page(request):

    template = f"about.html"
    context = {"request": request}
    logger.info(f"page '{request.url.path}' accessed")
    return templates.TemplateResponse(template, context)
