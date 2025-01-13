from enum import Enum
from sqlalchemy import Column, Uuid, Time
import uuid

class BaseEntity:
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)

class Status(Enum):
    OPEN = "open"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
