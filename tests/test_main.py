# -*- coding: utf-8 -*-
import pytest

from starlette.testclient import TestClient

from main import app


def test_status():

    url = f"/status/"
    client = TestClient(app)
    response = client.get(url)
    assert response.status_code == 200

def test_health():

    url = f"/status/health"
    client = TestClient(app)
    response = client.get(url)
    assert response.status_code == 200

def test_information():

    url = f"/status/information"
    client = TestClient(app)
    response = client.get(url)
    assert response.status_code == 200

def test_metrics():

    url = f"/status/metrics"
    client = TestClient(app)
    response = client.get(url)
    assert response.status_code == 200
