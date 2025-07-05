# === backend/api/v1/patient/schemas.py ===
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, time

# === Base schema ===
class BenhNhanBase(BaseModel):
    hoTen: str
    ngaySinh: Optional[date]
    gioiTinh: Optional[str]
    soDienThoai: Optional[str]
    email: Optional[str]
    diaChi: Optional[str]
    cccd: Optional[str]
    tienSuBenhLy: Optional[str]

class BenhNhanCreate(BenhNhanBase):
    pass

class BenhNhanUpdate(BenhNhanBase):
    pass

# ✅ Sửa: dùng alias để map MaBenhNhan -> id
class BenhNhanOut(BenhNhanBase):
    MaBenhNhan: str

    class Config:
        from_attributes = True

# --- Schema cho hồ sơ ---
class LichHenOut(BaseModel):
    MaLichHen: str
    ngay_kham: Optional[date]
    ly_do: Optional[str]

    class Config:
        from_attributes = True

class KetQuaOut(BaseModel):
    id: int
    chan_doan: Optional[str]
    ghi_chu: Optional[str]

    class Config:
        from_attributes = True

class DonThuocOut(BaseModel):
    id: int
    thuoc: Optional[str]
    lieu_luong: Optional[str]
    huong_dan: Optional[str]

    class Config:
        from_attributes = True

class HoSoChiTietOut(BaseModel):
    benh_nhan: BenhNhanOut
    lich_su: List[LichHenOut]
    ket_qua: List[KetQuaOut]
    don_thuoc: List[DonThuocOut]
