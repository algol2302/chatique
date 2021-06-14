from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class MessageBase(BaseModel):
    id: Optional[UUID] = None
    room_id: UUID
    txt: str


# Properties to receive via API on creation
class MessageCreate(MessageBase):
    pass


# Properties to receive via API on update
class MessageUpdate(MessageBase):
    pass


class MessageInDBBase(MessageBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class Message(MessageInDBBase):
    pass


# Additional properties stored in DB
class MessageInDB(MessageInDBBase):
    pass
