# === backend/api/v1/patient/schemas.py ===
from pydantic import BaseModel, Field, validator
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

    @validator("gioiTinh", pre=True)
    def normalize_gender(cls, v):
        if v is None:
            return None
        v = v.strip().lower()
        if v in ["M","m", "nam", "Nam"]:
            return "Nam"
        elif v in ["F","f", "nữ", "nu","Nữ"]:
            return "Nữ"
        else:
            return v

class BenhNhanCreate(BenhNhanBase):
    pass

class BenhNhanUpdate(BenhNhanBase):
    pass

# ✅ Sửa: dùng alias để map MaBenhNhan -> id
class BenhNhanOut(BaseModel):
    maBenhNhan: str = Field(..., alias="MaBenhNhan")
    hoTen: str = Field(..., alias="HoTen")
    ngaySinh: Optional[date] = Field(None, alias="NgaySinh")
    gioiTinh: Optional[str] = Field(None, alias="GioiTinh")
    soDienThoai: Optional[str] = Field(None, alias="SoDienThoai")
    email: Optional[str] = Field(None, alias="Email")
    diaChi: Optional[str] = Field(None, alias="DiaChi")
    cccd: Optional[str] = Field(None, alias="CCCD")
    tienSuBenhLy: Optional[str] = Field(None, alias="TienSuBenhLy")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True

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
