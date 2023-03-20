"""
release related endpoint
"""
from operator import itemgetter
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from starlette.requests import Request

from app.db import database
from app.managers.auth import oauth2_scheme
from app.managers.release import ReleaseManager
from app.schemas.response.release import ReleaseOut, ReleaseTracksOut
from app.schemas.response.track import TrackOut

router = APIRouter(tags=["Release"])


@router.get("/release/by_barcode",
            summary="returns the list of releases that match the barcode id",
            # dependencies=[Depends(oauth2_scheme)],
            response_model=List[ReleaseOut]
            )
async def find_release_by_barcode(barcode: str):
    # TODO: return flag in_collection: boolean
    list_releases = await ReleaseManager.find_releases_by_barcode(barcode)
    return list_releases


@router.get("/release/{release_id}",
            summary="fetch release data by release ID",
            # dependencies=[Depends(oauth2_scheme)],
            response_model=ReleaseOut
            )
async def get_release_by_id(release_id: int):
    # TODO: return flag in_collection: boolean
    release = await ReleaseManager.get_release(release_id)
    return release


@router.get("/release/{release_id}/tracks",
            summary="returns the tracklist of the release",
            # dependencies=[Depends(oauth2_scheme)],
            response_model=ReleaseTracksOut
            )
async def get_release_tracks(release_id: int):
    list_release_tracks = await ReleaseManager.get_release_tracks(release_id)
    list_release_tracks = sorted(list_release_tracks, key=itemgetter('medium_position', 'track_position'))
    return {
        "total_tracks": len(list_release_tracks),
        "track_list": list_release_tracks
    }
