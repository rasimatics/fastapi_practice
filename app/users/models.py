from sqlalchemy.orm import relationship
from ..db.database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), autoincrement=True, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    full_name = Column(String(length=30), nullable=False)
    description = Column(String(length=100))

    articles = relationship('Post', back_populates='author')


    