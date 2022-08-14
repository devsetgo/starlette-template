# -*- coding: utf-8 -*-

from enum import unique
import databases
from loguru import logger
import loguru
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
databases_supported: list = ["mysql", "mariadb", "postgresql", "sqlite"]

# Database URI configuration for SQLite, PostgreSQL, MySQL/MariaDB, and Oracle/MSSQL
# sqlite://:memory:?cache=shared

if config_settings.release_env == "test":
    database_uri = "sqlite://:memory:?cache=shared"

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


metadata = sa.MetaData()
database = databases.Database(database_uri)


def create_db():
    metadata.create_all(engine)
    logger.info(f"Creating tables")


async def connect_db():
    await database.connect()
    logger.info(f"connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info(f"disconnecting from database")


users = sa.Table(
    "users",
    metadata,
    sa.Column("_id", sa.String, primary_key=True),
    sa.Column("username", sa.String, index=True),
    sa.Column("email", sa.String, index=True),
    sa.Column("password", sa.String, index=True),
    sa.Column("is_approved", sa.Boolean, index=True),
    sa.Column("is_admin", sa.Boolean, index=True),
    sa.Column("date_created", sa.DateTime, index=True),
    sa.Column("date_updated", sa.DateTime, index=True),
    sa.Column("last_login", sa.DateTime, index=True),
)


class UserHistoryType(enum.Enum):
    USER = "user"
    SYSTEM = "system"
    ADMIN = "admin"


user_history = sa.Table(
    "user_history",
    metadata,
    sa.Column("_id", sa.String, primary_key=True),
    sa.Column("user_id", sa.ForeignKey("user._id"), nullable=False),
    sa.Column("message", sa.String, index=True),
    sa.Column("type", sa.Enum(UserHistoryType)),
    sa.Column("date_created", sa.DateTime, index=True),
)
