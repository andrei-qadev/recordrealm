"""
user collection endpoint
"""
from typing import List
from dataclasses import fields

from fastapi import APIRouter, HTTPException, Depends
from starlette.requests import Request

from app.managers.auth import oauth2_scheme
from app.managers.collection import CollectionManager
from app.schemas.request.collection import ReleaseIn
from app.schemas.response.collection import CollectionItemOut

router = APIRouter(tags=["Collection"])


@router.post("/collection",
             status_code=201,
             summary="add release to collection",
             dependencies=[Depends(oauth2_scheme)],
             response_model=CollectionItemOut
             )
async def add_item(request: Request, user_release: ReleaseIn):
    user = request.state.user
    item_db = await CollectionManager.add_item(
        user=user,
        item=user_release.dict()
    )
    return item_db


@router.get("/collection/releases",
            summary="shows all releases that were added by user",
            dependencies=[Depends(oauth2_scheme)],
            response_model=List[CollectionItemOut]
            )
async def get_collection(request: Request):
    user = request.state.user
    return await CollectionManager.get_collection(user=user)


@router.get("/collection/releases/{release_id}",
            summary="returns info about the release added to user's collection",
            dependencies=[Depends(oauth2_scheme)],
            response_model=CollectionItemOut
            )
async def get_collection_release(request: Request):
    ...
