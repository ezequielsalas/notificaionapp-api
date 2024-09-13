from sqlalchemy.orm import Session
from app.repositories.notification_log_repository import NotificationLogRepository

class NotificationLogService:
    def __init__(self):
        self.notification_log_repository = NotificationLogRepository()

    def get_notifications(self, db: Session):
        return self.notification_log_repository.get_notification_logs(db)