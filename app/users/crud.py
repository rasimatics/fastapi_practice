from typing import Optional
from sqlalchemy.orm.session import Session
from .schemas import CreateUser, RoleCreate, RoleUpdate, UserUpdate, PermissionCreate, PermissionUpdate
from .security import hash_password, verify_password
from ..core.base_crud import CRUDBase
from ..users.models import Permission, Role, User



class UserCrud(CRUDBase[User, CreateUser, UserUpdate]):
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email==email).first()


    def create(self, db: Session, obj_in: CreateUser) -> User:
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



class PermissionCrud(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    pass


permission_service = PermissionCrud(Permission)


class RoleCrud(CRUDBase[Role, RoleCreate, RoleUpdate]):
    
    def create(self, db: Session, *, obj_in: RoleCreate) -> Role:

        new_obj = Role(name=obj_in.name)
        new_obj.permissions  = [permission_service.get(db=db, id=permission_id) for permission_id in obj_in.permissions]
    
        db.add(new_obj)
        db.commit()

        return new_obj

    
    def assign_user(self, db: Session, role_id: int, user_id: int):
        role = self.get(db=db, id=role_id)
        user = user_service.get(db=db, id=user_id)

        # check user and role exist

        if role and user:
            user.roles.append(role)
            db.commit()

        return user

role_service = RoleCrud(Role)
