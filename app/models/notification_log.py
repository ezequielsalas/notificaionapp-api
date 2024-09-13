from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class NotificationLog(Base):
    __tablename__ = "notification_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_type = Column(String) 
    notification_type = Column(String)  # SMS, Email, Push Notification
    status = Column(String)  # Success or Failure
    timestamp = Column(DateTime, default=datetime.utcnow)
    