from sqlalchemy import Column, Enum, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship
from database import Base
from .base_entity import BaseEntity, Status, Priority

class Task(Base, BaseEntity):
    __tablename__ = "tasks"

    summary = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(Status), default=Status.OPEN)
    priority = Column(Enum(Priority), default=Priority.MEDIUM)
    reporter_id = Column(Uuid, ForeignKey("users.id"), nullable=False)
    assignee_id = Column(Uuid, ForeignKey("users.id"))

    reporter = relationship("User", foreign_keys="Task.reporter_id")
    assignee = relationship("User", foreign_keys="Task.assignee_id")
