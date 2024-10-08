from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import settings

SQLALCHEMY_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/practice'

engine = create_engine(SQLALCHEMY_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base()


def get_db(): 
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()