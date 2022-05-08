# -*- coding: utf-8 -*-
import unittest
import uuid

# from starlette.testclient import TestClient
from async_asgi_testclient import TestClient
from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    async def test_pages_tables(self):
        pages = ["data", "jsgrid", "simple"]

        for page in pages:
            url = f"/pages/tables/{page}"
            response = await client.get(url)
            assert response.status_code == 200
            assert response.text is not None

    async def test_pages_tables_error(self):
        uid = uuid.uuid1()
        url = f"/pages/tables/{uid}"
        response = await client.get(url)
        assert response.status_code == 404
        assert response.text is not None
