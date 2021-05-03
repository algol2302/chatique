from sqlalchemy import Column, String
from sqlalchemy.ext.associationproxy import association_proxy

from db.base_class import Base


class Company(Base):
    name = Column(String(length=320), unique=True, index=True, nullable=False)
    # association proxy of "company_users" collection
    # to "user" attribute
    users = association_proxy('company_users', 'user')

