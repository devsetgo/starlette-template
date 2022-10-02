# -*- coding: utf-8 -*-

from loguru import logger

from core.database_crud import fetch_one_db
from core.database_models import users
from core.user_lib import verify_pass


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
    logger.info(f"fetch user_name: {user_name}")
    query = users.select().where(users.c.user_name == user_name)
    user_data = await fetch_one_db(query)

    logger.debug(f"LOOK AT THIS query result = {user_data}")

    if user_data == None:
        result = False

        return result

    result = verify_pass(pwd, user_data["password"])
    logger.info(f"password validity is {result}")
    return result
