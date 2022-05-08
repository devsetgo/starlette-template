# -*- coding: utf-8 -*-
import unittest

from starlette.testclient import TestClient
# from async_asgi_testclient import TestClient
from main import app

client = TestClient(app,backend="asyncio")


class Test(unittest.TestCase):
    def test_status(self):

        url = f"/status/"
        response = client.get(url)
        assert response.status_code == 200

    def test_env(self):

        url = f"/status/env"
        response = client.get(url)
        assert response.status_code == 200

    def test_health(self):

        url = f"/status/health"
        response = client.get(url)
        assert response.status_code == 200

    def test_information(self):

        url = f"/status/information"
        response = client.get(url)
        assert response.status_code == 200

    def test_log(self):

        url = f"/status/log"
        response = client.get(url)
        assert response.status_code == 200

    def test_metrics(self):

        url = f"/status/metrics"
        response = client.get(url)
        assert response.status_code == 200
