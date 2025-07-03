from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan
from . import services, schemas

router = APIRouter(prefix="/benh", tags=["Benh"])

@router.get("/", response_model=list[schemas.BenhResponse])
def get_all(db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.get_all(db)

from fastapi import HTTPException

@router.post("/", response_model=schemas.BenhResponse)
def create_benh(data: schemas.BenhCreate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.create(db, data)

@router.put("/{ma_benh}", response_model=schemas.BenhResponse)
def update_benh(ma_benh: str, data: schemas.BenhUpdate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    result = services.update(db, ma_benh, data)
    if not result:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh")
    return result

@router.delete("/{ma_benh}")
def delete_benh(ma_benh: str, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    if not services.delete(db, ma_benh):
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh")
    return {"message": "Đã xoá thành công"}
