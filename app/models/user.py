from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from .company import CompanyViewModel

class UserModel(BaseModel):
    username: str = Field(min_length=6)
    password: str = Field(min_length=6, max_length=20)
    first_name: str
    last_name: str
    email: Optional[str]
    company_id: Optional[UUID]

class UserBaseModel(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    first_name: str
    last_name: str
    class Config:
        from_attributes = True
    
class UserViewModel(UserBaseModel):
    company_id: UUID | None = None
    company: CompanyViewModel | None = None
    is_active: bool
    is_admin: bool
    created_at: datetime | None = None
    updated_at: datetime | None = None
