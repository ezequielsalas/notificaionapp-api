from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.notification_log import NotificationLog

class NotificationLogRepository:
    def __init__(self):
        pass

    def create_notification_log(self, db: Session, user_id: int, category_type: str, notification_type: str, status: str):
        log = NotificationLog (
             user_id = user_id,
            category_type = category_type, 
            notification_type = notification_type,
            status = status)
        
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def get_notification_logs(self, db: Session):
        return db.query(NotificationLog).order_by(desc(NotificationLog.timestamp)).all()