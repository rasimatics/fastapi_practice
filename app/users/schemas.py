from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr


class CreateUser(UserBase):
    full_name: str
    password: str
    description: Optional[str]


class UserOut(UserBase):
    id: int
    full_name: str
    description: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    password: str


class AccessToken(BaseModel):
    token: str


class UserDB(UserBase):
    full_name: str
    password: str
    description: Optional[str]

    class Config:
        orm_mode = True


class UserOut(UserBase):
    id: int
    full_name: str
    description: Optional[str]

    class Config:
        orm_mode = True


