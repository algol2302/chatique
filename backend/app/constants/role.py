from enum import Enum, unique


@unique
class Roles(Enum):
    OWNER = 1
    ADMIN = 2
    USER = 3
