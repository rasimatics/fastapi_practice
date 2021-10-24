from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.users.dependency import get_current_user
from app.db.dependency import get_db
from app.posts.schemas import CreatePost, PostOut, UpdatePost
from app.users.models import User
from ..crud.post import post_service
from ..crud.category import category_service

post_routes = APIRouter()


@post_routes.get('/posts', response_model=List[PostOut])
def get_all_posts(db: Session = Depends(get_db)):
    return post_service.get_all(db=db)


@post_routes.get('/post/{id}', response_model=PostOut)
def get_post(id: int, db: Session = Depends(get_db)):
    if post := post_service.get(db=db, id=id):
        return post

    raise HTTPException(
        status_code=404,
        detail='post not found'
    )


@post_routes.post('/posts', response_model=PostOut)
def create_post(obj_in: CreatePost, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if category_service.get(db=db, id=obj_in.category_id):
        return post_service.create(db=db, obj_in=obj_in, author_id=user.id)
        
    raise HTTPException(
        status_code=404,
        detail='Category not found'
    )


@post_routes.put('/post/{id}', response_model=PostOut)
def update_post(id: int, obj_in: UpdatePost, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if not category_service.get(db=db, id=obj_in.category_id):        
        raise HTTPException(
            status_code=404,
            detail='Category not found'
        )
    
    if not post_service.get(db=db, id=id):
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )

    db_obj = post_service.get(db=db, id=id)
    return post_service.update(db=db, obj_in=obj_in, db_obj=db_obj)
    


@post_routes.delete('/post/{id}', response_model=PostOut)
def delete_post(id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if post_service.get(db=db, id=id):
        return post_service.remove(db=db, id=id)
        
    raise HTTPException(
        status_code=404,
        detail='post not found'
    ) 