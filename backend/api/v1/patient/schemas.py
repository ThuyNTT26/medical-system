from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BenhNhanBase(BaseModel):
    name: str
    phone: str
    address: Optional[str] = None

class BenhNhanCreate(BenhNhanBase):
    pass

class BenhNhanOut(BenhNhanBase):
    id: int
    class Config:
        orm_mode = True

class LichHenBase(BaseModel):
    patient_id: int
    date: datetime
    reason: Optional[str] = None

class LichHenCreate(LichHenBase):
    pass

class LichHenOut(LichHenBase):
    id: int
    patient: BenhNhanOut
    class Config:
        orm_mode = True
