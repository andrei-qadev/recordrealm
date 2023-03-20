from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Table
import sqlalchemy.dialects

from app.db import rr_metadata
from app.models.mixins import TimeStamp

from dataclasses import dataclass
from datetime import datetime
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey


@dataclass
class Wishlist():
    id: int
    release_id: str
    user_id: int
    comment: str
    created_at: datetime
    updated_at: datetime


# Define the wishlists table using SQLAlchemy Core
wishlists_table = Table(
    "wishlists",
    rr_metadata,
    TimeStamp.created_at.copy(),
    TimeStamp.updated_at.copy(),
    Column("id", Integer, primary_key=True),
    Column("release_id", String(), nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("comment", Text),
)
