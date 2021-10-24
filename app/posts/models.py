from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Text
from ..db.base import Base


class Category(Base):
    __tablename__='categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100))
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

    post = relationship('Post', back_populates='categories')


class Post(Base):
    __tablename__='posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    title = Column(String(length=100))
    description = Column(String(length=250))
    content = Column(Text)
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

    author = relationship('User', back_populates='articles')
    categories = relationship('Category', back_populates='post')


