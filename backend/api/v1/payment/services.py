from sqlalchemy.orm import Session
from . import models, schemas

def get_all_thanh_toan(db: Session):
    return db.query(models.ThanhToan).all()

def search_thanh_toan(db: Session, keyword: str):
    return db.query(models.ThanhToan).filter(
        models.ThanhToan.MaBenhNhan.ilike(f"%{keyword}%")
    ).all()

def create_thanh_toan(db: Session, data: schemas.ThanhToanCreate):
    obj = models.ThanhToan(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_thanh_toan(db: Session, ma_hoa_don: str, data: schemas.ThanhToanUpdate):
    obj = db.query(models.ThanhToan).get(ma_hoa_don)
    if obj:
        for key, value in data.dict().items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
    return obj

def delete_thanh_toan(db: Session, ma_hoa_don: str):
    obj = db.query(models.ThanhToan).get(ma_hoa_don)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
