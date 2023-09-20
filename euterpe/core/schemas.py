from pydantic import BaseModel


class SpotifyAccountBase(BaseModel):
    client_id: str
    client_secret: str


class SpotifyAccountCreate(SpotifyAccountBase):
    pass


class SpotifyAccount(SpotifyAccountBase):
    id: int

    class Config:
        from_attributes = True


class PeeringBase(BaseModel):
    nfc_id: int
    spotify_id: int | None = None


class PeeringCreate(PeeringBase):
    pass


class Peering(PeeringBase):
    id: int

    class Config:
        from_attributes = True
