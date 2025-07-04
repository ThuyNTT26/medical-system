from sqlalchemy import Column, String, DECIMAL, DateTime
from backend.core.database import Base

class ThanhToan(Base):
    __tablename__ = "ThanhToan"

    MaHoaDon = Column(String(50), primary_key=True)
    MaBenhNhan = Column(String(50))
    MaKetQua = Column(String(50), nullable=True)
    LoaiHoaDon = Column(String(50))
    SoTien = Column(DECIMAL(10,2))
    SoTienDaTra = Column(DECIMAL(10,2), nullable=True)
    SoTienConNo = Column(DECIMAL(10,2), nullable=True)
    ThoiGianThanhToan = Column(DateTime)
    HinhThucThanhToan = Column(String(50))
    MaNhanVien = Column(String(50), nullable=True)
    TrangThai = Column(String(50))