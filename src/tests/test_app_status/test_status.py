# -*- coding: utf-8 -*-
import unittest

import pytest
from async_asgi_testclient import TestClient

from main import app

# from starlette.testclient import TestClient


client = TestClient(app)


# class Test(unittest.TestCase):


@pytest.mark.asyncio
async def test_status():

    url = f"/status/"
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_env():

    url = f"/status/env"
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health():

    url = f"/status/health"
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_information():

    url = f"/status/information"
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_log():

    url = f"/status/log"
    response = await client.get(url)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_metrics():

    url = f"/status/metrics"
    response = await client.get(url)
    assert response.status_code == 200
