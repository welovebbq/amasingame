from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class MetamaskTwitchBase(BaseModel):
    twitch_handle: str
    metamask_id: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class MetamaskTwitch(MetamaskTwitchBase):
    user_id: int

    class Config:
        orm_mode = True
