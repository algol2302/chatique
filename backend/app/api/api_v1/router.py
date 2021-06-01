from fastapi import APIRouter

from api.api_v1.endpoints import login, users, chat

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(chat.router, tags=["chat"])
