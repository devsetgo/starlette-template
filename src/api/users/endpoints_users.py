# -*- coding: utf-8 -*-

from loguru import logger
from sqlalchemy.sql.functions import session_user
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, RedirectResponse

# from core import login_required
from resources import templates


# @login_required.require_login
async def users_list(request):
    # html_page = request.path_params["page"]
    try:
        template = "/users/index.html"
        # this should be replaced with a function that does actual searches
        data: list = []
        context = {"request": request, "data": data}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        detail: str = (
            f"Error: Page accessed: /auth/login , but HTML page {e} does not exist"
        )
        logger.error(detail)
        raise HTTPException(404, detail=detail)


# @login_required.require_login
async def user_profile(request):
    # html_page = request.path_params["page"]
    try:
        template = "/users/profile.html"
        # this should be replaced with a function that does actual searches
        data: list = []
        context = {"request": request, "data": data}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        detail: str = (
            f"Error: Page accessed: /auth/login , but HTML page {e} does not exist"
        )
        logger.error(detail)
        raise HTTPException(404, detail=detail)


# @login_required.require_login
async def user_profile_update(request):
    # html_page = request.path_params["page"]
    try:
        # update and redirect
        return "x"
    except Exception as e:
        detail: str = (
            f"Error: Page accessed: /auth/login , but HTML page {e} does not exist"
        )
        logger.error(detail)
        raise HTTPException(404, detail=detail)
