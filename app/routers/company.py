from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from models import CompanyModel, CompanyViewModel
from schemas import Company, User
from services import auth as auth_service
from utility import db

router = APIRouter(prefix="/companies", tags=["Company"])

db_context = db.get_db_context

@router.get("", response_model=list[CompanyViewModel])
async def get_companies(
        user: User = Depends(auth_service.token_interceptor),
        db: Session = Depends(db_context)
    ):
    return db.query(Company).all()

@router.post("", status_code=status.HTTP_201_CREATED, response_model=CompanyViewModel)
async def create_company(
        request: CompanyModel,
        user: User = Depends(auth_service.token_interceptor),
        db: Session = Depends(db_context)
    ):
    company = Company(**request.model_dump())
    company.created_at = datetime.now(timezone.utc)
    db.add(company)
    db.commit()
    db.refresh(company)

    return company

@router.get("/{company_id}", response_model=CompanyViewModel)
async def get_company(
        company_id: str, 
        user: User = Depends(auth_service.token_interceptor), 
        db: Session = Depends(db_context)
    ):
    company = db.query(Company).filter(Company.id == company_id).one_or_none()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.put("/{company_id}", response_model=CompanyViewModel)
async def update_company(
        company_id: str,
        request: CompanyModel, 
        user: User = Depends(auth_service.token_interceptor), 
        db: Session = Depends(db_context)
    ):
    company = db.query(Company).filter(Company.id == company_id).one_or_none()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    for field, value in request.model_dump().items():
        setattr(company, field, value)

    company.updated_at = datetime.now(timezone.utc)
    db.add(company)
    db.commit()
    db.refresh(company)

    return company

