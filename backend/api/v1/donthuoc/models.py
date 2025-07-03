from sqlalchemy import Column, String, Date, Text, ForeignKey
from backend.core.database import Base

class DonThuoc(Base):
    __tablename__ = "DonThuoc"

    MaDonThuoc = Column(String(50), primary_key=True)
    MaKetQua = Column(String(50), ForeignKey("KetQuaKham.MaKetQua"))
    NgayKeDon = Column(Date)
    GhiChu = Column(Text)
