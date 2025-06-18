from pydantic import BaseModel
from datetime import datetime

class LichHenOut(BaseModel):
    thoi_gian: datetime
    noi_dung: str
    ket_qua: str

    class Config:
        orm_mode = True
