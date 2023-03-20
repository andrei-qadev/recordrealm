from starlette.middleware.cors import CORSMiddleware

from app.db import database
from typing import Final

from fastapi import FastAPI
from decouple import config
from app.api.routers import auth
from app.api.routers import collection
from app.api.routers import artist
from app.api.routers import release

API_PREFIX: Final = "/api/"

# api_router = APIRouter()
app: FastAPI = FastAPI(
    title=f"{config('ENV')}",
    docs_url='/docs',
    redoc_url=None
)

app.include_router(auth.router)
app.include_router(collection.router)
app.include_router(artist.router)
app.include_router(release.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
