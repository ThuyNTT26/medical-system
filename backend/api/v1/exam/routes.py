# backend/api/v1/exam/routes.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PhieuKham(BaseModel):
    patient_id: int
    symptom: str
    diagnosis: str

@router.post("/phieu")
def create_phieu_kham(data: PhieuKham):
    # Thực tế chỗ này sẽ gọi DB insert
    return {
        "message": "Tạo phiếu khám thành công!",
        "data": data
    }
