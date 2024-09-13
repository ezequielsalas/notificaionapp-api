from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAEnum, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message_type = Column(String, index=False)
    notification_type = Column(String, index=False)
    timestamp = Column(DateTime, default=datetime.utcnow)