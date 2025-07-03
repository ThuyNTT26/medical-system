from sqlalchemy.orm import Session
from .models import KetQuaKham
from . import schemas

def get_all(db: Session):
    return db.query(KetQuaKham).all()

def create(db: Session, data: schemas.KetQuaKhamCreate):
    kq = KetQuaKham(**data.dict())
    db.add(kq)
    db.commit()
    db.refresh(kq)
    return kq

def update(db: Session, ma_kq: str, data: schemas.KetQuaKhamUpdate):
    kq = db.query(KetQuaKham).filter(KetQuaKham.MaKetQua == ma_kq).first()
    if not kq:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(kq, key, value)
    db.commit()
    db.refresh(kq)
    return kq

def delete(db: Session, ma_kq: str):
    kq = db.query(KetQuaKham).filter(KetQuaKham.MaKetQua == ma_kq).first()
    if not kq:
        return False
    db.delete(kq)
    db.commit()
    return True
