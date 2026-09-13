from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: "UserInfo"


class UserInfo(BaseModel):
    id: str
    email: str


class MeResponse(BaseModel):
    id: str
    email: str
