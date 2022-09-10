# -*- coding: utf-8 -*-
"""
endpoint routes for index
"""
from starlette.routing import Route

from api.auth import endpoints

# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority

base_path: str = "/users"
endpoint_routes = [
    Route(f"{base_path}/profile", endpoint=endpoints.login, methods=["GET", "UPDATE"]),
    Route(f"{base_path}/profile", endpoint=endpoints.login, methods=["GET", "UPDATE"]),
    Route(f"{base_path}/auth/login", endpoint=endpoints.login, methods=["POST"]),
    Route(f"{base_path}/auth/logout", endpoint=endpoints.logout, methods=["POST"]),
]
