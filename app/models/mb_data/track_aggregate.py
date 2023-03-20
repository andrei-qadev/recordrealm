from dataclasses import dataclass
import sqlalchemy.dialects
from sqlalchemy import Table

from app.db import mb_metadata


@dataclass
class TrackAggregate:
    id: int
    name: str
    length: int
    track_position: int
    medium_position: int
    release_id: int

    
track_aggregate_table = Table(
    "track_aggregate",
    mb_metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR),
    sqlalchemy.Column("length", sqlalchemy.Integer),
    sqlalchemy.Column("track_position", sqlalchemy.SMALLINT),
    sqlalchemy.Column("medium_position", sqlalchemy.Integer),
    sqlalchemy.Column("release_id", sqlalchemy.Integer),
)


