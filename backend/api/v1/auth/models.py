from sqlalchemy import Column, String, Integer
from backend.core.database import Base

class TaiKhoan(Base):
    __tablename__ = "taikhoan"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(100))
