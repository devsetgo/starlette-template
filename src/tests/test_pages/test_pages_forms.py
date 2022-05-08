# -*- coding: utf-8 -*-
import unittest
import uuid

# from starlette.testclient import TestClient
import pytest
from async_asgi_testclient import TestClient

from main import app

client = TestClient(app)


# class Test(unittest.TestCase):
@pytest.mark.asyncio
async def test_pages_forms():
    pages = ["advanced", "editors", "general", "validation"]

    for page in pages:
        url = f"/pages/forms/{page}"
        response = await client.get(url)
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_pages_forms_error():
    uid = uuid.uuid1()
    url = f"/pages/forms/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
