# -*- coding: utf-8 -*-
import asyncio
import datetime
import logging
import uuid

from dsg_lib import logging_config
from loguru import logger
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from settings import config_settings
from core.database_setup import connect_db, create_db, disconnect_db

# templates and static files
templates = Jinja2Templates(directory="templates", autoescape=False, auto_reload=True)
statics = StaticFiles(directory="statics")


def init_app():
    """
    Initialization of application functions
    """
    logging_config.config_log(
        logging_directory="log",
        # or None and defaults to logging
        log_name="log.log",
        # or None and defaults to "log.log"
        logging_level=config_settings.loguru_logging_level,
        # or "info" or "debug" or "warning" or "error" or "critical"
        # or None and defaults to "info"
        log_rotation=config_settings.loguru_rotation,
        # or None and default is 10 MB
        log_retention=config_settings.loguru_retention,
        # or None and defaults to "14 Days"
        log_backtrace=True,
        # or None and defaults to False
        app_name=config_settings.app_name,
        # app name is used to identify the application
        # this is an optional field
        service_id=str(uuid.uuid4()),
        # service id is used to identify the service
        append_app_name=False,
        # append app name to log file name defaults to false
        # this is an optional field and will be injected
        append_service_id=False,
        # append app name and service name to log file name defaults to false
        # this is an optional field and will be injected
    )
    logger.info("Application logging has been initialized")
    logger.info("Initiating application")

    # create_db()
    logging.info("Initiating database-standard logging")


async def startup():
    """
    Functions and logging during startup
    """
    logger.info("starting up services")
    # start functions like database etc..
    # create database
    create_db()
    # connect to database
    await connect_db()
    logger.info("database connection established")

    # Create demo data if environment variable is true
    if config_settings.create_demo_data == True:
        # create demo data
        import time
        from core.demo_data import create_demo_data

        qty: int = config_settings.create_demo_qty
        logger.info(
            "Creating demo data is {config_settings.create_demo_data} and with a create qty of {qty}"
        )
        await create_demo_data(qty)


async def shutdown():
    """
    Functions and logging during shutdown
    """
    logger.info("shutting down services")
    # shutdown functions like database, saves etc..
    # disconnect from database
    await disconnect_db()
    logger.info("database disconnected")


# add other resource functions below here
