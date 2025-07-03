from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Bệnh nhân"])

@router.get("/", response_model=list[schemas.BenhNhanOut])
def get_all(db: Session = Depends(get_db)):
    return services.get_all(db)

@router.get("/{ma_benh_nhan}", response_model=schemas.BenhNhanOut)
def get_by_id(ma_benh_nhan: str, db: Session = Depends(get_db)):
    bn = services.get_by_id(db, ma_benh_nhan)
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")
    return bn

@router.post("/", response_model=schemas.BenhNhanOut)
def create(data: schemas.BenhNhanCreate, db: Session = Depends(get_db)):
    return services.create(db, data)

@router.put("/{ma_benh_nhan}", response_model=schemas.BenhNhanOut)
def update(ma_benh_nhan: str, data: schemas.BenhNhanUpdate, db: Session = Depends(get_db)):
    return services.update(db, ma_benh_nhan, data)

@router.delete("/{ma_benh_nhan}")
def delete(ma_benh_nhan: str, db: Session = Depends(get_db)):
    if not services.delete(db, ma_benh_nhan):
        raise HTTPException(status_code=404, detail="Xoá thất bại")
    return {"message": "Xoá thành công"}

@router.get("/{ma_benh_nhan}/hosos", response_model=schemas.HoSoChiTietOut)
def get_hoso(ma_benh_nhan: str, db: Session = Depends(get_db)):
    return services.get_hoso_chi_tiet(db, ma_benh_nhan)
