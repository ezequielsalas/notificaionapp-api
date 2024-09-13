from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

user_category_association = Table(
    'user_category_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)