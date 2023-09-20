from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .core import crud, schemas
from .core import models
from .core.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Welcome to euterpe"}


@app.post("/peering/", response_model=schemas.Peering)
def create_peering(peering: schemas.PeeringCreate, db: Session = Depends(get_db)):
    # db_peering = crud.get_peering_by_email(db, email=peering.email)
    # if db_peering:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_peering(db=db, peering=peering)


@app.get("/peerings/", response_model=list[schemas.Peering])
def read_peerings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    peerings = crud.get_peerings(db, skip=skip, limit=limit)
    return peerings


@app.post("/account/", response_model=schemas.SpotifyAccount)
def create_account(account: schemas.SpotifyAccountCreate, db: Session = Depends(get_db)):
    return crud.create_spotify_account(db=db, account=account)


@app.get("/accounts/", response_model=list[schemas.SpotifyAccount])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_spotify_accounts(db, skip=skip, limit=limit)
