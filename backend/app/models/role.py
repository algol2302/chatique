from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import backref, relationship

from db.base_class import Base
from constants import Roles
from .user import User
from .company import Company


class Role(Base):
    role = Column(pg.ENUM(Roles), unique=False, nullable=False)

    user_id = Column(
        pg.UUID(as_uuid=True),
        ForeignKey('user.id'),
        primary_key=True
    )

    company_id = Column(
        pg.UUID(as_uuid=True),
        ForeignKey('company.id'),
        primary_key=True
    )

    # bidirectional attribute/collection of "user"/"user_companies"
    user = relationship(
        User,
        backref=backref(
            "user_companies",
            cascade="all, delete-orphan"
        )
    )

    # bidirectional attribute/collection of "company"/"company_users"
    company = relationship(
        Company,
        backref=backref(
            "company_users",
            cascade="all, delete-orphan"
        )
    )
