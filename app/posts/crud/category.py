from app.posts.schemas import CreateCategory, UpdateCategory
from ...core.base_crud import CRUDBase
from ..models import  Category


class CategoryCRUD(CRUDBase[Category, CreateCategory, UpdateCategory ]):
    """
        Category crud
    """


category_service = CategoryCRUD(Category)