from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from database.database import engine
from database.base import Base
from sqlalchemy import text
from database.schemas import users
from routers.user_router import userRouter 
from routers.ai_router import aiRouter

from sqlalchemy import text
Base.metadata.create_all(bind=engine)
with engine.connect() as conn:

    conn.execute(text("""
        ALTER TABLE users
        ADD COLUMN IF NOT EXISTS guid VARCHAR
    """))

    conn.commit()


app = FastAPI( debug=True, title="ExplainerAI API", description="API for ExplainerAI application", version="1.0.0" )

app.include_router(userRouter, prefix="/api/v1", tags=["Users"])
app.include_router(aiRouter, prefix="/api/v1", tags=["AI"])
@app.get("/")
def root():
    return {"message": "FastAPI PostgreSQL Connected"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

