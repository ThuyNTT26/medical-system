from pydantic import BaseModel
from typing import Optional

class BenhResponse(BaseModel):
    MaBenh: str
    TenBenh: Optional[str]
    MoTa: Optional[str]
    MaICD: Optional[str]
    MaKetQua: Optional[str]

    model_config = {
    "from_attributes": True
    }

class BenhCreate(BaseModel):
    MaBenh: str
    TenBenh: Optional[str]
    MoTa: Optional[str]
    MaICD: Optional[str]
    MaKetQua: Optional[str]

class BenhUpdate(BaseModel):
    TenBenh: Optional[str]
    MoTa: Optional[str]
    MaICD: Optional[str]
    MaKetQua: Optional[str]
