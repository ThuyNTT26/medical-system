from pydantic import BaseModel

class ChiTietDonThuocBase(BaseModel):
    MaDonThuoc: str
    MaThuoc: str
    SoLuong: int
    LieuDung: str

class ChiTietDonThuocCreate(ChiTietDonThuocBase):
    pass

class ChiTietDonThuocUpdate(BaseModel):
    SoLuong: int
    LieuDung: str

class ChiTietDonThuocResponse(ChiTietDonThuocBase):
    model_config = {
    "from_attributes": True
    }

