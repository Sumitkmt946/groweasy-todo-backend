from pydantic import BaseModel, EmailStr
from typing import Optional, List


# ---------- User Schemas ----------

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


# ---------- Auth Schemas ----------

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ---------- Todo Schemas ----------

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    completed: Optional[bool] = None
    title: Optional[str] = None
    description: Optional[str] = None


class TodoOut(TodoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True


class ProfileOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
