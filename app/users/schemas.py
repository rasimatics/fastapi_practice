from typing import Optional
from pydantic import BaseModel, EmailStr


class UserDB(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    description: Optional[str]

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    description: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str


class AccessToken(BaseModel):
    token: str