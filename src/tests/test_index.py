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
async def test_index():
    url = "/"
    response = await client.get(url)
    assert response.status_code == 200
    # assert response.json() == {"message": "Temp Home"}

@pytest.mark.asyncio
async def test_home():
    url = f"/index/home"
    response = await client.get(url)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_about():

    url = f"/index/about"
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_index_error():
    uid = uuid.uuid4()
    url = f"/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
