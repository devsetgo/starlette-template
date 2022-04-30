# -*- coding: utf-8 -*-
"""
application routes
"""
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from resources import statics

from api.index import endpoint_paths as index_routes, endpoints as index_endpoints
from api.app_status import endpoint_paths as status_routing

routes = [
    Route("/", endpoint=index_endpoints.homepage, methods=["GET"]),
    Mount("/index", name="index", routes=index_routes.endpoint_routes),
    Mount("/status", name="status", routes=status_routing.endpoint_routes),
    Mount("/static", app=StaticFiles(directory="statics"), name="static"),
]
