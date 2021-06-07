import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column, String, ForeignKey

from db.base_class import Base


class Room(Base):
    name = Column(
        String(length=120),
        unique=True,
        index=True,
        nullable=False
    )

    company_id = Column(
        pg.UUID(as_uuid=True),
        ForeignKey('company.id')
    )
