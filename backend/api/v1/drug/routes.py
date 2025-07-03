from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from . import services, schemas

router = APIRouter(tags=["Thuoc"])

@router.get("/", response_model=list[schemas.ThuocResponse])
def get_all(db: Session = Depends(get_db)):
    return services.get_all_thuoc(db)

@router.get("/search", response_model=list[schemas.ThuocResponse])
def search(keyword: str, db: Session = Depends(get_db)):
    return services.search_thuoc(db, keyword)

@router.post("/", response_model=schemas.ThuocResponse)
def create(data: schemas.ThuocCreate, db: Session = Depends(get_db)):
    return services.create_thuoc(db, data)

@router.put("/{ma_thuoc}", response_model=schemas.ThuocResponse)
def update(ma_thuoc: str, data: schemas.ThuocUpdate, db: Session = Depends(get_db)):
    return services.update_thuoc(db, ma_thuoc, data)

@router.delete("/{ma_thuoc}")
def delete(ma_thuoc: str, db: Session = Depends(get_db)):
    return services.delete_thuoc(db, ma_thuoc)
