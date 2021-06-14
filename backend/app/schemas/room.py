from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class RoomBase(BaseModel):
    id: Optional[UUID] = None
    name: str = "general"
    company_id: UUID


# Properties to receive via API on creation
class RoomCreate(RoomBase):
    pass


# Properties to receive via API on update
class RoomUpdate(RoomBase):
    pass


class RoomInDBBase(RoomBase):

    class Config:
        orm_mode = True


# Additional properties to return via API
class Room(RoomInDBBase):
    pass


# Additional properties stored in DB
class RoomInDB(RoomInDBBase):
    pass
