import os

#from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from breeze_service.settings import config

from breeze_service.settings import get_config
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASS.get_secret_value()}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, future=True, echo=True
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
