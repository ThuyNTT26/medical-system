'''from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan
from . import services, schemas

router = APIRouter(prefix="/phieukhambenh", tags=["PhieuKhamBenh"])

@router.get("/", response_model=list[schemas.PhieuKhamBenhResponse])
def get_all(db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.get_all(db)

@router.post("/", response_model=schemas.PhieuKhamBenhResponse)
def create_phieu(data: schemas.PhieuKhamBenhCreate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.create(db, data)

@router.put("/{ma_phieu}", response_model=schemas.PhieuKhamBenhResponse)
def update_phieu(ma_phieu: str, data: schemas.PhieuKhamBenhUpdate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    phieu = services.update(db, ma_phieu, data)
    if not phieu:
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu khám")
    return phieu

@router.delete("/{ma_phieu}")
def delete_phieu(ma_phieu: str, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    if not services.delete(db, ma_phieu):
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu khám")
    return {"message": "Đã xoá phiếu khám"}'''

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.api.v1.auth.models import TaiKhoan

from . import services, schemas

router = APIRouter(prefix="/phieukhambenh", tags=["PhieuKhamBenh"])

# Lấy toàn bộ phiếu khám bệnh
@router.get("/", response_model=list[schemas.PhieuKhamBenhResponse])
def get_all_phieu(
    db: Session = Depends(get_db),
):
    return services.get_all(db)

# Tạo phiếu khám bệnh mới
@router.post("/", response_model=schemas.PhieuKhamBenhResponse)
def create_phieu(
    data: schemas.PhieuKhamBenhCreate,
    db: Session = Depends(get_db),
):
    return services.create(db, data)

# Cập nhật phiếu khám bệnh
@router.put("/{ma_phieu}", response_model=schemas.PhieuKhamBenhResponse)
def update_phieu(
    ma_phieu: str,
    data: schemas.PhieuKhamBenhUpdate,
    db: Session = Depends(get_db),
    
):
    phieu = services.update(db, ma_phieu, data)
    if not phieu:
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu khám")
    return phieu

# Xoá phiếu khám bệnh
@router.delete("/{ma_phieu}")
def delete_phieu(
    ma_phieu: str,
    db: Session = Depends(get_db),
   
):
    if not services.delete(db, ma_phieu):
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu khám")
    return {"message": "Đã xoá phiếu khám"}

