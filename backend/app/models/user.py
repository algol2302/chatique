from fastapi_users.db import SQLAlchemyBaseUserTable

from db.base_class import Base


class User(Base, SQLAlchemyBaseUserTable):
    pass
