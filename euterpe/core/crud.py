from sqlalchemy.orm import Session

from . import models, schemas


def get_spotify_account(db: Session, spotify_id: str):
    return db.query(models.SpotifyAccount).filter(models.SpotifyAccount.id == spotify_id).first()


def get_spotify_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SpotifyAccount).offset(skip).limit(limit).all()


def create_spotify_account(db: Session, account: schemas.SpotifyAccountCreate):
    db_account = models.SpotifyAccount(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_peering(db: Session, peering_id: int):
    return db.query(models.Peering).filter(models.Peering.id == peering_id).first()


def get_peerings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Peering).offset(skip).limit(limit).all()


def create_peering(db: Session, peering: schemas.PeeringCreate):
    db_peering = models.Peering(**peering.dict())
    db.add(db_peering)
    db.commit()
    db.refresh(db_peering)
    return db_peering
