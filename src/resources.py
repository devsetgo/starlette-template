# -*- coding: utf-8 -*-
import asyncio
import datetime
import logging
import uuid

from loguru import logger
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from dsg_lib import logging_config

from settings import config_settings

# templates and static files
templates = Jinja2Templates(directory="templates")
statics = StaticFiles(directory="statics")


def init_app():

    logging_config.config_log(
        logging_directory="log",
        # or None and defaults to logging
        log_name="log.log",
        # or None and defaults to "log.log"
        logging_level="info",
        # or "info" or "debug" or "warning" or "error" or "critical"
        # or None and defaults to "info"
        log_rotation="10 MB",
        # or None and default is 10 MB
        log_retention="1 Day",
        # or None and defaults to "14 Days"
        log_backtrace=True,
        # or None and defaults to False
        app_name="my_app",
        # app name is used to identify the application
        # this is an optional field
        service_id=str(uuid.uuid4()),
        # service id is used to identify the service
        # this is an optional field
        append_app_name=True,
        # append app name to log file name defaults to false
        append_service_id=True,
        # append app name and service name to log file name defaults to false
    )
    logger.info("Initiating application")

    # create_db()
    logging.info("Initiating database-standard logging")


async def startup():

    logger.info("starting up services")
    # start functions like database etc..


async def shutdown():

    logger.info("shutting down services")
    # shutdown functions like database, saves etc..


# add other resource functions below here