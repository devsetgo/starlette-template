# -*- coding: utf-8 -*-
"""
endpoint routes for index
"""
from starlette.routing import Route

from api.index import endpoints

# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority
endpoint_routes = [
    Route("/home", endpoint=endpoints.homepage, methods=["GET"]),
    # Route("/index", endpoint=endpoints.homepage, methods=["GET"]),
    Route("/about", endpoint=endpoints.about_page, methods=["GET"]),
]
