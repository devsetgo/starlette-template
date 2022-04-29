# -*- coding: utf-8 -*-
"""
Application status endpoints
"""

from loguru import logger
from starlette.responses import JSONResponse
from settings import config_settings
from dsg_lib.file_functions import open_text


page_url = "/status"

async def status(request):
    """
    Application status endpoint with response from various connections
    """
    status_routes = {
        "status": "/status/",
        "health": "/status/health",
        "information": "/status/information",
        "metrics": "/status/metrics",
        "environment": "/status/env",
        "log": "/status/log",
        "shutdown": "/status/shutdown",
        "thread_dump": "/status/thread",
    }
    the_routes=dict(sorted(status_routes.items(),key= lambda x:x[1]))
    logger.info(f"page {page_url} accessed")
    return JSONResponse(the_routes)


async def health_status(request):
    """
    Application status endpoint with response of UP
    """
    logger.info(f"page {page_url}/health accessed")
    return JSONResponse({"status": "up"})

async def information(request):
    """
    Application status endpoint with response from various connections
    """
    logger.info(f"page {page_url}/information accessed")
    return JSONResponse({"information": "up"})


async def environment_config(request):
    """
    Application status endpoint with response from various connections
    """
    print(dict(config_settings))
    logger.info(f"page {page_url}/information accessed")
    return JSONResponse(dict(config_settings))


async def log_file(request):
    """
    Application status endpoint with response from various connections
    """
    data = open_text(config_settings.LOG_FILE)
    logger.info(f"page {page_url}/information accessed")
    return JSONResponse({"information": "up"})

async def thread_dump(request):
    """
    Application status endpoint with response from various connections
    """

    logger.info(f"page {page_url}/information accessed")
    return JSONResponse({"information": "up"})


async def shut_down(request):
    """
    Application status endpoint with response from various connections
    """
    import sys 
    
    logger.info(f"page {page_url}/information accessed")
    sys.exit()


