from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.api.v1.patient import schemas, services
from backend.core.security import get_current_user  # Bảo vệ API

router = APIRouter(
    prefix="/api/v1/patient",
    tags=["patient"]
)

@router.post("/", response_model=schemas.BenhNhanOut)
def create_patient(benhnhan: schemas.BenhNhanCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return services.create_benhnhan(db, benhnhan)

@router.get("/", response_model=list[schemas.BenhNhanOut])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return services.get_benhnhan(db, skip, limit)

@router.post("/appointment", response_model=schemas.LichHenOut)
def create_appointment(lichhen: schemas.LichHenCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return services.create_lichhen(db, lichhen)

@router.get("/appointment", response_model=list[schemas.LichHenOut])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return services.get_lichhen(db, skip, limit)
