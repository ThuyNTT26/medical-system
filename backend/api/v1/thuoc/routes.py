from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan
from . import services, schemas

router = APIRouter(prefix="/thuoc", tags=["Thuoc"])

@router.get("/", response_model=list[schemas.ThuocResponse])
def get_all(db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.get_all(db)

@router.post("/", response_model=schemas.ThuocResponse)
def create_thuoc(data: schemas.ThuocCreate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.create(db, data)

@router.put("/{ma_thuoc}", response_model=schemas.ThuocResponse)
def update_thuoc(ma_thuoc: str, data: schemas.ThuocUpdate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    thuoc = services.update(db, ma_thuoc, data)
    if not thuoc:
        raise HTTPException(status_code=404, detail="Không tìm thấy thuốc")
    return thuoc

@router.delete("/{ma_thuoc}")
def delete_thuoc(ma_thuoc: str, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    if not services.delete(db, ma_thuoc):
        raise HTTPException(status_code=404, detail="Không tìm thấy thuốc")
    return {"message": "Đã xoá thuốc"}
