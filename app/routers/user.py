from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from models import UserModel, UserViewModel, UserUpdateModel
from schemas import User
from utility import db as db_util, user as user_util

router = APIRouter(prefix="/users", tags=["User"])

db_context = db_util.get_db_context

@router.get("", status_code=status.HTTP_200_OK, response_model=list[UserViewModel])
async def get_all_users(db: Session = Depends(db_context)):
    return db.query(User).all()

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserViewModel)
async def create_user(request: UserModel, db: Session = Depends(db_context)) -> None:
    user = User(**request.model_dump())
    user.password = user_util.get_password_hash(user.password)
    user.created_at = datetime.now(timezone.utc)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{user_id}", response_model=UserViewModel)
async def get_user(user_id: str, db: Session = Depends(db_context)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserViewModel)
async def update_user(user_id: str, request: UserUpdateModel, db: Session = Depends(db_context)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    for field, value in request.model_dump().items():
        setattr(user, field, value)
    user.updated_at = datetime.now(timezone.utc)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
