from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from . import services, schemas

router = APIRouter( tags=["ThanhToan"])

@router.get("/", response_model=list[schemas.ThanhToanOut])
def get_all(db: Session = Depends(get_db)):

    return services.get_all_thanh_toan(db)

@router.get("/search", response_model=list[schemas.ThanhToanOut])
def search(keyword: str, db: Session = Depends(get_db)):
    return services.search_thanh_toan(db, keyword)

@router.post("/", response_model=schemas.ThanhToanOut)
def create(data: schemas.ThanhToanCreate, db: Session = Depends(get_db)):
    return services.create_thanh_toan(db, data)

@router.put("/{ma_hoa_don}", response_model=schemas.ThanhToanOut)
def update(ma_hoa_don: str, data: schemas.ThanhToanUpdate, db: Session = Depends(get_db)):
    return services.update_thanh_toan(db, ma_hoa_don, data)

@router.delete("/{ma_hoa_don}")
def delete(ma_hoa_don: str, db: Session = Depends(get_db)):
    return services.delete_thanh_toan(db, ma_hoa_don)
