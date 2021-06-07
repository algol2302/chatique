import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column, ForeignKey, Text

from db.base_class import Base


class Message(Base):
    room_id = Column(
        pg.UUID(as_uuid=True),
        ForeignKey('room.id')
    )

    text = Column(
        Text,
        nullable=False
    )
