from sqlalchemy import Column, Integer, String
from backend.core.database import Base

class TaiKhoan(Base):
    __tablename__ = "taikhoan"

    id = Column(Integer, primary_key=True, index=True)
    tenDangNhap = Column(String, unique=True, nullable=False)
    matKhau = Column(String, nullable=False)
    vaiTro = Column(String, default="user")

