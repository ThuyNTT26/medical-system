'''from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan
from . import services, schemas

router = APIRouter(prefix="/ketquakham", tags=["KetQuaKham"])

@router.get("/", response_model=list[schemas.KetQuaKhamResponse])
def get_all(db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.get_all(db)

@router.post("/", response_model=schemas.KetQuaKhamResponse)
def create_ketqua(data: schemas.KetQuaKhamCreate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    return services.create(db, data)

@router.put("/{ma_ketqua}", response_model=schemas.KetQuaKhamResponse)
def update_ketqua(ma_ketqua: str, data: schemas.KetQuaKhamUpdate, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    kq = services.update(db, ma_ketqua, data)
    if not kq:
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả khám")
    return kq

@router.delete("/{ma_ketqua}")
def delete_ketqua(ma_ketqua: str, db: Session = Depends(get_db), user: TaiKhoan = Depends(get_current_user)):
    if not services.delete(db, ma_ketqua):
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả khám")
    return {"message": "Đã xoá kết quả khám"}'''


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan

from . import services, schemas

router = APIRouter(prefix="/ketquakham", tags=["KetQuaKham"])

# Lấy tất cả kết quả khám
@router.get("/", response_model=list[schemas.KetQuaKhamResponse])
def get_all_ketquakham(
    db: Session = Depends(get_db),
    
):
    return services.get_all(db)

# Tạo mới kết quả khám
@router.post("/", response_model=schemas.KetQuaKhamResponse)
def create_ketquakham(
    data: schemas.KetQuaKhamCreate,
    db: Session = Depends(get_db),
    
):
    return services.create(db, data)

# Cập nhật kết quả khám
@router.put("/{ma_ketqua}", response_model=schemas.KetQuaKhamResponse)
def update_ketquakham(
    ma_ketqua: str,
    data: schemas.KetQuaKhamUpdate,
    db: Session = Depends(get_db),
    
):
    ketqua = services.update(db, ma_ketqua, data)
    if not ketqua:
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả khám")
    return ketqua

# Xoá kết quả khám
@router.delete("/{ma_ketqua}")
def delete_ketquakham(
    ma_ketqua: str,
    db: Session = Depends(get_db),
  
):
    if not services.delete(db, ma_ketqua):
        raise HTTPException(status_code=404, detail="Không tìm thấy kết quả khám")
    return {"message": "Đã xoá kết quả khám"}
