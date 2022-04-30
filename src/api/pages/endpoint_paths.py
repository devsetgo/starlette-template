
# -*- coding: utf-8 -*-
"""
endpoint routes for index
"""
from starlette.routing import Route
from api.pages import endpoints


# define all routes for endpoint here
# note alphabetical order is important for prescidence of routes
# https://www.starlette.io/routing/#route-priority
endpoint_routes = [
    Route("/{page}", endpoint=endpoints.example_pages, methods=["GET"]),
    Route("/charts/{page}", endpoint=endpoints.example_pages_charts, methods=["GET"]),
    Route(
        "/examples/{page}", endpoint=endpoints.example_pages_examples, methods=["GET"],
    ),
    Route("/forms/{page}", endpoint=endpoints.example_pages_forms, methods=["GET"]),
    Route("/mailbox/{page}", endpoint=endpoints.example_pages_mailbox, methods=["GET"]),
    Route(
        "/data_tables/{page}", endpoint=endpoints.example_pages_tables, methods=["GET"],
    ),
    Route("/ui/{page}", endpoint=endpoints.example_pages_ui, methods=["GET"]),
]
