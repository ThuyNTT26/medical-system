from sqlalchemy.orm import Session
from .models import PhieuKhamBenh
from . import schemas

def get_all(db: Session):
    return db.query(PhieuKhamBenh).all()

def create(db: Session, data: schemas.PhieuKhamBenhCreate):
    phieu = PhieuKhamBenh(**data.dict())
    db.add(phieu)
    db.commit()
    db.refresh(phieu)
    return phieu

def update(db: Session, ma_phieu: str, data: schemas.PhieuKhamBenhUpdate):
    phieu = db.query(PhieuKhamBenh).filter(PhieuKhamBenh.MaPhieuKham == ma_phieu).first()
    if not phieu:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(phieu, key, value)
    db.commit()
    db.refresh(phieu)
    return phieu

def delete(db: Session, ma_phieu: str):
    phieu = db.query(PhieuKhamBenh).filter(PhieuKhamBenh.MaPhieuKham == ma_phieu).first()
    if not phieu:
        return False
    db.delete(phieu)
    db.commit()
    return True
