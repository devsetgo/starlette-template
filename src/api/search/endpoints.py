# -*- coding: utf-8 -*-

from loguru import logger
from sqlalchemy.sql.functions import session_user
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, RedirectResponse

# from core import login_required
from resources import templates
from api.search.function import search_creator

# @login_required.require_login


async def search_page(request):
    # html_page = request.path_params["page"]
    try:
        template = "/search/index.html"

        context = {"request": request, "data": search_creator()}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        detail: str = (
            f"Error: Page accessed: /search/index , but HTML page {e} does not exist"
        )
        logger.error(detail)
        raise HTTPException(404, detail=detail)
