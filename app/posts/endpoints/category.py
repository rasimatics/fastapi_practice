from typing import List
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.posts.schemas import CategoryOut, CreateCategory, UpdateCategory
from ..crud.category import category_service
from ...db.dependency import get_db

category_routes = APIRouter()


@category_routes.get('/categories', response_model=List[CategoryOut])
def get_all_categories(db: Session = Depends(get_db)):
    return category_service.get_all(db=db)


@category_routes.get('/category/{id}', response_model=CategoryOut)
def get_category(id: int, db: Session = Depends(get_db)):
    if category := category_service.get(db=db, id=id):
        return category

    raise HTTPException(
        status_code=404,
        detail='Category not found'
    )


@category_routes.post('/categories', response_model=CategoryOut)
def create_category(obj_in: CreateCategory, db: Session = Depends(get_db)):
    return category_service.create(db=db, obj_in=obj_in)


@category_routes.put('/category/{id}', response_model=CategoryOut)
def update_category(id: int, obj_in: UpdateCategory, db: Session = Depends(get_db)):
    if not category_service.get(db=db, id=id):
        raise HTTPException(
            status_code=404,
            detail='Category not found'
        )

    db_obj = category_service.get(db=db, id=id)
    return category_service.update(db=db, obj_in=obj_in, db_obj=db_obj)


@category_routes.delete('/category/{id}', response_model=CategoryOut)
def delete_category(id: int, db: Session = Depends(get_db)):
    if category_service.get(db=db, id=id):
        return category_service.remove(db=db, id=id)
        
    raise HTTPException(
        status_code=404,
        detail='Category not found'
    ) 