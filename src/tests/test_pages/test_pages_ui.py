# -*- coding: utf-8 -*-
import logging
import unittest
import uuid

# from starlette.testclient import TestClient
import pytest
from async_asgi_testclient import TestClient
from dsg_lib.patterns import pattern_between_two_char
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
        title_text = pattern_between_two_char(response.text, "<title>", "</title>")
        assert title_text["matched_found"] != 0


@pytest.mark.asyncio
async def test_pages_ui_error():
    uid = uuid.uuid1()
    url = f"/pages/ui/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
    title_text = pattern_between_two_char(response.text, "<title>", "</title>")
    assert title_text["matched_found"] != 0
