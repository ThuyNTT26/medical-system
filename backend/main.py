# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.exam import routes as exam_routes

app = FastAPI(title="Medical Management System")

# Cho phép gọi từ frontend (HTML)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route của module "exam"
app.include_router(exam_routes.router, prefix="/api/v1/exam")
