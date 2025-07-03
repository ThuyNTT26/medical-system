# backend/api/v1/appointment/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, services
from backend.core.database import get_db

router = APIRouter(tags=["Lịch hẹn khám"])

@router.get("/", response_model=list[schemas.LichHenOut])
def get_all(db: Session = Depends(get_db)):
    return services.get_all(db)

@router.get("/{id}", response_model=schemas.LichHenOut)
def get_one(id: str, db: Session = Depends(get_db)):
    lh = services.get_by_id(db, id)
    if not lh:
        raise HTTPException(status_code=404, detail="Không tìm thấy")
    return lh

@router.post("/", response_model=schemas.LichHenOut)
def create(data: schemas.LichHenCreate, db: Session = Depends(get_db)):
    return services.create(db, data)

@router.put("/{id}", response_model=schemas.LichHenOut)
def update(id: str, data: schemas.LichHenUpdate, db: Session = Depends(get_db)):
    lh = services.update(db, id, data)
    if not lh:
        raise HTTPException(status_code=404, detail="Không tìm thấy")
    return lh

@router.delete("/{id}")
def delete(id: str, db: Session = Depends(get_db)):
    if not services.delete(db, id):
        raise HTTPException(status_code=404, detail="Không tìm thấy")
    return {"message": "Xoá thành công"}
