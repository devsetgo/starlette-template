# -*- coding: utf-8 -*-

from loguru import logger
from sqlalchemy.sql.functions import session_user
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, RedirectResponse

# from core import login_required
from resources import templates


async def login(request):
    # html_page = request.path_params["page"]
    try:
        template = "/auth/login.html"
        # this should be replaced with a function that does actual searches
        data: list = await search_creator()
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
async def logout(request):
    # html_page = request.path_params["page"]
    try:
        template = "/auth/logout.html"
        # this should be replaced with a function that does actual searches
        data: list = await search_creator()
        context = {"request": request, "data": data}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        detail: str = (
            f"Error: Page accessed: /auth/login , but HTML page {e} does not exist"
        )
        logger.error(detail)
        raise HTTPException(404, detail=detail)
