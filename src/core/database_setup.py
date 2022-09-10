# -*- coding: utf-8 -*-

import enum
import databases
from loguru import logger

from settings import config_settings

import sqlalchemy as sa

# from sqlalchemy import (
#     JSON,
#     BigInteger,
#     Boolean,
#     Column,
#     Date,
#     DateTime,
#     Enum,
#     Float,
#     Integer,
#     Interval,
#     LargeBinary,
#     MatchType,
#     MetaData,
#     Numeric,
#     PickleType,
#     SchemaType,
#     SmallInteger,
#     String,
#     Table,
#     Text,
#     Time,
#     Unicode,
#     UnicodeText,
#     create_engine,
#     pool,
# )


# Supported database types
databases_supported: list = ["mysql", "postgresql", "sqlite"]

# Database URI configuration for SQLite, PostgreSQL, and MySQL
# If library supports other types in future, they will be added

if config_settings.release_env == "test":
    database_uri = "sqlite:///:memory:?cache=shared"

    engine = sa.create_engine(
        database_uri,
        poolclass=sa.pool.QueuePool,
        max_overflow=10,
        pool_size=100,
    )
else:

    if config_settings.database_driver == "sqlite":
        database_uri = f"sqlite:///sqlite_db/{config_settings.db_name}.db"

        engine = sa.create_engine(
            database_uri,
            poolclass=sa.pool.QueuePool,
            max_overflow=10,
            pool_size=100,
        )

    elif config_settings.database_driver.lower() in databases_supported:
        database_uri = f"{config_settings.database_driver}://{config_settings.db_username}:{config_settings.db_password}@{config_settings.db_location}/{config_settings.db_name}"
        engine = sa.create_engine(
            database_uri,
            poolclass=sa.pool.QueuePool,
            max_overflow=10,
            pool_size=100,
        )

    else:
        # If the database driver is not supported, raise an error
        error_text = (
            f"Database driver {config_settings.database_driver} is not supported"
        )
        logger.critical(error_text)
        raise Exception(error_text)


# metadata = sa.MetaData()
database = databases.Database(database_uri)


def create_db():
    from core.database_models import metadata

    metadata.create_all(engine)
    logger.info(f"Creating tables")


async def connect_db():
    await database.connect()
    logger.info(f"connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info(f"disconnecting from database")
