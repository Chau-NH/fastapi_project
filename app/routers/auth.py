from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utility import db as db_util
from services import auth as auth_services

router = APIRouter(prefix="/auth", tags=["Auth"])

db_context = db_util.get_db_context

@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(db_context)):

    user = auth_services.autheticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "access_token": auth_services.create_access_token(user, timedelta(minutes=10)),
        "token_type": "bearer"
    }