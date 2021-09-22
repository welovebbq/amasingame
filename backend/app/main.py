from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

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
    return {"message": "Hello World4"}


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/details/{user_id}", response_model=schemas.MetamaskTwitch)
def read_mmt(user_id: int, db: Session = Depends(get_db)):
    db_mmt = crud.get_mmt(db, user_id=user_id)
    if db_mmt is None:
        raise HTTPException(status_code=404, detail="Details for user not found")
    return db_mmt
