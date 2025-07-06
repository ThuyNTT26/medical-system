from sqlalchemy import Column, String, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import relationship
from backend.core.database import Base


class BenhNhan(Base):
    __tablename__ = "benhnhan"

    MaBenhNhan = Column(String(10), primary_key=True, index=True)
    hoTen = Column(String, nullable=False)
    ngaySinh = Column(Date)
    gioiTinh = Column(String)
    soDienThoai = Column(String)
    email = Column(String)
    diaChi = Column(String)
    cccd = Column(String)
    tienSuBenhLy = Column(String)
    ket_qua_kham = relationship(
        "backend.api.v1.Ketquakham.models.KetQuaKham",
        back_populates="benh_nhan",
        cascade="all, delete-orphan",
    )
    lich_hen = relationship("LichHenKham", back_populates="benh_nhan")


class BacSi(Base):
    __tablename__ = "bacsi"

    MaBacSi = Column(String(10), primary_key=True, index=True)
    hoTen = Column(String)
    chuyenKhoa = Column(String)
    soDienThoai = Column(String)
    email = Column(String)


class LichLamViec(Base):
    __tablename__ = "lichlamviec"

    MaLich = Column(String(10), primary_key=True, index=True)
    MaBacSi = Column(String(10), ForeignKey("bacsi.MaBacSi"))
    Ngay = Column(Date)
    GioBatDau = Column(Time)
    GioKetThuc = Column(Time)
