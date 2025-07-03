from sqlalchemy.orm import Session
from .models import Thuoc
from . import schemas

def get_all(db: Session):
    return db.query(Thuoc).all()

def create(db: Session, data: schemas.ThuocCreate):
    thuoc = Thuoc(**data.dict())
    db.add(thuoc)
    db.commit()
    db.refresh(thuoc)
    return thuoc

def update(db: Session, ma_thuoc: str, data: schemas.ThuocUpdate):
    thuoc = db.query(Thuoc).filter(Thuoc.MaThuoc == ma_thuoc).first()
    if not thuoc:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(thuoc, key, value)
    db.commit()
    db.refresh(thuoc)
    return thuoc

def delete(db: Session, ma_thuoc: str):
    thuoc = db.query(Thuoc).filter(Thuoc.MaThuoc == ma_thuoc).first()
    if not thuoc:
        return False
    db.delete(thuoc)
    db.commit()
    return True
