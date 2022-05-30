# -*- coding: utf-8 -*-
from cgitb import reset
import unittest
from urllib import response
import uuid

import pytest

# from starlette.testclient import TestClient
from async_asgi_testclient import TestClient
from dsg_lib.patterns import pattern_between_two_char
from main import app

client = TestClient(app)


# class Test(unittest.TestCase):


@pytest.mark.asyncio
async def test_search_index():
    response = await client.get("/search/index")
    assert response.status_code == 200
    title_text = pattern_between_two_char(response.text, "<title>", "</title>")
    assert title_text["matched_found"] != 0


@pytest.mark.asyncio
async def test_search_index_error():
    response = await client.get("/search/index/xxx")
    assert response.status_code == 404
    # title_text = pattern_between_two_char(response.text, "<title>", "</title>")
    # assert title_text["matched_found"] != 0
