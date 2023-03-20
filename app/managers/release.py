from typing import List

from asyncpg import CaseNotFoundError
from fastapi import HTTPException

from app.db import database
from app.models import (
    ReleaseAggregate,
    release_aggregate_table,
    Release,
    releases_table,
    TrackAggregate,
    track_aggregate_table
)


class ReleaseManager:
    @staticmethod
    async def find_releases_by_barcode(barcode) -> List[ReleaseAggregate]:
        q = release_aggregate_table.select() \
            .where(release_aggregate_table.c.barcode == barcode)
        list_releases: List[ReleaseAggregate] = await database.fetch_all(q)

        if not len(list_releases):  # release does not exist
            raise HTTPException(404, f"Release with barcode {barcode} does not exist")

        return list_releases

    @staticmethod
    async def get_release(release_id) -> ReleaseAggregate:
        q = release_aggregate_table.select() \
            .where(release_aggregate_table.c.id == release_id)
        release: ReleaseAggregate = await database.fetch_one(q)
        if not release:
            raise HTTPException(404, f"Release with ID {release_id} not found")
        return release

    @staticmethod
    async def get_release_tracks(release_id) -> List[TrackAggregate]:
        q = track_aggregate_table.select() \
            .where(track_aggregate_table.c.release_id == release_id)
        list_tracks: List[TrackAggregate] = await database.fetch_all(q)

        if not len(list_tracks):  # tracks do not exist
            raise HTTPException(404, f"No tracks found for release with ID {release_id}")
        return list_tracks
