from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID

class CompanyModel(BaseModel):
    name: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    rating: Optional[int]

class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str
    rating: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
