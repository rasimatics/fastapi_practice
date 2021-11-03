from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator

class UserBase(BaseModel):
    email: EmailStr


class CreateUser(UserBase):
    full_name: str
    password: str
    description: Optional[str]


class UserUpdate(UserBase):
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



class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(PermissionBase):
    pass

class PermissionOut(PermissionBase):
    id: int

    class Config:
        orm_mode = True



class RoleBase(BaseModel):
    name: str

class RoleCreate(PermissionBase):
    permissions: List[int]


class RoleUpdate(PermissionBase):
    pass

class RoleOut(PermissionBase):
    id: int
    permissions: List[PermissionOut]


    class Config:
        orm_mode = True


class RoleOut2(PermissionBase):
    id: int


    class Config:
        orm_mode = True


class UserRole(BaseModel):
    user_id: int
    role_id: int


class UserRoleOut(UserOut):
    roles: List[RoleOut2]

    class Config:
        orm_mode = True