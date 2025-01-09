from fastapi import APIRouter, Depends, HTTPException
from starlette import status

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("", status_code=status.HTTP_200_OK)
async def get_tasks():
    return "All tasks"