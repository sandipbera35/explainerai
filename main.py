from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from database.database import engine
from database.base import Base
from sqlalchemy import text
from database.schemas import users
from routers.user_router import userRouter 

@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)
    print()
    print("Database connected")
    print()

    yield

    print("Application shutdown")


app = FastAPI(
    lifespan=lifespan
)

app.include_router(userRouter)
@app.get("/")
async def root():
    return {"message": "FastAPI PostgreSQL Connected"}

