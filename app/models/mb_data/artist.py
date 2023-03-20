from app.db import mb_metadata

from dataclasses import dataclass
from sqlalchemy import Table, Column, Integer, String, VARCHAR


@dataclass
class Artist:
    id: int
    name: str
    sort_name: str
    begin_date_year: int
    end_date_year: int
    area: int
    rating: int


artist_table = Table(
    "artist",
    mb_metadata,
    Column("id", Integer),
    Column("name", VARCHAR),
    Column("sort_name", VARCHAR),
    Column("begin_date_year", Integer),
    Column("end_date_year", Integer),
    Column("area", Integer),
    Column("rating", Integer),
)
