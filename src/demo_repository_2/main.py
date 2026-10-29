from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .tasks import init_db, router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(title="Demo Repository API", lifespan=lifespan)
app.include_router(tasks_router)


@app.get("/echo/{message}")
def echo(message: str) -> dict[str, str]:
    """Return the message supplied in the URL."""
    return {"message": message}