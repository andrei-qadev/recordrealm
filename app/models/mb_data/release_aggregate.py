from dataclasses import dataclass
import sqlalchemy.dialects
from uuid import UUID
from sqlalchemy import Table, Column, Integer, String, VARCHAR, SMALLINT, BIGINT

from app.db import mb_metadata


@dataclass
class ReleaseAggregate:
    id: int
    release_group_name: str
    artist_credit_name: str
    year: int
    country_name: str
    label_name: str
    release_type: str
    packaging: str
    artist_credit_id: int
    barcode: str
    release_group_id: int
    gid: UUID


release_aggregate_table = Table(
    "release_aggregate",
    mb_metadata,
    sqlalchemy.Column("id", Integer),
    sqlalchemy.Column("release_group_name", VARCHAR),
    sqlalchemy.Column("artist_credit_name", VARCHAR),
    sqlalchemy.Column("year", SMALLINT),
    sqlalchemy.Column("country_name", VARCHAR),
    sqlalchemy.Column("label_name", VARCHAR),
    sqlalchemy.Column("release_type", VARCHAR),
    sqlalchemy.Column("packaging", VARCHAR),
    sqlalchemy.Column("artist_credit_id", Integer),
    sqlalchemy.Column("barcode", VARCHAR),
    sqlalchemy.Column("release_group_id", Integer),
    sqlalchemy.Column("gid", sqlalchemy.dialects.postgresql.UUID),
)
