import asyncio
from typing import List

from app.db import database
from app.models import collection_table, Item


async def check():
    await database.connect()

    user = {"id": 4}

    q = collection_table \
        .select() \
        .where(collection_table.c.user_id == user["id"])
    list_releases: List[Item] = await database.fetch_all(q)

    print(list_releases)
    for release in list_releases:
        print(release.created_at)

    await database.disconnect()


asyncio.run(check())
