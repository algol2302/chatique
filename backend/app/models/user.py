from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from .mixins import BaseMixin

Base: DeclarativeMeta = declarative_base()


class User(Base, BaseMixin, SQLAlchemyBaseUserTable):
    pass
