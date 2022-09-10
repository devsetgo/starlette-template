# -*- coding: utf-8 -*-

from operator import truediv
from loguru import logger
from core.database_crud import execute_one_db, fetch_all_db, fetch_one_db
from settings import config_settings
import time
from tqdm import tqdm
from core.database_models import users, user_history
import silly
import uuid
import random
import secrets
from core.user_lib import encrypt_pass
import datetime


async def create_demo_data(qty: int):
    t0 = time.time()
    db_empty = await confirm_db_empty()

    user_id: list = []

    if db_empty == True:
        for _ in tqdm(range(qty)):
            id = await create_user()
            user_id.append(id)

        await get_user_list()
        for u in tqdm(user_id):
            time.sleep(.005)
            for _ in tqdm(range(100),leave=False):
                await user_history_insert(u)
    t1 = time.time() - t0
    logger.info(f"demo took {t1:.2f} seconds to create")

async def confirm_db_empty() -> bool:
    # if empty, return true
    query = users.select().limit(10)
    result = await fetch_all_db(query)
    logger.critical(result)

    if len(result) <= 1:
        logger.warning("database is empty")
        return True
    else:
        logger.warning("database is note empty")
        return False


async def create_user():
    set_id = str(uuid.uuid1())
    rand_name: str = silly.noun()
    rand_num: int = random.randint(1, 10000)
    username: str = f"{rand_name}{rand_num}"
    email = silly.email()
    notes: str = "a bunch of words can go here...."
    hash_pwd: str = encrypt_pass(secrets.token_urlsafe(8))

    user_information = {
        "_id": set_id,
        "username": username,
        "email": email,
        "notes": notes,
        "password": hash_pwd,
        "date_created": datetime.datetime.utcnow(),
        "date_updated": datetime.datetime.utcnow(),
        "last_login": None,
        "is_approved": random.choice([True, False]),
        "is_active": random.choice([True, False]),
        "is_admin": random.choice([True, False]),
    }
    query = users.insert()
    await execute_one_db(query=query, values=user_information)
    logger.warning(f"DEMO user ID: {set_id} created")
    return set_id


async def get_user_list() -> list:
    query = users.select().limit(10)
    result = await fetch_all_db(query)
    logger.info(f"number of records in database = {len(result)}")
    return result


async def user_history_insert(user_id: str):

    history_type: list = ["user", "system", "admin"]
    rand_hist = random.randint(0, 2)
    if history_type[rand_hist] != "user":
        id = None
    else:
        id=user_id

    base_id=str(uuid.uuid1())
    history_data = {
        "_id": base_id,
        "user_id": id,
        "message": silly.sentence(),
        "type": history_type[rand_hist],
        "date_created": datetime.datetime.utcnow(),
    }
    query = user_history.insert()
    await execute_one_db(query=query, values=history_data)
    logger.warning(f"DEMO user history ID: {base_id} created")
    return True
