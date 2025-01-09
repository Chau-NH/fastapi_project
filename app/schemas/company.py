from sqlalchemy import Column, Integer, String
from database import Base
from .base_entity import BaseEntity

class Company(Base, BaseEntity):
    __tablename__ = "companies"

    name = Column(String, nullable=False)
    description = Column(String)
    rating = Column(Integer)