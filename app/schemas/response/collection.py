from pydantic import BaseModel, validator

from app.models.enums import ConditionType
from app.schemas.response.release import ReleaseOut


class CollectionItemOut(BaseModel):
    id: int
    release: ReleaseOut
    condition: ConditionType
    bought_for: int | None
    comment: str
    is_for_sale: bool
    is_sold: bool
    sold_for: int | None
