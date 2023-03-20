"""
Artist related endpoint
"""
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from starlette.requests import Request
from app.db import database

from app.managers.auth import oauth2_scheme
from app.managers.artist import ArtistManager
from app.schemas.request.artist import ArtistIn
from app.schemas.response.artist import ArtistOut, ArtistReleaseGroupOut

router = APIRouter(tags=["Artist"])


@router.get("/artist/{substring}",
            summary="Find artist by name substring",
            dependencies=[Depends(oauth2_scheme)],
            response_model=List[ArtistOut]
            )
async def find_artist_by_substring(substring):
    list_artists = await ArtistManager.find_artist(substring)
    return list_artists


@router.get("/artist/{artist_id}/release_groups",
            summary="get all release groups of the artist",
            dependencies=[Depends(oauth2_scheme)],
            response_model=List[ArtistReleaseGroupOut]
            )
async def get_artist_release_groups(artist_id: int):
    list_release_groups = await ArtistManager.get_artist_release_groups(artist_id)
    return list_release_groups
