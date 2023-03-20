from dataclasses import dataclass
import sqlalchemy.dialects
from uuid import UUID
from sqlalchemy import Table

from app.db import mb_metadata


@dataclass
class Release:
    id: int
    gid: UUID
    name: str
    artist_credit: int
    release_group: int
    barcode: str
    packaging: str


releases_table = Table(
    "release",
    mb_metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("gid", sqlalchemy.dialects.postgresql.UUID),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR),
    sqlalchemy.Column("artist_credit", sqlalchemy.Integer),
    sqlalchemy.Column("release_group", sqlalchemy.Integer),
    sqlalchemy.Column("barcode", sqlalchemy.dialects.postgresql.VARCHAR),
    sqlalchemy.Column("packaging", sqlalchemy.String),
)
