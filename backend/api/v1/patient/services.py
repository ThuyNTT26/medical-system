from sqlalchemy.orm import Session
from . import models, schemas
from backend.api.v1.patient.models import BenhNhan
from backend.api.v1.appointment.models import LichHenKham
from backend.api.v1.Ketquakham.models import KetQuaKham
from backend.api.v1.donthuoc.models import DonThuoc
from backend.api.v1.appointment.schemas import LichHenCreate

from fastapi import HTTPException

def get_all(db: Session):
    return db.query(BenhNhan).all()

def get_by_id(db: Session, ma_benh_nhan: str):
    return db.query(BenhNhan).filter(BenhNhan.MaBenhNhan == ma_benh_nhan).first()

def create(db: Session, data: schemas.BenhNhanCreate):
    max_code = db.query(BenhNhan.MaBenhNhan).order_by(BenhNhan.MaBenhNhan.desc()).first()
    if max_code and max_code[0]:
        max_number = int(max_code[0][2:])
    else:
        max_number = 0

    new_code = f"BN{max_number + 1:03d}"

    bn = BenhNhan(
        MaBenhNhan=new_code,
        hoTen=data.hoTen,
        ngaySinh=data.ngaySinh,
        gioiTinh=data.gioiTinh,
        soDienThoai=data.soDienThoai,
        email=data.email,
        diaChi=data.diaChi,
        cccd=data.cccd,
        tienSuBenhLy=data.tienSuBenhLy
    )

    db.add(bn)
    db.commit()
    db.refresh(bn)
    return bn


def update(db: Session, ma_benh_nhan: str, data: schemas.BenhNhanUpdate):
    bn = db.query(BenhNhan).filter(BenhNhan.MaBenhNhan == ma_benh_nhan).first()
    if not bn:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(bn, key, value)
    db.commit()
    db.refresh(bn)
    return bn

def delete(db: Session, ma_benh_nhan: str):
    bn = db.query(BenhNhan).filter(BenhNhan.MaBenhNhan == ma_benh_nhan).first()
    if bn:
        db.delete(bn)
        db.commit()
    return bn

def get_hoso_chi_tiet(db: Session, ma_benh_nhan: str):
    bn = db.query(BenhNhan).filter(BenhNhan.MaBenhNhan == ma_benh_nhan).first()
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")

    lich_su = db.query(LichHenKham).filter(LichHenKham.MaBenhNhan == ma_benh_nhan).all()
    ket_qua = db.query(KetQuaKham).filter(KetQuaKham.MaPhieuKham.in_(
        db.query(KetQuaKham.MaPhieuKham).join(LichHenKham, KetQuaKham.MaPhieuKham == LichHenKham.MaLichHen)
        .filter(LichHenKham.MaBenhNhan == ma_benh_nhan)
    )).all()
    don_thuoc = db.query(DonThuoc).filter(DonThuoc.MaKetQua.in_(
        [k.MaKetQua for k in ket_qua]
    )).all()

    return {
        "benh_nhan": bn,
        "lich_su": lich_su,
        "ket_qua": ket_qua,
        "don_thuoc": don_thuoc,
    }

def get_lichhen(db: Session):
    return db.query(LichHenKham).all()

def create_lichhen(db: Session, lichhen: LichHenCreate):
    db_lh = LichHen(**lichhen.dict())
    db.add(db_lh)
    db.commit()
    db.refresh(db_lh)
    return db_lh
