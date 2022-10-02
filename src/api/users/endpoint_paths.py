# -*- coding: utf-8 -*-
"""
endpoint routes for index
"""
from starlette.routing import Route

from api.users import endpoints

# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority

# base_path: str = "/users"
endpoint_routes = [
    Route(f"/", endpoint=endpoints.login, methods=["GET", "UPDATE"]),
    Route(f"/login", endpoint=endpoints.login, methods=["GET","POST"]),
    Route(f"/logout", endpoint=endpoints.logout, methods=["POST"]),
]
