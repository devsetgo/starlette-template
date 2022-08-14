# -*- coding: utf-8 -*-
"""
endpoint routes for index
"""
from starlette.routing import Route

from api.auth import endpoints

# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority
endpoint_routes = [
    Route("/auth/login", endpoint=endpoints.login, methods=["POST"]),
    Route("/auth/logout", endpoint=endpoints.logout, methods=["POST"]),
]
