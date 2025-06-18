from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from backend.core.database import Base
from backend.api.v1.exam.models import LichHen, KetQua, DonThuoc

from sqlalchemy.orm import Session


class BenhNhan(Base):
    __tablename__ = "benhnhan"

    id = Column(Integer, primary_key=True, index=True)
    hoTen = Column(String, nullable=False)
    ngaySinh = Column(Date)
    gioiTinh = Column(String)
    soDienThoai = Column(String)
    email = Column(String)
    diaChi = Column(String)
    cccd = Column(String)
    tienSuBenhLy = Column(String)
    lichhen = relationship("LichHen", back_populates="benh_nhan", cascade="all, delete-orphan")

def get_hoso_chi_tiet(db: Session, id: int):
    bn = db.query(BenhNhan).filter(BenhNhan.id == id).first()
    if not bn:
        raise HTTPException(status_code=404, detail="Không tìm thấy bệnh nhân")

    lich_su = db.query(LichHen).filter(LichHen.benh_nhan_id == id).all()
    ket_qua = db.query(KetQua).filter(KetQua.benh_nhan_id == id).all()
    don_thuoc = db.query(DonThuoc).filter(DonThuoc.benh_nhan_id == id).all()

    return {
        "benh_nhan": bn,
        "lich_su": lich_su,
        "ket_qua": ket_qua,
        "don_thuoc": don_thuoc
    }
