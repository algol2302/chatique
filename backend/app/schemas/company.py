from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class CompanyBase(BaseModel):
    id: Optional[UUID] = None
    name: str


# Properties to receive via API on creation
class CompanyCreate(CompanyBase):
    pass


# Properties to receive via API on update
class CompanyUpdate(CompanyBase):
    pass


class CompanyInDBBase(CompanyBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Company(CompanyInDBBase):
    pass


# Additional properties stored in DB
class CompanyInDB(CompanyInDBBase):
    pass
