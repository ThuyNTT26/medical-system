from sqlalchemy.orm import Session
from .models import Benh
from backend.api.v1.benh import schemas

def get_all(db: Session):
    return db.query(Benh).all()

def create(db: Session, data: schemas.BenhCreate):
    benh = Benh(**data.dict())
    db.add(benh)
    db.commit()
    db.refresh(benh)
    return benh

def update(db: Session, ma_benh: str, data: schemas.BenhUpdate):
    benh = db.query(Benh).filter(Benh.MaBenh == ma_benh).first()
    if not benh:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(benh, key, value)
    db.commit()
    db.refresh(benh)
    return benh

def delete(db: Session, ma_benh: str):
    benh = db.query(Benh).filter(Benh.MaBenh == ma_benh).first()
    if not benh:
        return False
    db.delete(benh)
    db.commit()
    return True
