# -*- coding: utf-8 -*-

import enum
from tkinter.tix import COLUMN
from typing import Collection
import databases
from loguru import logger
import loguru
from settings import config_settings

import sqlalchemy as sa

"""
SQLAlchemy data types
    JSON,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    Integer,
    Interval,
    LargeBinary,
    MatchType,
    MetaData,
    Numeric,
    PickleType,
    SchemaType,
    SmallInteger,
    String,
    Table,
    Text,
    Time,
    Unicode,
    UnicodeText,
    create_engine,
    pool,
"""

metadata = sa.MetaData()

users = sa.Table(
    "users",
    metadata,
    sa.Column("_id", sa.String, primary_key=True),
    sa.Column("user_name", sa.String(50), index=True),
    sa.Column("email", sa.String, index=True),
    sa.Column("password", sa.String, index=True),
    sa.Column("notes", sa.String(5000)),
    sa.Column("is_active", sa.Boolean),
    sa.Column("is_approved", sa.Boolean, index=True),
    sa.Column("is_rejected", sa.Boolean, index=True),
    sa.Column("is_admin", sa.Boolean, index=True),
    sa.Column("date_created", sa.DateTime, index=True),
    sa.Column("date_updated", sa.DateTime, index=True),
    sa.Column("last_login", sa.DateTime, index=True),
)

user_approval = sa.Table(
    "user_approval",
    metadata,
    sa.Column("_id", sa.String, primary_key=True),
    sa.Column("user_id", sa.ForeignKey("users._id"), nullable=False),
    sa.Column("is_approved", sa.Boolean),
    sa.Column("date_created", sa.DateTime),
    sa.Column("reviewed_by", sa.String),
)

user_login_failures = sa.Table(
    "user_login_failures",
    metadata,
    sa.Column("_id", sa.String, index=True, primary_key=True),
    sa.Column("date_created", sa.DateTime, index=True),
    sa.Column("user_name", sa.String, index=True),
    sa.Column("ip_address", sa.String, index=True),
    sa.Column("is_valid", sa.Boolean, index=True),
    sa.Column("is_active", sa.Boolean, index=True),
    sa.Column("request_data",sa.JSON())
)

# user history type
class UserHistoryType(enum.Enum):
    user = "user"
    system = "system"
    admin = "admin"


user_history = sa.Table(
    "user_history",
    metadata,
    sa.Column("_id", sa.String, primary_key=True),
    sa.Column("user_id", sa.ForeignKey("users._id"), nullable=True),
    sa.Column("message", sa.String, index=True),
    sa.Column("type", sa.Enum(UserHistoryType)),
    sa.Column("date_created", sa.DateTime, index=True),
)
