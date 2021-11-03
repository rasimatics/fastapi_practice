from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Boolean
from ..db.database import Base
from sqlalchemy import Column, String, Integer



user_role = Table('user_role', Base.metadata,
    Column('user_id', ForeignKey('users.id', ondelete='cascade'), primary_key=True),
    Column('role_id', ForeignKey('roles.id', ondelete='cascade'), primary_key=True)
)


role_permission = Table('role_permission', Base.metadata,
    Column('role_id', ForeignKey('roles.id', ondelete='cascade'), primary_key=True),
    Column('permission_id', ForeignKey('permissions.id', ondelete='cascade'), primary_key=True)
)



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    full_name = Column(String(length=30), nullable=False)
    description = Column(String(length=100))
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    # relationship
    articles = relationship('Post', back_populates='author', cascade="all, delete", passive_deletes=True)
    roles = relationship("Role", secondary=user_role, back_populates="users", cascade="all, delete", passive_deletes=True)





class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    name = Column(String(length=30))

    # relationship
    permissions = relationship('Permission', secondary=role_permission ,back_populates='roles', cascade="all, delete", passive_deletes=True)
    users = relationship("User", secondary=user_role, back_populates="roles")



class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    name = Column(String(length=50))

    # relationship
    roles = relationship("Role", secondary=role_permission, back_populates="permissions")
    