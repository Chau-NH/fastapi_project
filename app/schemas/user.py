from sqlalchemy import Boolean, Column, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship
from database import Base
from .base_entity import BaseEntity

class User(Base, BaseEntity):
    __tablename__ = "users"

    email = Column(String, unique=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default= False)
    company_id = Column(Uuid, ForeignKey('companies.id'))
    
    # Relationships
    company = relationship('Company')