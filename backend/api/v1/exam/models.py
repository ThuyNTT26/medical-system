# backend/api/v1/exam/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from backend.core.database import Base

class KetQuaKham(Base):
    __tablename__ = "ketquakham"

    MaKetQua = Column(String(10), primary_key=True, index=True)
    MaPhieuKham = Column(String(10), ForeignKey("phieukhambenh.MaPhieuKham"), unique=True)
    LoaiXetNghiem = Column(String(100))
    KetQuaXetNghiem = Column(Text)
    NgayThucHien = Column(Date)
    MaBenhNhan = Column(String(10), ForeignKey("benhnhan.MaBenhNhan"))
    benh_nhan = relationship("BenhNhan", back_populates="ket_qua_kham")
    don_thuoc = relationship("DonThuoc", back_populates="ket_qua")


class DonThuoc(Base):
    __tablename__ = "donthuoc"

    MaDonThuoc = Column(String(10), primary_key=True, index=True)
    MaKetQua = Column(String(10), ForeignKey("ketquakham.MaKetQua"))
    NgayKeDon = Column(Date)
    GhiChu = Column(Text)

    ket_qua = relationship("KetQuaKham", back_populates="don_thuoc")

