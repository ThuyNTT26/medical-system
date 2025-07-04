from sqlalchemy import Column, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from backend.core.database import Base
from backend.api.v1.Ketquakham.models import KetQuaKham
from backend.api.v1.donthuoc.models import DonThuoc
from backend.api.v1.appointment.models import LichHenKham

from sqlalchemy.orm import Session
from fastapi import HTTPException


class BenhNhan(Base):
    __tablename__ = "benhnhan"

    MaBenhNhan = Column(String(10), primary_key=True, index=True)
    hoTen = Column(String, nullable=False)
    ngaySinh = Column(Date)
    gioiTinh = Column(String)
    soDienThoai = Column(String)
    email = Column(String)
    diaChi = Column(String)
    cccd = Column(String)
    tienSuBenhLy = Column(String)
    ket_qua_kham = relationship(
        "KetQuaKham", back_populates="benh_nhan", cascade="all, delete-orphan"
    )
    lich_hen = relationship("LichHenKham", back_populates="benh_nhan")


def get_hoso_chi_tiet(db: Session, ma_benh_nhan: str):
    bn = db.query(BenhNhan).filter(BenhNhan.MaBenhNhan == ma_benh_nhan).first()
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")

    lich_su = db.query(LichHenKham).filter(LichHenKham.MaBenhNhan == ma_benh_nhan).all()
    ket_qua = db.query(KetQuaKham).filter(KetQuaKham.MaBenhNhan == ma_benh_nhan).all()
    don_thuoc = db.query(DonThuoc).filter(DonThuoc.MaBenhNhan == ma_benh_nhan).all()

    return {
        "benh_nhan": bn,
        "lich_su": lich_su,
        "ket_qua": ket_qua,
        "don_thuoc": don_thuoc,
    }


class BacSi(Base):
    __tablename__ = "bacsi"

    MaBacSi = Column(String(10), primary_key=True, index=True)
    hoTen = Column(String)
    chuyenKhoa = Column(String)
    soDienThoai = Column(String)
    email = Column(String)


class LichLamViec(Base):
    __tablename__ = "lichlamviec"

    MaLich = Column(String(10), primary_key=True, index=True)
    MaBacSi = Column(String(10), ForeignKey("bacsi.MaBacSi"))
    Ngay = Column(Date)
    GioBatDau = Column(Time)
    GioKetThuc = Column(Time)
