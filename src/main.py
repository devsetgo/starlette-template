# -*- coding: utf-8 -*-

from concurrent.futures.thread import _worker
from starlette.applications import Starlette

import resources
import app_routes
from core import exceptions
from resources import init_app
from settings import config_settings
import app_middleware

init_app()

if config_settings.release_env == "prd":
    debug_value = False
else:
    debug_value = config_settings.debug

app = Starlette(
    debug=debug_value,
    routes=app_routes.routes,
    middleware=app_middleware.middleware,
    exception_handlers=exceptions.exception_handlers,
    on_startup=[resources.startup],
    on_shutdown=[resources.shutdown],
)


# for starting server by file
if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info", debug=debug_value)