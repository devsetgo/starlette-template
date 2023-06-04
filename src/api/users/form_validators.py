# -*- coding: utf-8 -*-
import datetime
import re
import uuid
from loguru import logger

from core.database_crud import fetch_one_db
from core.database_models import users
from core.user_lib import verify_pass
from core.database_crud import execute_one_db, fetch_one_db
from core.database_models import user_login_failures, users


async def user_name_check(user_name: str):

    # check if unique user_name
    user_name = user_name.lower()
    query = users.select().where(users.c.user_name == user_name)
    logger.info(f"validating user_name: {user_name}")
    result = await fetch_one_db(query)
    logger.debug(f"LOOK AT THIS query result = {result}")
    return result


async def email_check(email: str):

    # check if unique email
    email_address = email.lower()
    query = users.select().where(users.c.email == email_address)
    logger.info(f"validating email: {email_address}")
    result = await fetch_one_db(query)
    logger.debug(f"query result = {result}")
    return result


async def valid_login(user_name: str, pwd: str):
    # get user user_name
    user_name = user_name.lower()
    logger.debug(f"checking if {user_name} has valid id")
    logger.info(f"fetch user_name: {user_name} to validate login")
    query = users.select().where(users.c.user_name == user_name)
    user_data = await fetch_one_db(query)

    logger.debug(f"LOOK AT THIS query result = {user_data}")

    if user_data == None:
        result = False
        return result

    result = verify_pass(pwd, user_data["password"])
    logger.info(f"password validity is {result}")
    return result


async def register_login_failure(fail_values: dict):
    logger.info(f"Start processing login failure record via background task")

    date_created = datetime.datetime.utcnow()
    _id = str(uuid.uuid4())

    fail_values["_id"] = _id
    fail_values["date_created"] = date_created

    fail_query = user_login_failures.insert()
    await execute_one_db(query=fail_query, values=fail_values)
    logger.info(f"End processing login failure record via background task")


async def test_bg(color:str):
    logger.critical(f"This color is {color}")
    from dsg_lib.file_functions import create_sample_files
    create_sample_files(filename="test_file", sample_size=1000)