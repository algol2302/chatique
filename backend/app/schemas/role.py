from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from constants.role import Roles


# Shared properties
class RoleBase(BaseModel):
    id: Optional[UUID] = None
    role: Roles = Roles.USER
    company_id: UUID
    user_id: UUID

    class Config:
        use_enum_values = True


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
