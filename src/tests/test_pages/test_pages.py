# -*- coding: utf-8 -*-
import unittest
import uuid

import pytest

# from starlette.testclient import TestClient
from async_asgi_testclient import TestClient

from main import app

client = TestClient(app)


# class Test(unittest.TestCase):


@pytest.mark.asyncio
async def test_pages():
    pages = [
        "calendar",
        "gallery",
        "widgets",
        "kanban",
        "iframe",
        "iframe-dark",
        "index",
        "index2",
        "index3",
    ]

    for page in pages:
        url = f"/pages/{page}"
        response = await client.get(url)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_pages_error():
    uid = uuid.uuid4()
    url = f"/pages/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
