from typing import Optional
from sqlalchemy.orm.session import Session
from .schemas import UserDB
from .security import hash_password, verify_password
from ..core.base_crud import CRUDBase
from ..users.models import User



class UserCrud(CRUDBase[User, UserDB, UserDB]):
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email==email).first()


    def create(self, db: Session, obj_in: UserDB) -> User:
        created_data = obj_in.dict()
        created_data.pop('password')
        obj = User(**created_data)
        obj.password = hash_password(obj_in.password)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user



user_service = UserCrud(User)