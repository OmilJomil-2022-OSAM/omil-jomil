from typing import Optional

from pydantic import BaseModel, Field

from core.schema_core import AllOptional


# Shared properties
class UserBase(BaseModel):
    name: str = Field(title="aaaaa")
    uid: str
    password: str
    number: str


# Properties to receive on item creation
class UserCreate(UserBase):
    pass


# Properties to receive on item update
class UserUpdate(UserBase, metaclass=AllOptional):
    pass

class UserDisplay(UserBase):
    pass


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    # id: int
    # title: str
    # owner_id: int

    class Config:
        orm_mode = True
