# -*- coding: utf-8 -*-
"""
endpoint routes for status
"""
from starlette.routing import Route
from api.app_status import endpoints as status_endpoints
from starlette_prometheus import metrics


# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority
endpoint_routes = [
    Route("/", endpoint=status_endpoints.status, methods=["GET"]),
    Route("/env", endpoint=status_endpoints.environment_config, methods=["GET"]),
    Route("/health", endpoint=status_endpoints.health_status, methods=["GET"]),
    Route("/information", endpoint=status_endpoints.information, methods=["GET"]),
    Route("/log", endpoint=status_endpoints.log_file, methods=["GET"]),
    Route("/metrics", endpoint=metrics, methods=["GET"]),
    Route("/shutdown", endpoint=status_endpoints.shut_down, methods=["GET"]),
    Route("/thread-dump", endpoint=status_endpoints.thread_dump, methods=["POST"]),
]
