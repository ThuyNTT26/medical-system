from sqlalchemy import Column, String, Date, Text, ForeignKey
from backend.core.database import Base

class PhieuKhamBenh(Base):
    __tablename__ = "PhieuKhamBenh"

    MaPhieuKham = Column(String(50), primary_key=True)
    MaBenhNhan = Column(String(50), ForeignKey("BenhNhan.MaBenhNhan", ondelete="SET NULL"), nullable=True)
    MaBacSi = Column(String(50), ForeignKey("BacSi.MaBacSi"))
    NgayKham = Column(Date)
    TrieuChung = Column(Text)
    ChuanDoan = Column(Text)
    HuongDieuTri = Column(Text)
    MaLichHen = Column(String(50), ForeignKey("LichHenKham.MaLichHen"))
