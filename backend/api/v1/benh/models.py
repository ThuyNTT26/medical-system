from sqlalchemy import Column, String, Text, ForeignKey
from backend.core.database import Base

class Benh(Base):
    __tablename__ = "Benh"

    MaBenh = Column(String(50), primary_key=True)
    TenBenh = Column(String(100))
    MoTa = Column(Text)
    MaICD = Column(String(50))
    MaKetQua = Column(String(50), ForeignKey("KetQuaKham.MaKetQua"))
