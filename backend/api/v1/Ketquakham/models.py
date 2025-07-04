from sqlalchemy import Column, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.core.database import Base

class KetQuaKham(Base):
    __tablename__ = "KetQuaKham"

    MaKetQua = Column(String(50), primary_key=True)
    MaPhieuKham = Column(String(50), ForeignKey("PhieuKhamBenh.MaPhieuKham"), unique=True)
    LoaiXetNghiem = Column(String(50))
    KetQuaXetNghiem = Column(Text)
    NgayThucHien = Column(Date)

    MaBenhNhan = Column(String(10), ForeignKey("benhnhan.MaBenhNhan"))
    benh_nhan = relationship("BenhNhan", back_populates="ket_qua_kham")