from pydantic import BaseModel


class ArtistOut(BaseModel):
    name: str
    id: int


class ArtistReleaseGroupOut(BaseModel):
    release_group_id: int
    release_group_name: str
    release_type: str