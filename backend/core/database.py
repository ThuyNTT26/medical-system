from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://NGUYEN_THUY\\SQLEXPRESS01:<password>@<server>/<database>?driver=ODBC+Driver+17+for+SQL+Server"
)


# Nếu dùng SQLite, cần thêm connect_args này
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Tạo SessionLocal để dùng cho Dependency Injection FastAPI
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class để các model kế thừa
Base = declarative_base()

# 👉 Hàm Dependency để lấy session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
