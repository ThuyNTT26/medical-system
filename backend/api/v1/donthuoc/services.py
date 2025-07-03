from sqlalchemy.orm import Session
from .models import DonThuoc
from . import schemas

def get_all(db: Session):
    return db.query(DonThuoc).all()

def create(db: Session, data: schemas.DonThuocCreate):
    don = DonThuoc(**data.dict())
    db.add(don)
    db.commit()
    db.refresh(don)
    return don

def update(db: Session, ma_don: str, data: schemas.DonThuocUpdate):
    don = db.query(DonThuoc).filter(DonThuoc.MaDonThuoc == ma_don).first()
    if not don:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(don, key, value)
    db.commit()
    db.refresh(don)
    return don

def delete(db: Session, ma_don: str):
    don = db.query(DonThuoc).filter(DonThuoc.MaDonThuoc == ma_don).first()
    if not don:
        return False
    db.delete(don)
    db.commit()
    return True
