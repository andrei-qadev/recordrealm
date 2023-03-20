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


class Collection:
    @staticmethod
    @router.get("/collection/items",
                summary="shows all releases that were added by user",
                dependencies=[Depends(oauth2_scheme)],
                response_model=List[CollectionItemOut]
                )
    async def list_collection_items(request: Request):
        user = request.state.user
        return await CollectionManager.get_collection(user=user)

    @staticmethod
    async def get_collection_stats():
        """
        returns the following stats:
        number of items in current collection
        number of items for sale
        number of items sold
        number of items in wishlist
        total cost of items in the collection
        total cost of items for sale
        total cost of sold items
        total cost of items in wishlist

        """
        ...


class Item:
    @staticmethod
    @router.post("/collection/items",
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

    @staticmethod
    @router.get("/collection/items/{item_id}",
                summary="returns info about the item (release and meta) added to user's collection",
                dependencies=[Depends(oauth2_scheme)],
                response_model=CollectionItemOut
                )
    async def get_item_by_id(request: Request, item_id: int):
        ...

    async def remove_item():
        ...

    async def edit_item():
        ...

    async def find_item_by_release_name():
        ...


class Sales:
    async def mark_item_for_sale():
        ...

    async def unmark_item_from_sale():
        ...

    async def sell_item():
        ...

    async def revert_sale():
        ...

    async def edit_sold_price():
        ...
