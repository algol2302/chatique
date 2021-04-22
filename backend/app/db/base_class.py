from typing import Any

from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any

    created_at = Column(
        DateTime,
        default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    deleted_at = Column(
        DateTime,
        nullable=True,
        default=None
    )

    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
