from typing import List
from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.users.models import Permission, Role

from .schemas import AccessToken, CreateUser, PermissionCreate, PermissionOut, RoleCreate, RoleOut, UserLogin, UserOut, UserRole, UserRoleOut
from .crud import user_service, permission_service, role_service
from .dependency import get_current_user
from .jwt import create_token
from ..db.dependency import get_db


user_routes = APIRouter()

@user_routes.post('/register', response_model=UserOut)
def register(user: CreateUser,   db: Session = Depends(get_db)):
    if not user_service.get_by_email(db=db, email=user.email):
        return user_service.create(db, user)
        
    raise HTTPException(status_code=400, detail='Email taken')


@user_routes.post('/login', response_model=AccessToken)
def login(user: UserLogin, db: Session = Depends(get_db)):

    if user := user_service.authenticate(db, user.email, user.password):
        return create_token(user.id)

    raise HTTPException(
        status_code=401,
        detail='Incorrect username or password',
        headers={'WWW-Authenticate':'Bearer'}
    )


@user_routes.get('/me', response_model=UserOut)
def profile(user = Depends(get_current_user)):
    return user



@user_routes.get('/users', response_model=List[UserOut])
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all(db)



@user_routes.get('/permissions', response_model=List[PermissionOut])
def get_all_permissiosn(db: Session = Depends(get_db)):
    return permission_service.get_all(db=db)



@user_routes.post('/permission')
def create_permission(obj_in: PermissionCreate, db: Session = Depends(get_db)):
    return permission_service.create(db=db, obj_in=obj_in)



@user_routes.get('/roles', response_model=List[RoleOut])
def get_all_roles(db: Session = Depends(get_db)):
    return role_service.get_all(db=db)



@user_routes.post('/role', response_model=RoleOut)
def create_role(obj_in: RoleCreate, db: Session = Depends(get_db)):
    return role_service.create(db=db, obj_in=obj_in)



@user_routes.post('/assign-user/', response_model=UserRoleOut)
def assign_role(obj_in: UserRole, db: Session = Depends(get_db)):
    return role_service.assign_user(db=db, role_id=obj_in.role_id, user_id=obj_in.user_id)



@user_routes.post('/delete-all')
def delete_all(db: Session = Depends(get_db)):
    db.query(Permission).delete()
    db.query(Role).delete()
    db.commit()
    return {'msg': 'Done!'}


"""
    check_role(['admin', 'manager'])                 ->     role_name in user.roles
    
    check_permissions(['post.edit', 'post.delete'])  ->     perm in user.permissions
"""

