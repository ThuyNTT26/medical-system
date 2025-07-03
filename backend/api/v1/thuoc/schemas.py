from pydantic import BaseModel
from datetime import date
from typing import Optional

class ThuocBase(BaseModel):
    TenThuoc: str
    DonViTinh: Optional[str]
    HamLuong: Optional[str]
    CongDung: Optional[str]
    SoLuongTon: Optional[int]
    GiaBan: Optional[float]
    NgayHetHan: Optional[date]

class ThuocCreate(ThuocBase):
    MaThuoc: str

class ThuocUpdate(BaseModel):
    TenThuoc: Optional[str]
    DonViTinh: Optional[str]
    HamLuong: Optional[str]
    CongDung: Optional[str]
    SoLuongTon: Optional[int]
    GiaBan: Optional[float]
    NgayHetHan: Optional[date]

class ThuocResponse(ThuocCreate):
    model_config = {
    "from_attributes": True
    }
