from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Table
import sqlalchemy.dialects

from app.db import rr_metadata
from app.models.enums import RoleType
from app.models.mixins import TimeStamp

from dataclasses import dataclass
from datetime import datetime
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Enum


@dataclass
class User():
    id: int
    email: str
    password: str
    name: str
    role: RoleType
    created_at: datetime
    updated_at: datetime


# Define the users table using SQLAlchemy Core
users_table = Table(
    "users",
    rr_metadata,
    TimeStamp.created_at.copy(),
    TimeStamp.updated_at.copy(),
    Column("id", Integer, primary_key=True),
    Column("email", String(120), unique=True),
    Column("password", String(255)),
    Column("name", String(255)),
    Column("role", Enum(RoleType), nullable=False, server_default=RoleType.user.name),
)
