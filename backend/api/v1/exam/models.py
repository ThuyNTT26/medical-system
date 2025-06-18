# backend/api/v1/exam/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.core.database import Base

class LichHen(Base):
    __tablename__ = "lichhen"
    id = Column(Integer, primary_key=True, index=True)
    benh_nhan_id = Column(Integer, ForeignKey("benhnhan.id"))
    ngay_kham = Column(Date)
    ly_do = Column(String(255))

    benh_nhan = relationship("BenhNhan", back_populates="lichhen")

class KetQua(Base):
    __tablename__ = "ketqua"
    id = Column(Integer, primary_key=True, index=True)
    benh_nhan_id = Column(Integer, ForeignKey("benhnhan.id"))
    chan_doan = Column(String(255))
    ghi_chu = Column(Text)

class DonThuoc(Base):
    __tablename__ = "donthuoc"
    id = Column(Integer, primary_key=True, index=True)
    benh_nhan_id = Column(Integer, ForeignKey("benhnhan.id"))
    thuoc = Column(String(255))
    lieu_luong = Column(String(255))
    huong_dan = Column(Text)
