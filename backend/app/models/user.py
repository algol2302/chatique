from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.ext.associationproxy import association_proxy
from db.base_class import Base


class User(Base, SQLAlchemyBaseUserTable):
    # association proxy of "user_companies" collection
    # to "company" attribute
    companies = association_proxy('user_companies', 'company')

