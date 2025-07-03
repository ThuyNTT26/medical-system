# backend/api/v1/appointment/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class LichHenBase(BaseModel):
    MaBenhNhan: Optional[str]
    MaBacSi: Optional[str]
    MaLich: Optional[str]
    NgayHen: Optional[date]
    GioHen: Optional[time]
    TrangThai: Optional[str] = "Chờ khám"
    LyDo: Optional[str]

class LichHenCreate(LichHenBase):
    pass

class LichHenUpdate(BaseModel):
    MaBenhNhan: Optional[str]
    MaBacSi: Optional[str]
    MaLich: Optional[str]
    NgayHen: Optional[date]
    GioHen: Optional[time]
    TrangThai: Optional[str]
    LyDo: Optional[str]

class LichHenOut(LichHenBase):
    MaLichHen: str

    class Config:
        orm_mode = True
