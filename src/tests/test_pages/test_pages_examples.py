# -*- coding: utf-8 -*-
import unittest
import uuid

# from starlette.testclient import TestClient
import pytest
from async_asgi_testclient import TestClient
from dsg_lib.patterns import pattern_between_two_char

from main import app

client = TestClient(app)


# class Test(unittest.TestCase):
@pytest.mark.asyncio
async def test_pages_examples():
    pages = [
        "403",
        "404",
        "500",
        "blank",
        "contacts",
        "e-commerce",
        "forgot-password",
        "invoice-print",
        "invoice",
        "lockscreen",
        "login",
        "pace",
        "profile",
        "project-add",
        "project-detail",
        "project-edit",
        "projects",
        "recover-password",
        "register",
    ]

    for page in pages:
        url = f"/pages/examples/{page}"
        response = await client.get(url)
        assert response.status_code == 200
        title_text = pattern_between_two_char(response.text, "<title>", "</title>")
        assert title_text["matched_found"] != 0


@pytest.mark.asyncio
async def test_pages_forms_error():
    uid = uuid.uuid1()
    url = f"/pages/examples/{uid}"
    response = await client.get(url)
    assert response.status_code == 404
    title_text = pattern_between_two_char(response.text, "<title>", "</title>")
    assert title_text["matched_found"] != 0
