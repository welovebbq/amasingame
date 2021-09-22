from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_mmt(db: Session, user_id: int):
    return db.query(models.MetamaskTwitch).filter(models.MetamaskTwitch.user_id == user_id).first()
