# -*- coding: utf-8 -*-
import unittest
import uuid
import logging
from loguru import logger
from starlette.testclient import TestClient
# from async_asgi_testclient import TestClient
from main import app

client = TestClient(app,backend="asyncio")

class Test(unittest.TestCase):
    def test_pages_ui(self):
        pages = [
            "buttons",
            "general",
            "icons",
            "modals",
            "navbar",
            "ribbons",
            "sliders",
            "timeline",
        ]

        for page in pages:
            url = f"/pages/ui/{page}"
            response =client.get(url)
            assert response.status_code == 200
            assert response.text is not None

    def test_pages_ui_error(self):
        uid = uuid.uuid1()
        url = f"/pages/ui/{uid}"
        response =client.get(url)
        assert response.status_code == 404
        assert response.text is not None
