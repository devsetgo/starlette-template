# -*- coding: utf-8 -*-
import logging
import unittest
import uuid

# from starlette.testclient import TestClient
import pytest
from async_asgi_testclient import TestClient
from loguru import logger

from main import app

client = TestClient(app)


# class Test(unittest.TestCase):
@pytest.mark.asyncio
async def test_pages_ui():
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
        response = await client.get(url)
        assert response.status_code == 200
        assert response.text is not None


@pytest.mark.asyncio
async def test_pages_ui_error():
    uid = uuid.uuid1()
    url = f"/pages/ui/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
    assert response.text is not None
