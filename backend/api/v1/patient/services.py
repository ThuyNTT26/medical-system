from sqlalchemy.orm import Session
from . import models, schemas
from backend.api.v1.patient.models import BenhNhan
from backend.api.v1.exam.models import LichHen, KetQua, DonThuoc


def get_all(db: Session):
    return db.query(models.BenhNhan).all()

def get_by_id(db: Session, id: int):
    return db.query(models.BenhNhan).filter(models.BenhNhan.id == id).first()

def create(db: Session, data: schemas.BenhNhanCreate):
    bn = models.BenhNhan(**data.dict())
    db.add(bn)
    db.commit()
    db.refresh(bn)
    return bn

def update(db: Session, id: int, data: schemas.BenhNhanUpdate):
    bn = db.query(models.BenhNhan).filter(models.BenhNhan.id == id).first()
    if not bn:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(bn, key, value)
    db.commit()
    db.refresh(bn)
    return bn

def delete(db: Session, id: int):
    bn = db.query(models.BenhNhan).filter(models.BenhNhan.id == id).first()
    if bn:
        db.delete(bn)
        db.commit()
    return bn

def get_hoso_chi_tiet(db: Session, id: int):
    bn = db.query(BenhNhan).filter(BenhNhan.id == id).first()
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")

    lich_su = db.query(LichHen).filter(LichHen.benh_nhan_id == id).all()
    ket_qua = db.query(KetQua).filter(KetQua.benh_nhan_id == id).all()
    don_thuoc = db.query(DonThuoc).filter(DonThuoc.benh_nhan_id == id).all()

    return {
        "benh_nhan": bn,
        "lich_su_kham": lich_su,
        "ket_qua_dieu_tri": ket_qua,
        "don_thuoc": don_thuoc,
    }

