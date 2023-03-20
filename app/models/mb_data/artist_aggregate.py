from dataclasses import dataclass
import sqlalchemy.dialects
from sqlalchemy import Table

from app.db import mb_metadata

from dataclasses import dataclass
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, VARCHAR


@dataclass
class ArtistAggregate:
    id: int
    name: str
    sort_name: str
    release_group_id: int
    release_group_name: str
    artist_position: int
    release_type: str


# Define the artist_aggregate table using SQLAlchemy Core
artist_aggregate_table = Table(
    "artist_aggregate",
    mb_metadata,
    Column("id", Integer),
    Column("name", VARCHAR),
    Column("sort_name", VARCHAR),
    Column("release_group_id", Integer),
    Column("release_group_name", VARCHAR),
    Column("artist_position", Integer),
    Column("release_type", VARCHAR),
)

#
#
# @dataclass
# class ArtistAggregate(BaseModel):
#     table = Table(
#         "artist_aggregate",
#         mb_metadata,
#         sqlalchemy.Column("id", sqlalchemy.Integer),
#         sqlalchemy.Column("name", sqlalchemy.VARCHAR),
#         sqlalchemy.Column("sort_name", sqlalchemy.VARCHAR),
#         sqlalchemy.Column("release_group_id", sqlalchemy.Integer),
#         sqlalchemy.Column("release_group_name", sqlalchemy.VARCHAR),
#         sqlalchemy.Column("artist_position", sqlalchemy.Integer),
#         sqlalchemy.Column("release_type", sqlalchemy.VARCHAR),
#     )
#
#     name: str
#     sort_name: str
#     release_group_id: int
#     release_group_name: str
#     artist_position: int
#     release_type: str
#     id: int | None = None
