# backend/api/v1/appointment/services.py
from . import models, schemas
from sqlalchemy.orm import Session

def get_all(db: Session):
    return db.query(models.LichHenKham).all()

def get_by_id(db: Session, id: str):
    return db.query(models.LichHenKham).filter(models.LichHenKham.MaLichHen == id).first()

def create(db: Session, data: schemas.LichHenCreate):
    # Auto gen mã lịch hẹn LHxxx
    count = db.query(models.LichHenKham).count() + 1
    ma = f"LH{count:03d}"
    lichhen = models.LichHenKham(MaLichHen=ma, **data.dict())
    db.add(lichhen)
    db.commit()
    db.refresh(lichhen)
    return lichhen

def update(db: Session, id: str, data: schemas.LichHenUpdate):
    lh = get_by_id(db, id)
    if not lh:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(lh, key, value)
    db.commit()
    db.refresh(lh)
    return lh

def delete(db: Session, id: str):
    lh = get_by_id(db, id)
    if not lh:
        return False
    db.delete(lh)
    db.commit()
    return True
