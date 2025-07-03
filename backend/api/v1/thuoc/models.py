from sqlalchemy import Column, String, Integer, DECIMAL, Date, Text
from backend.core.database import Base

class Thuoc(Base):
    __tablename__ = "Thuoc"

    MaThuoc = Column(String(50), primary_key=True)
    TenThuoc = Column(String(100))
    DonViTinh = Column(String(20))
    HamLuong = Column(String(50))
    CongDung = Column(Text)
    SoLuongTon = Column(Integer)
    GiaBan = Column(DECIMAL(10, 2))
    NgayHetHan = Column(Date)
