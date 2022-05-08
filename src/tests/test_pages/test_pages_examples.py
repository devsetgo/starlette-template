# -*- coding: utf-8 -*-
import unittest
import uuid

#from starlette.testclient import TestClient
from async_asgi_testclient import TestClient
from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    async def test_pages_examples(self):
        pages = [
            "403",
            "404",
            "500",
            "blank",
            "contacts",
            "e_commerce",
            "forgot-password",
            "invoice-print",
            "invoice",
            "lockscreen",
            "login",
            "pace",
            "profile",
            "project_add",
            "project_detail",
            "project_edit",
            "projects",
            "recover-password",
            "register",
        ]

        for page in pages:
            url = f"/pages/examples/{page}"
            response = await client.get(url)
            assert response.status_code == 200

    async def test_pages_forms_error(self):
        uid = uuid.uuid1()
        url = f"/pages/examples/{uid}"
        response = await client.get(url)
        assert response.status_code == 404
