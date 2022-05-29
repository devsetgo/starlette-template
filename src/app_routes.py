# -*- coding: utf-8 -*-
"""
application routes
"""
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from api.app_status import endpoint_paths as status_routing
from api.index import endpoint_paths as index_routes
from api.index import endpoints as index_endpoints
from api.pages import endpoint_paths as pages_routing
from api.search import endpoint_paths as search_routing

routes = [
    Route("/", endpoint=index_endpoints.temp_homepage, methods=["GET"]),
    Route("/about", endpoint=index_endpoints.about_page, methods=["GET"]),
    Mount("/index", name="index", routes=index_routes.endpoint_routes),
    Mount("/pages", name="pages", routes=pages_routing.endpoint_routes),
    Mount("/search", name="search", routes=search_routing.endpoint_routes),
    Mount("/status", name="status", routes=status_routing.endpoint_routes),
    Mount("/static", app=StaticFiles(directory="statics"), name="static"),
]
