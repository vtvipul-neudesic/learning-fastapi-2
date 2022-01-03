from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url="postgresql://postgres:root@localhost:5433/freecodecamp"

engine=create_engine(database_url)

localsession=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()