from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from . import schemas, services

router = APIRouter(tags=["Bệnh nhân"])

@router.get("/", response_model=list[schemas.BenhNhanOut])
def get_all(db: Session = Depends(get_db)):
    return services.get_all(db)

@router.get("/{id}", response_model=schemas.BenhNhanOut)
def get_by_id(id: int, db: Session = Depends(get_db)):
    bn = services.get_by_id(db, id)
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")
    return bn

@router.post("/", response_model=schemas.BenhNhanOut)
def create(data: schemas.BenhNhanCreate, db: Session = Depends(get_db)):
    return services.create(db, data)

@router.put("/{id}", response_model=schemas.BenhNhanOut)
def update(id: int, data: schemas.BenhNhanUpdate, db: Session = Depends(get_db)):
    return services.update(db, id, data)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    if not services.delete(db, id):
        raise HTTPException(status_code=404, detail="Xoá thất bại")
    return {"message": "Xoá thành công"}

@router.get("/{id}/hosos")
def get_hoso(id: int, db: Session = Depends(get_db)):
    return services.get_hoso_chi_tiet(db, id)
