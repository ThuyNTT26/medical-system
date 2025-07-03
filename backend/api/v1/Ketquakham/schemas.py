from pydantic import BaseModel
from datetime import date
from typing import Optional

class KetQuaKhamBase(BaseModel):
    MaPhieuKham: str
    LoaiXetNghiem: Optional[str]
    KetQuaXetNghiem: Optional[str]
    NgayThucHien: Optional[date]

class KetQuaKhamCreate(KetQuaKhamBase):
    MaKetQua: str

class KetQuaKhamUpdate(BaseModel):
    LoaiXetNghiem: Optional[str]
    KetQuaXetNghiem: Optional[str]
    NgayThucHien: Optional[date]

class KetQuaKhamResponse(KetQuaKhamCreate):
    model_config = {
    "from_attributes": True
    }
