from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class RoleBase(BaseModel):
    id: Optional[UUID] = None
    role: int


# Properties to receive via API on creation
class RoleCreate(RoleBase):
    pass


# Properties to receive via API on update
class RoleUpdate(RoleBase):
    pass


class RoleInDBBase(RoleBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Role(RoleInDBBase):
    pass


# Additional properties stored in DB
class RoleInDB(RoleInDBBase):
    pass
