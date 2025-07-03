from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 👉 Kết nối CSDL MySQL 
DATABASE_URL = "mysql+pymysql://root:trang091106@localhost/phongkhamtunhan"

# 👉 Tạo engine kết nối CSDL
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # kiểm tra kết nối còn sống trước khi dùng
    echo=False           # bật True nếu bạn muốn xem log các câu SQL
)

# 👉 SessionLocal là phiên làm việc với DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 👉 Base dùng để kế thừa trong các model (các bảng)
Base = declarative_base()

# 👉 Dependency cho FastAPI (sử dụng trong các route)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
