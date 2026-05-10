DATABASE_URL = "postgresql+asyncpg://sandipbera35:1221@localhost:5432/explainerai"
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)


engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session