from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from app.posts.schemas import CreatePost, UpdatePost
from ...core.base_crud import CRUDBase
from ..models import  Post



class PostCRUD(CRUDBase[Post, CreatePost, UpdatePost ]):
    """
        Post crud
    """

    def create(self, db: Session, *, obj_in: CreatePost, author_id: int)-> Post:
        obj = jsonable_encoder(obj_in)
        new_obj = self.model(**obj, author_id=author_id)
        db.add(new_obj)
        db.commit()
        db.refresh(new_obj)
        return new_obj
    



post_service = PostCRUD(Post)