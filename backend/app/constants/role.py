from enum import Enum, unique


@unique
class Roles(Enum):
    OWNER = 'OWNER'
    ADMIN = 'ADMIN'
    USER = 'USER'
