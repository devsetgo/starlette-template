# -*- coding: utf-8 -*-
import silly


# this should be replaced with a function that does actual searches
async def search_creator(qty: int = 20) -> list:
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
