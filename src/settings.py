# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""

import secrets
from functools import lru_cache
import logging
from pydantic import BaseSettings


class Settings(BaseSettings):
    # use_env = "dotenv"
    app_name: str = "starlette-template"
    app_version: str = "1.0.0"

    # application configuration
    release_env: str = "prd"
    debug: bool = False
    create_demo_data: bool = False
    create_demo_qty: int = 0
    # Gunicorn or Uvicorn workers
    workers: int = 2
    # session logout timeout
    max_timeout: int = 7200
    same_site: str = "lax"
    login_timeout: int = 120
    # require HTTPS
    https_on: bool = False
    # endable prometheus metrics
    prometheus_on: bool = True
    # Database Configuration
    database_driver: str = "sqlite"
    db_username: str = "test"
    db_password: str = "test"
    db_location: str = "localhost"
    db_name: str = "api"
    # logging settings
    log_name: str = "log.log"
    loguru_retention: str = "30 days"
    loguru_rotation: str = "100 MB"
    # set value to be default if not set in .env
    # Values NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
    loguru_logging_level: str = "INFO"
    admin_create: bool = False
    admin_user_name: str = None
    admin_user_key: str = None
    admin_user_email: str = None
    # secrets
    csrf_secret = secrets.token_hex(48)
    secret_key = secrets.token_hex(512)
    # invalid character list
    invalid_character_list: list = [
        " ",
        ";",
        "<",
        ">",
        "/",
        "\\",
        "{",
        "}",
        "[",
        "]",
        "+",
        "=",
        "?",
        "&",
        ",",
        ":",
        "'",
        ".",
        '"',
        "`",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()


config_settings = get_settings()
