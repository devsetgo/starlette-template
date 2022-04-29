# -*- coding: utf-8 -*-
"""
Application status endpoints
"""
from pathlib import Path
import re
from loguru import logger
from starlette.responses import JSONResponse, PlainTextResponse
from settings import config_settings
from dsg_lib.folder_functions import last_data_files_changed


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
    }
    the_routes=dict(sorted(status_routes.items(),key= lambda x:x[1]))
    logger.info(f"page '{request.url.path}' accessed")
    return JSONResponse(the_routes)


async def health_status(request):
    """
    Application status endpoint with response of UP
    """
    logger.info(f"page '{request.url.path}' accessed")
    return JSONResponse({"status": "up"})

async def information(request):
    """
    Application status endpoint with response from various connections
    """
    # custom information here.
    data:dict = {"information": "add yours here"}
    logger.info(f"page '{request.url.path}' accessed")
    return JSONResponse(data)

# this needs to be secure
async def environment_config(request):
    """
    Application enviornment configuration endpoint
    """
    logger.info(f"page '{request.url.path}' accessed")
    return JSONResponse(dict(config_settings))

# this needs to be secure
async def log_file(request):
    """
    Application log file endpoint
    Only displays for instance access and not a central log file
    """

    directory_to__files: str = "log"
    # get log file name from directory
    log_directory = Path.cwd().joinpath(directory_to__files)
    last_file = last_data_files_changed(directory_path=log_directory)
    file_name = str(last_file[1])
    file_save = Path.cwd().joinpath(directory_to__files).joinpath(file_name)
        # open/create file
    with open(file_save, "r", encoding="utf-8") as f:
        # write data to file
        data = f.read()

    logger.info(f"page '{request.url.path}' accessed")
    return PlainTextResponse(data)
