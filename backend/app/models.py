from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class MetamaskTwitch(Base):
    __tablename__ = "metamask_twitch"

    user_id = Column(Integer, ForeignKey("users.id"))
    twitch_handle = Column(String, index=True, primary_key=True)
    metamask_id = Column(String, index=True, primary_key=True)
