'''from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "supersecrettoken":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": "admin"}'''

from fastapi import Depends

# Nếu bạn vẫn muốn giữ cấu trúc OAuth2 nhưng bỏ xác thực
from fastapi.security import OAuth2PasswordBearer

# Dummy token scheme để giữ nguyên cấu trúc swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    ⚠️ Phiên bản không xác thực – luôn cho phép truy cập
    """
    return {"username": "anonymous"}

