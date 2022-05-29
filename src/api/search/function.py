# -*- coding: utf-8 -*-
import silly


def search_creator(qty: int = 50) -> list:
    search_data: list = []
    for i in range(qty):
        data: dict = {
            "name": silly.name(),
            "thing": silly.thing(),
            "domain": silly.domain(),
            "text": silly.sentence(),
            "email": silly.email(),
        }
        search_data.append(data)
    return search_data
