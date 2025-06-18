# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.v1.exam import routes as exam_routes
from backend.api.v1.patient import routes as patient_routes
from backend.api.v1.auth import routes as auth_routes
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI(title="Medical Management System")

# Cho phép gọi từ frontend (HTML)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount static
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
# Kết nối thư mục chứa HTML
templates = Jinja2Templates(directory="frontend")
# tạo route login
@app.get("/auth/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})
# Include route của module "exam"
app.include_router(exam_routes.router, prefix="/api/v1/exam")
app.include_router(patient_routes.route, prefix="/api/v1/patient")
app.include_router(auth_routes.router, prefix="/api/v1/auth")