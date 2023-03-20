from typing import Optional
from app.models.enums import ConditionType

from pydantic import BaseModel


class ReleaseIn(BaseModel):
    release_id: int
    condition: ConditionType = ConditionType.mint
    bought_for: Optional[int] = None
    comment: Optional[str] = ''
