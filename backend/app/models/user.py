from sqlalchemy import Boolean, Column, String
from sqlalchemy.ext.associationproxy import association_proxy

from db.base_class import Base


class User(Base):
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=72), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    # association proxy of "user_companies" collection
    # to "company" attribute
    companies = association_proxy('user_companies', 'company')
