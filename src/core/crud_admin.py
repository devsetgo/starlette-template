# -*- coding: utf-8 -*-
import datetime
import uuid

from loguru import logger

from core.database_crud import execute_one_db, fetch_all_db, fetch_one_db
from core.database_models import user_approval, users
from core.email_service import send_user_review


async def get_all_approvals():

    # get active bots
    query = user_approval.select()
    logger.debug(f"query for bots: {query}")
    result = await fetch_all_db(query)
    logger.debug(f"LOOK AT THIS query result = {result}")
    return result


async def get_unreviewed_approvals():

    # get active bots
    query = user_approval.select().where(user_approval.c.is_reviewed == False)
    logger.debug(f"query for bots: {query}")
    result = await fetch_all_db(query)
    logger.debug(f"Query result = {result}")
    return result


async def review_user(access_id: str):
    """
    Summary:
    Arguments:
        access_id {str} -- [description]
    Returns:
        [type] -- [description]
    """

    query = user_approval.select().where(user_approval.c.access_id == access_id)
    logger.debug(f"query for bots: {query}")
    result: dict = await fetch_one_db(query)
    logger.debug(f"Query result = {result}")
    return result


async def create_review_user(user_name: str):

    id = uuid.uuid4()
    values = {
        "date_create": datetime.datetime.utcnow(),
        "date_updated": datetime.datetime.utcnow(),
        "user_name": user_name.lower(),
        "access_id": str(id),
        "is_reviewed": False,
        "is_rejected": False,
        "is_admin": False,
    }
    query = user_approval.insert()
    logger.debug(f"query for bots: {query}")
    result = await execute_one_db(query=query, values=values)
    logger.critical(str(result))
    result = send_user_review(access_id=str(id))
    logger.critical(result)


# update reviewed user
async def update_user_review(data: dict):
    """
    [summary]
    Arguments:
        access_id {str} -- [description]
        is_reviewed {bool} -- [description]
        is_aproved {bool} -- [description]
        is_admin {bool} -- [description]
    """
    # "access_id": access_id,
    # "user_name": user_name,
    # "is_reviewed": True,
    # "is_rejected": is_rejected,
    # "is_active": is_active,
    # "is_admin": is_admin,
    values = {
        "date_updated": datetime.datetime.utcnow(),
        "is_reviewed": data["is_reviewed"],
        "is_rejected": data["is_rejected"],
        "is_admin": data["is_admin"],
    }
    query = user_approval.update().where(
        user_approval.c.access_id == str(data["access_id"])
    )
    await execute_one_db(query=query, values=values)

    user_values = {
        "is_active": data["is_active"],
        "is_admin": data["is_admin"],
    }
    user_query = users.update().where(users.c.user_name == data["user_name"])
    await execute_one_db(query=user_query, values=user_values)


async def user_data(use_name: str):

    query = users.select().where(users.c.user_name == use_name)
    result = await fetch_one_db(query=query)
    return result
