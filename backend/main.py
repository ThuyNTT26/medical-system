from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import router từng phần
from backend.api.v1.exam import routes as exam_routes
from backend.api.v1.patient import routes as patient_routes
from backend.api.v1.auth import routes as auth_routes
from backend.api.v1.appointment import routes as appointment_routes

from backend.core.database import engine
from backend.api.v1.auth.models import TaiKhoan

from backend.seed_admin import create_admin

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Medical Management System")

@app.on_event("startup")
def startup_event():
    create_admin()

# CORS cho phép gọi API từ frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (css, js, images)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Kết nối thư mục chứa các HTML template
templates = Jinja2Templates(directory="frontend")


# Route trả về trang login
@app.get("/auth/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

# dashboard
@app.get("/index", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Gắn các route backend vào API chính
app.include_router(exam_routes.router, prefix="/api/v1/exam")
app.include_router(patient_routes.router, prefix="/api/v1/patient")
app.include_router(auth_routes.router, prefix="/api/v1/auth")
app.include_router(appointment_routes.router, prefix="/api/v1/appointments")

for route in app.router.routes:
    print(route.path)