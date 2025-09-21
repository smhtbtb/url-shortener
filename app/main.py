from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import routes, health
from app.db.session import Base, engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="URL Shortener", lifespan=lifespan)

# routers
app.include_router(health.router)
app.include_router(routes.router)
