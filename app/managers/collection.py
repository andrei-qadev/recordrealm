from pprint import pprint
from typing import List

from app.db import database
from app.models import collection_table, Item


class CollectionManager:
    @staticmethod
    async def get_collection(user) -> List[Item] | None:
        q = collection_table \
            .select() \
            .where(collection_table.c.user_id == user["id"])
        list_items: List[Item] = await database.fetch_all(q)
        return list_items

    @staticmethod
    async def add_item(user, item) -> Item:
        item["user_id"] = user.id
        q = collection_table \
            .insert() \
            .values(**item)
        id_ = await database.execute(q)
        item_db: Item = await database.fetch_one(
            collection_table.select()
            .where(collection_table.c.id == id_)
        )
        return item_db
