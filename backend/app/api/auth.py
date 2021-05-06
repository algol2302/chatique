import logging

from fastapi import Request
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase

from core.config import settings
from db.session import database
from models.user import User as UserModel
from schemas.user import User, UserCreate, UserUpdate, UserDB
from sevices.logger import get_logger

logger = get_logger(level=logging.DEBUG)

user_db = SQLAlchemyUserDatabase(UserDB, database, UserModel.__table__)


def on_after_register(user: UserDB, request: Request):
    logger.info(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    logger.info(
        f"User {user.id} has forgot their password. "
        f"Reset token: {token}"
    )


def after_verification_request(user: UserDB, token: str, request: Request):
    logger.info(
        f"Verification requested for user {user.id}. "
        f"Verification token: {token}"
    )

# TODO fix auth
jwt_authentication = JWTAuthentication(
    secret=settings.SECRET_KEY,
    lifetime_seconds=3600,
    tokenUrl="/auth/jwt/login",
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
