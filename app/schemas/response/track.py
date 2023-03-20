from typing import Optional

from pydantic import BaseModel


class TrackOut(BaseModel):
    id: int
    name: str
    length: int
    medium_position: int
    track_position: int
    release_id: int
