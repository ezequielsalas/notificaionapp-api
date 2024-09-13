from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.user_channel_association import user_channel_association


class Channel(Base):
    __tablename__ = "channels"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)  # SMS, Email, Push Notification