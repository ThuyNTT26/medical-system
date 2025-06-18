from sqlalchemy.orm import Session
from . import models, schemas

def create_benhnhan(db: Session, benhnhan: schemas.BenhNhanCreate):
    db_obj = models.BenhNhan(**benhnhan.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_benhnhan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BenhNhan).offset(skip).limit(limit).all()

def create_lichhen(db: Session, lichhen: schemas.LichHenCreate):
    db_obj = models.LichHen(**lichhen.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_lichhen(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LichHen).offset(skip).limit(limit).all()
