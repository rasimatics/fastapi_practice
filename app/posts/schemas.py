

from datetime import date, datetime
from pydantic.main import BaseModel


class CategoryBase(BaseModel):
    name: str


class CreateCategory(CategoryBase):
    """
        create new category schema
    """
    

class UpdateCategory(CategoryBase):
    """
        update new category schema
    """


class CategoryOut(CategoryBase):
    id: int
    created: datetime
    updated: datetime


    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    description: str
    content: str
    category_id: int


class CreatePost(PostBase):
    """
        create new post schema
    """


class UpdatePost(PostBase):
    """
        update new post schema
    """


class PostOut(PostBase):
    id: int
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True