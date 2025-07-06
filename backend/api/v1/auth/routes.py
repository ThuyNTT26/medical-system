from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.core import security
from backend.api.v1.auth import schemas, services

from backend.core.security import get_current_user
from backend.api.v1.auth.models import TaiKhoan


router = APIRouter(tags=["auth"])


@router.get("/me")
def get_me(current_user: TaiKhoan = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "tenDangNhap": current_user.tenDangNhap,
        "vaiTro": current_user.vaiTro,
    }


@router.post("/login", response_model=schemas.TokenResponse)
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = services.authenticate_user(db, data.tenDangNhap, data.matKhau)
    print("🔐 Tìm thấy user:", user)
    if not user:
        raise HTTPException(status_code=401, detail="Sai tài khoản hoặc mật khẩu")
    token = security.create_access_token({"sub": user.tenDangNhap})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register")
def register(data: schemas.RegisterRequest, db: Session = Depends(get_db)):
    user = services.register_user(db, data.tenDangNhap, data.matKhau, data.vaiTro)
    if not user:
        raise HTTPException(status_code=400, detail="Tài khoản đã tồn tại")
    return {"message": "Đăng ký thành công"}
