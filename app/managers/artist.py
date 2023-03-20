from asyncpg import CaseNotFoundError
from fastapi import HTTPException
from sqlalchemy import func

from app.db import database
from app.models import artist_table, Artist, \
    artist_aggregate_table, ArtistAggregate, \
    ReleaseAggregate, release_aggregate_table
from typing import List
from app.utils.db_cache import async_cache


class ArtistManager:
    @async_cache(maxsize=1024)
    @staticmethod
    async def find_artist(substring) -> List[Artist]:
        similarity_threshold = 0.5
        similarity_score = func.similarity(artist_table.c.name, substring)
        q = (
            artist_table.select()
            .where(similarity_score >= similarity_threshold)
            .order_by(similarity_score.asc(), artist_table.c.rating.asc())
        )

        list_artists: List[Artist] = await database.fetch_all(q)
        return list_artists

    @staticmethod
    async def get_artist_release_groups(artist_id) -> List[ArtistAggregate]:
        q = artist_aggregate_table.select() \
            .where(artist_aggregate_table.c.id == artist_id)
        list_release_groups: List[ArtistAggregate] = await database.fetch_all(q)

        if not len(list_release_groups):  # artist does not exist
            raise HTTPException(404, f"Artist with ID {artist_id} does not exist")

        return list_release_groups
