# -*- coding: utf-8 -*-

from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from starlette_wtf import CSRFProtectMiddleware
from starlette_prometheus import PrometheusMiddleware

from core.custom_middleware import LoggerMiddleware
from settings import config_settings

middleware = [
    Middleware(
        SessionMiddleware,
        secret_key=config_settings.secret_key,
        max_age=config_settings.max_timeout,
        same_site="strict",
        session_cookie="session",
    ),
    Middleware(PrometheusMiddleware),
    Middleware(CSRFProtectMiddleware, csrf_secret=config_settings.csrf_secret),
    # Middleware(PrometheusMiddleware),
    # Middleware(LoggerMiddleware),
]
