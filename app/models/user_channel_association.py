from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

user_channel_association = Table(
    'user_channel_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('channel_id', Integer, ForeignKey('channels.id'), primary_key=True)
)