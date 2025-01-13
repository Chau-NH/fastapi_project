from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from schemas.base_entity import Status, Priority
from .user import UserViewModel


class TaskModel(BaseModel):
    summary: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    status: Status = Field(default=Status.OPEN)
    priority: Priority = Field(default=Priority.MEDIUM)
    assignee_id: Optional[UUID] | None = None

class TaskViewModel(BaseModel):
    id: UUID
    summary: str
    description: str
    status: Status | None = None
    priority: Priority | None = None
    reporter: UserViewModel | None = None
    assignee: UserViewModel | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    class Config:
        from_attributes = True
