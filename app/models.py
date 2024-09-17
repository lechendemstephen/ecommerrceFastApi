from .database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey



class Users(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    jioned_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=("now()"))



class Blog(Base): 
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=("now()"))

    post_owner = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


class Products(Base): 
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=("now()"))

    post_owner = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)





