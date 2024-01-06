from fastapi import FastAPI
from pypox import createAsyncEngine, getAsyncEngine
from pypox.database import init_database_async
from gamedle.database.SQLITE import GamedleDatabase

createAsyncEngine(GamedleDatabase, "aiosqlite", echo=True)


async def __call__(app: FastAPI):
    await init_database_async(getAsyncEngine(GamedleDatabase), GamedleDatabase)
