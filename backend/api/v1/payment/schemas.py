from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ThanhToanBase(BaseModel):
    MaBenhNhan: str
    MaKetQua: Optional[str] = None
    LoaiHoaDon: str
    SoTien: float
    SoTienDaTra: Optional[float] = None
    SoTienConNo: Optional[float] = None
    ThoiGianThanhToan: datetime
    HinhThucThanhToan: str
    MaNhanVien: Optional[str] = None
    TrangThai: str

class ThanhToanCreate(ThanhToanBase):
    MaHoaDon: str

class ThanhToanUpdate(ThanhToanBase):
    pass

class ThanhToanOut(ThanhToanBase):
    MaHoaDon: str

    class Config:
        from_attributes = True