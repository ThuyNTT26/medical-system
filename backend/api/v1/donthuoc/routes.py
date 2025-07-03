from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from . import services, schemas

router = APIRouter(prefix="/donthuoc", tags=["DonThuoc"])

@router.get("/", response_model=list[schemas.DonThuocResponse])
def get_all(db: Session = Depends(get_db)):
    return services.get_all(db)

@router.post("/", response_model=schemas.DonThuocResponse)
def create_don(data: schemas.DonThuocCreate, db: Session = Depends(get_db)):
    return services.create(db, data)

@router.put("/{ma_don}", response_model=schemas.DonThuocResponse)
def update_don(ma_don: str, data: schemas.DonThuocUpdate, db: Session = Depends(get_db)):
    don = services.update(db, ma_don, data)
    if not don:
        raise HTTPException(status_code=404, detail="Không tìm thấy đơn thuốc")
    return don

@router.delete("/{ma_don}")
def delete_don(ma_don: str, db: Session = Depends(get_db)):
    if not services.delete(db, ma_don):
        raise HTTPException(status_code=404, detail="Không tìm thấy đơn thuốc")
    return {"message": "Đã xoá đơn thuốc"}

