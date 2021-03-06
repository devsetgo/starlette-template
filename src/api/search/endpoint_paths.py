# -*- coding: utf-8 -*-
"""
endpoint routes for index
"""
from starlette.routing import Route

from api.search import endpoints

# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority
endpoint_routes = [
    Route("/index", endpoint=endpoints.search_page, methods=["GET"]),
]
