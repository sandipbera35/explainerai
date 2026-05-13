# DATABASE_URL = "postgresql+asyncpg://sandipbera35:1221@localhost:5432/explainerai"
DATABASE_URL = "postgresql+psycopg2://sandipbera35:1221@localhost:5432/explainerai"


from sqlalchemy.engine import create_engine

from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()