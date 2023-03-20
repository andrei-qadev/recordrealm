from typing import Optional, List

from pydantic import BaseModel

from app.schemas.response.track import TrackOut


class ReleaseOut(BaseModel):
    artist_credit_id: int
    artist_credit_name: str
    country_name: str
    id: int
    label_name: str
    packaging: str
    release_group_id: int
    release_group_name: str
    release_type: str
    year: int


class ReleaseTracksOut(BaseModel):
    total_tracks: int
    track_list: List[TrackOut]
