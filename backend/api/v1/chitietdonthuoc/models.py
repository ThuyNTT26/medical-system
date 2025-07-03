from sqlalchemy import Column, String, Integer, ForeignKey
from backend.core.database import Base

class ChiTietDonThuoc(Base):
    __tablename__ = "ChiTietDonThuoc"

    MaDonThuoc = Column(String(50), ForeignKey("DonThuoc.MaDonThuoc"), primary_key=True)
    MaThuoc = Column(String(50), ForeignKey("Thuoc.MaThuoc"), primary_key=True)
    SoLuong = Column(Integer)
    LieuDung = Column(String(255))
