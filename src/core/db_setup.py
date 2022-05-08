# -*- coding: utf-8 -*-

from enum import unique

import databases
from loguru import logger
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
    pool,
)
from sqlalchemy.sql.sqltypes import Text

from settings import config_settings

engine = create_engine(
    config_settings.sqlalchemy_database_uri,
    poolclass=pool.QueuePool,
    max_overflow=10,
    pool_size=100,
)
metadata = MetaData()
database = databases.Database(config_settings.sqlalchemy_database_uri)


def create_db():

    metadata.create_all(engine)
    logger.info("Creating tables")
    get_all_tables()


def get_all_tables():
    from sqlalchemy import MetaData

    m = MetaData()
    m.reflect(engine)
    for table in m.tables.values():
        # logger.info(table.name)
        columns: list = []
        for column in table.c:
            columns.append(column.name)
        table_data = {"table": table.name, "columns": columns}
        logger.info(f"Table exists - {table_data}")


async def connect_db():
    await database.connect()
    logger.info("connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info("disconnecting from database")


users = Table(
    "users",
    metadata,
    Column("id", String, primary_key=True),
    Column("user_name", String, index=True, unique=True),
    Column("password", String, index=True),
    Column("email", String, index=True),  # , unique=True),
    # add more fields as needed
    Column("notes", String(500)),
    Column("is_active", Boolean, index=True),
    Column("is_admin", Boolean, index=True),
    Column("first_login", Boolean, index=True),
    Column("from_config", Boolean, index=True),
    Column("date_created", DateTime, index=True),
    Column("last_login", DateTime, index=True),
)
