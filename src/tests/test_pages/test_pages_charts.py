# -*- coding: utf-8 -*-
import unittest
import uuid

# from starlette.testclient import TestClient
from async_asgi_testclient import TestClient
from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    async def test_pages_charts(self):
        pages = [
            "chartjs",
            "flot",
            'inline',"uplot","charts-inline"
        ]

        for page in pages:
            url = f"/pages/charts/{page}"
            response = await client.get(url)
            assert response.status_code == 200

    async def test_pages_charts_error(self):
        uid = uuid.uuid1()
        url = f"/pages/charts/{uid}"
        response = await client.get(url)
        assert response.status_code == 404
