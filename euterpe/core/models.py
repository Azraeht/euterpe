from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class SpotifyAccount(Base):
    __tablename__ = "spotify_accounts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, index=True)
    client_secret = Column(String, index=True)


class Peering(Base):
    __tablename__ = "peering"

    id = Column(Integer, primary_key=True, index=True)
    nfc_id = Column(Integer, index=True)
    song_id = Column(Integer, index=True)
