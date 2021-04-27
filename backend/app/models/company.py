from sqlalchemy import Column, String

from db.base_class import Base


class Company(Base):
    name = Column(String(length=320), unique=True, index=True, nullable=False)
