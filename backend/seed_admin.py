# backend/seed_admin.py

from backend.core.database import SessionLocal
from backend.core.security import get_password_hash
from backend.api.v1.auth.models import TaiKhoan

def create_admin():
    db = SessionLocal()
    if db.query(TaiKhoan).filter(TaiKhoan.tenDangNhap == "admin").first():
        print("⚠ Admin đã tồn tại.")
        return

    admin = TaiKhoan(
        tenDangNhap="admin",
        matKhau=get_password_hash("123456"),
        vaiTro="admin"
    )
    db.add(admin)
    db.commit()
    db.close()
    print("✅ Đã tạo tài khoản admin: admin / 123456")

if __name__ == "__main__":
    create_admin()
