# backend/api/v1/appointment/models.py
from sqlalchemy import Column, String, Date, Time, Text, ForeignKey
from backend.core.database import Base
from sqlalchemy.orm import relationship

class LichHenKham(Base):
    __tablename__ = "lichhenkham"

    MaLichHen = Column(String(10), primary_key=True)
    MaBenhNhan = Column(String(10), ForeignKey("benhnhan.MaBenhNhan"))
    MaBacSi = Column(String(10), ForeignKey("bacsi.MaBacSi"))
    MaLich = Column(String(10))
    NgayHen = Column(Date)
    GioHen = Column(Time)
    TrangThai = Column(String(50), default="Chờ khám")
    LyDo = Column(Text)
    benh_nhan = relationship("BenhNhan", back_populates="lich_hen")