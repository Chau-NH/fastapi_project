from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate
from starlette import status
from sqlalchemy.orm import Session
from utility.db import get_db_context
from models.task import TaskModel, TaskViewModel
from services import auth as auth_service
from schemas import Task, User

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("", status_code=status.HTTP_200_OK)
async def get_tasks(
        db: Session = Depends(get_db_context),
        user: User = Depends(auth_service.token_interceptor)
    ) -> Page[TaskViewModel]:
    tasks = db.query(Task).all()
    return paginate(tasks)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task(
        request: TaskModel, 
        db: Session = Depends(get_db_context), 
        user: User = Depends(auth_service.token_interceptor)
    ) -> TaskViewModel:

    task = Task(**request.model_dump())
    task.reporter_id = user.id
    task.created_at = datetime.now(timezone.utc)

    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

@router.get("/{task_id}", response_model=TaskViewModel)
async def get_task(
        task_id: str,
        db: Session = Depends(get_db_context),
        user: User = Depends(auth_service.token_interceptor)
    ):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskViewModel)
async def update_task(
        task_id: str, 
        request: TaskModel, 
        db: Session = Depends(get_db_context),
        user: User = Depends(auth_service.token_interceptor)
    ):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for field, value in request.model_dump().items():
        setattr(task, field, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
