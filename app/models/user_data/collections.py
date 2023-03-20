from datetime import datetime

from app.db import rr_metadata
from app.models.enums import ConditionType
from app.models.mixins import TimeStamp

from dataclasses import dataclass
import sqlalchemy


@dataclass
class Item():
    created_at: datetime
    updated_at: datetime
    id: int
    user_id: int
    release_id: int
    condition: str
    bought_price: int
    comment: str
    is_for_sale: bool
    is_sold: bool
    sold_price: int


# TODO: убрать таблицу Wishlist, добавить айтему параметр Status: (WANT_TO_BUY, IN_COLLECTION, FOR_SALE, SOLD, DELETED)


collection_table = sqlalchemy.Table(
    "collections",
    rr_metadata,
    TimeStamp.created_at.copy(),
    TimeStamp.updated_at.copy(),
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("release_id", sqlalchemy.Integer, nullable=False),  # TODO: add foreign key to mb_data.release id
    sqlalchemy.Column("condition", sqlalchemy.Enum(ConditionType), nullable=False, default=ConditionType.mint.name),
    sqlalchemy.Column("bought_price", sqlalchemy.Integer),
    sqlalchemy.Column("comment", sqlalchemy.Text),
    sqlalchemy.Column("is_for_sale", sqlalchemy.Boolean, server_default='false'),
    sqlalchemy.Column("is_sold", sqlalchemy.Boolean, server_default='false'),
    sqlalchemy.Column("sold_price", sqlalchemy.Integer),
)
