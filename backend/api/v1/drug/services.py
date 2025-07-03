from sqlalchemy.orm import Session
from . import models, schemas

def get_all_thuoc(db: Session):
    return db.query(models.Thuoc).all()

def search_thuoc(db: Session, keyword: str):
    return db.query(models.Thuoc).filter(models.Thuoc.TenThuoc.ilike(f"%{keyword}%")).all()

def create_thuoc(db: Session, thuoc: schemas.ThuocCreate):
    db_thuoc = models.Thuoc(**thuoc.dict())
    db.add(db_thuoc)
    db.commit()
    db.refresh(db_thuoc)
    return db_thuoc

def update_thuoc(db: Session, ma_thuoc: str, data: schemas.ThuocUpdate):
    db_thuoc = db.query(models.Thuoc).get(ma_thuoc)
    if db_thuoc:
        for key, value in data.dict().items():
            setattr(db_thuoc, key, value)
        db.commit()
        db.refresh(db_thuoc)
    return db_thuoc

def delete_thuoc(db: Session, ma_thuoc: str):
    db_thuoc = db.query(models.Thuoc).get(ma_thuoc)
    if db_thuoc:
        db.delete(db_thuoc)
        db.commit()
    return db_thuoc
