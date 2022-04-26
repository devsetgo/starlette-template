# -*- coding: utf-8 -*-
"""
application routes
"""
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from api.index import endpoints as index_endpoints
from api.app_status import endpoints as status_endpoints, routing as status_routing

routing = [
    Route("/", index_endpoints.homepage, name="dashboard", methods=["GET", "POST"]),
    Route("/about", index_endpoints.about_page, name="about", methods=["GET"]),
    Mount("/status", name="status", routes=status_routing.routes),
    Mount("/static", app=StaticFiles(directory="statics"), name="static"),
]
