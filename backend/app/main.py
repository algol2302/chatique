import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api_v1 import router
from core.config import settings
from db.session import database

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router.api_router, prefix=settings.API_V1_STR)


@app.on_event('startup')
async def on_startup() -> None:
    await database.connect()


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await database.disconnect()


DEBUG = os.getenv("DEBUG") == 'True'


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


if __name__ == "__main__" and DEBUG:
    import uvicorn
    uvicorn.run("main:app", debug=True, reload=True)
