from pydantic import BaseModel
from datetime import date
from typing import Optional

class PhieuKhamBenhBase(BaseModel):
    MaBenhNhan: str
    MaBacSi: str
    NgayKham: date
    TrieuChung: Optional[str]
    ChuanDoan: Optional[str]
    HuongDieuTri: Optional[str]
    MaLichHen: Optional[str]

class PhieuKhamBenhCreate(PhieuKhamBenhBase):
    MaPhieuKham: str

class PhieuKhamBenhUpdate(BaseModel):
    TrieuChung: Optional[str]
    ChuanDoan: Optional[str]
    HuongDieuTri: Optional[str]

class PhieuKhamBenhResponse(PhieuKhamBenhCreate):
    model_config = {
    "from_attributes": True
    }
