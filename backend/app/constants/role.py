# https://fastapi.tiangolo.com/tutorial/path-params/#working-with-python-enumerations

from enum import Enum, unique


class Roles(str, Enum):
    OWNER = 'OWNER'
    ADMIN = 'ADMIN'
    USER = 'USER'
