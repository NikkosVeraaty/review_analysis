from contextlib import asynccontextmanager

import sqlite3
from fastapi import FastAPI

from core.config import settings
from core.db_helper import create_reviews_table
from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    connection = sqlite3.connect(database=settings.db.name)
    app.state.connection = connection
    create_reviews_table(connection=connection)
    yield
    app.state.connection.close()


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
