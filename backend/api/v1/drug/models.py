from sqlalchemy import Column, String, Integer, Float, Date, Text
from backend.core.database import Base

class Thuoc(Base):
    __tablename__ = "Thuoc"

    MaThuoc = Column(String(10), primary_key=True, index=True)
    TenThuoc = Column(String(100), nullable=False)
    DonViTinh = Column(String(20))
    HamLuong = Column(String(50))
    CongDung = Column(Text)
    SoLuongTon = Column(Integer)
    GiaBan = Column(Float)
    NgayHetHan = Column(Date, nullable=True)
