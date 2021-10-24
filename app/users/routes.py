from typing import List
from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from .schemas import AccessToken, CreateUser, UserLogin, UserOut
from .crud import user_service
from .dependency import get_current_user
from .jwt import create_token
from ..db.dependency import get_db


user_routes = APIRouter()

@user_routes.post('/register', response_model=UserOut)
def register(user: CreateUser, db: Session = Depends(get_db)):
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

