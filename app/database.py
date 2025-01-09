from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import SQLALCHEMY_DB_URL

engine = create_engine(SQLALCHEMY_DB_URL)
metadata = MetaData()

LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()