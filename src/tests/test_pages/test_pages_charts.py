# -*- coding: utf-8 -*-
import unittest
import uuid

import pytest

# from starlette.testclient import TestClient
from async_asgi_testclient import TestClient
from dsg_lib.patterns import pattern_between_two_char

from main import app

client = TestClient(app)


# class Test(unittest.TestCase):


@pytest.mark.asyncio
async def test_pages_charts():
    pages = ["chartjs", "flot", "inline", "uplot"]  # , "charts-inline"]

    for page in pages:
        url = f"/pages/charts/{page}"
        response = await client.get(url)
        assert response.status_code == 200
        title_text = pattern_between_two_char(response.text, "<title>", "</title>")
        assert title_text["matched_found"] != 0


@pytest.mark.asyncio
async def test_pages_charts_error():
    uid = uuid.uuid1()
    url = f"/pages/charts/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
    title_text = pattern_between_two_char(response.text, "<title>", "</title>")
    assert title_text["matched_found"] != 0
