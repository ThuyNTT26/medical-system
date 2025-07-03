from sqlalchemy.orm import Session
from backend.api.v1.auth.models import TaiKhoan
from backend.core.security import verify_password, hash_password, create_access_token

def authenticate_user(db: Session, tenDangNhap: str, matKhau: str):
    user = db.query(TaiKhoan).filter(TaiKhoan.tenDangNhap == tenDangNhap).first()
    if user and verify_password(matKhau, user.matKhau):
        return user
    return None

def register_user(db: Session, tenDangNhap: str, matKhau: str, vaiTro: str = "user"):
    user = db.query(TaiKhoan).filter(TaiKhoan.tenDangNhap == tenDangNhap).first()
    if user:
        return None
    new_user = TaiKhoan(
        tenDangNhap=tenDangNhap,
        matKhau=hash_password(matKhau),
        vaiTro=vaiTro
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
