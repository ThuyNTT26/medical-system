from pydantic import BaseModel

class DangNhapData(BaseModel):
    tenDangNhap: str
    matKhau: str

class LoginRequest(BaseModel):
    tenDangNhap: str
    matKhau: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RegisterRequest(BaseModel):
    tenDangNhap: str
    matKhau: str
    vaiTro: str = "user"
