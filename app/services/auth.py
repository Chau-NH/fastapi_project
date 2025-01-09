from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from typing import Optional
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from schemas import User
from utility.user import vevify_password
from settings import JWT_ALGORITHM, JWT_SECRET

oa2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

def autheticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not vevify_password(password, user.password):
        return False
    return user

def create_access_token(user: User, expires: Optional[timedelta] = None):
    claims = {
        "sub": user.username,
        "id": str(user.id),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_admin": user.is_admin
    }
    expires_in = datetime.now(timezone.utc) + expires if expires else datetime.now(timezone.utc) + timedelta(minutes=5)
    claims.update({"exp": expires_in})
    return jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM)

def token_interceptor(token: str = Depends(oa2_bearer)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = User()
        user.username = payload.get("sub")
        user.id = payload.get("id")
        user.first_name = payload.get("first_name")
        user.last_name = payload.get("last_name")
        user.is_admin = payload.get("is_admin")

        if (user.username is None or user.id is None):
            raise HTTPException(status_code=401, detail="Invalid credential", headers={"WWW-Authenticate": "bearer"})
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credential", headers={"WWW-Authenticate": "bearer"})
