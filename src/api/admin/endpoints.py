# -*- coding: utf-8 -*-

from loguru import logger
from sqlalchemy.sql.functions import session_user
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse, RedirectResponse
from settings import config_settings

# from core import login_required
from resources import templates


async def index(request):

    template = f"index.html"
    context = {"request": request}
    logger.info(f"page '{request.url.path}' accessed")
    logger.critical(config_settings.release_env)
    return templates.TemplateResponse(template, context)


async def users_list(request):
    # TODO: create list of users to review
    template = f"users-list.html"
    context = {"request": request}
    logger.info(f"page '{request.url.path}' accessed")
    logger.critical(config_settings.release_env)
    return templates.TemplateResponse(template, context)


async def access_request(request):
    # TODO: create open access request review
    template = f"access-request.html"
    context = {"request": request}
    logger.info(f"page '{request.url.path}' accessed")
    logger.critical(config_settings.release_env)
    return templates.TemplateResponse(template, context)


async def access_rejections(request):
    # TODO: create open access request review
    template = f"access-rejections.html"
    context = {"request": request}
    logger.info(f"page '{request.url.path}' accessed")
    logger.critical(config_settings.release_env)
    return templates.TemplateResponse(template, context)


async def access_decision(request):
    # TODO: complete user access accept/reject status
    return "state"
