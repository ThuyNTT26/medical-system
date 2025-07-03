from pydantic import BaseModel
from datetime import date
from typing import Optional

class DonThuocBase(BaseModel):
    MaKetQua: str
    NgayKeDon: Optional[date]
    GhiChu: Optional[str]

class DonThuocCreate(DonThuocBase):
    MaDonThuoc: str

class DonThuocUpdate(BaseModel):
    NgayKeDon: Optional[date]
    GhiChu: Optional[str]

class DonThuocResponse(DonThuocCreate):
    model_config = {
    "from_attributes": True
    }
