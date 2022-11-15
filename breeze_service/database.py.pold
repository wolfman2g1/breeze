import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from breeze_service.settings import get_config

db_host=get_config().DB_HOST
db_user=get_config().DB_USER
db_pass=get_config().DB_PASS
db_name=get_config().DB_NAME
db_port=get_config().DB_PORT

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
            yield db
    finally:
        db.close()