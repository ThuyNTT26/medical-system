'''from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan
from . import services, schemas

router = APIRouter(prefix="/chitiet-donthuoc", tags=["ChiTietDonThuoc"])

@router.get("/", response_model=list[schemas.ChiTietDonThuocResponse])
def get_all(db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.get_all(db)

@router.post("/", response_model=schemas.ChiTietDonThuocResponse)
def create_chitiet(data: schemas.ChiTietDonThuocCreate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.create(db, data)

@router.put("/{ma_don}/{ma_thuoc}", response_model=schemas.ChiTietDonThuocResponse)
def update_chitiet(ma_don: str, ma_thuoc: str, data: schemas.ChiTietDonThuocUpdate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    result = services.update(db, ma_don, ma_thuoc, data)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy chi tiết đơn thuốc")
    return result

@router.delete("/{ma_don}/{ma_thuoc}")
def delete_chitiet(ma_don: str, ma_thuoc: str, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    if not services.delete(db, ma_don, ma_thuoc):
        raise HTTPException(status_code=404, detail="Không tìm thấy chi tiết đơn thuốc")
    return {"message": "Đã xoá chi tiết đơn thuốc"}'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from . import services, schemas

router = APIRouter(prefix="/chitiet-donthuoc", tags=["ChiTietDonThuoc"])

@router.get("/", response_model=list[schemas.ChiTietDonThuocResponse])
def get_all(db: Session = Depends(get_db)):
    return services.get_all(db)

@router.post("/", response_model=schemas.ChiTietDonThuocResponse)
def create_chitiet(data: schemas.ChiTietDonThuocCreate, db: Session = Depends(get_db)):
    return services.create(db, data)

@router.put("/{ma_don}/{ma_thuoc}", response_model=schemas.ChiTietDonThuocResponse)
def update_chitiet(ma_don: str, ma_thuoc: str, data: schemas.ChiTietDonThuocUpdate, db: Session = Depends(get_db)):
    result = services.update(db, ma_don, ma_thuoc, data)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy chi tiết đơn thuốc")
    return result

@router.delete("/{ma_don}/{ma_thuoc}")
def delete_chitiet(ma_don: str, ma_thuoc: str, db: Session = Depends(get_db)):
    if not services.delete(db, ma_don, ma_thuoc):
        raise HTTPException(status_code=404, detail="Không tìm thấy chi tiết đơn thuốc")
    return {"message": "Đã xoá chi tiết đơn thuốc"}

