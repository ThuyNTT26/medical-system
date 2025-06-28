from pydantic import BaseModel
from typing import Optional
from datetime import date

class ThuocBase(BaseModel):
    TenThuoc: str
    DonViTinh: str
    HamLuong: str
    CongDung: Optional[str] = None
    SoLuongTon: int
    GiaBan: float
    NgayHetHan: Optional[date] = None

class ThuocCreate(ThuocBase):
    MaThuoc: str

class ThuocUpdate(ThuocBase):
    pass

class ThuocResponse(ThuocCreate):
    class Config:
        from_attributes = True