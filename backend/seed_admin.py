from backend.core.database import SessionLocal
from backend.core.security import get_password_hash
from backend.api.v1.auth.models import TaiKhoan

def create_admin():
    db = SessionLocal()
    try:
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
        db.refresh(admin)  # 👉 nên có
        print("✅ Đã tạo tài khoản admin: admin / 123456")
    except Exception as e:
        db.rollback()
        print("❌ Lỗi tạo tài khoản admin:", e)
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()
