from sqlalchemy.orm import Session
from .models import ChiTietDonThuoc
from . import schemas

def get_all(db: Session):
    return db.query(ChiTietDonThuoc).all()

def create(db: Session, data: schemas.ChiTietDonThuocCreate):
    ct = ChiTietDonThuoc(**data.dict())
    db.add(ct)
    db.commit()
    db.refresh(ct)
    return ct

def update(db: Session, ma_don: str, ma_thuoc: str, data: schemas.ChiTietDonThuocUpdate):
    ct = db.query(ChiTietDonThuoc).filter_by(MaDonThuoc=ma_don, MaThuoc=ma_thuoc).first()
    if not ct:
        return None
    ct.SoLuong = data.SoLuong
    ct.LieuDung = data.LieuDung
    db.commit()
    db.refresh(ct)
    return ct

def delete(db: Session, ma_don: str, ma_thuoc: str):
    ct = db.query(ChiTietDonThuoc).filter_by(MaDonThuoc=ma_don, MaThuoc=ma_thuoc).first()
    if not ct:
        return False
    db.delete(ct)
    db.commit()
    return True
