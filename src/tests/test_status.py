# -*- coding: utf-8 -*-
import unittest

from starlette.testclient import TestClient

from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    def test_status(self):

        url = f"/status/"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 200

    def test_health(self):

        url = f"/status/health"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 200

    def test_information(self):

        url = f"/status/information"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 200

    def test_metrics(self):

        url = f"/status/metrics"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 200
