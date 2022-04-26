# -*- coding: utf-8 -*-
"""
Application status endpoints
"""

from loguru import logger
from starlette.responses import JSONResponse



page_url = "/status"


async def health_status(request):
    """
    Application status endpoint with response of UP
    """
    logger.info(f"page {page_url}/health accessed")
    return JSONResponse({"status": "UP"})

async def information(request):
    """
    Application status endpoint with response from various connections
    """
    logger.info(f"page {page_url}/information accessed")
    return JSONResponse({"information": "UP"})