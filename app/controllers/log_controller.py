from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.notification_log_service import NotificationLogService
from app.database import get_db

router = APIRouter()
notification_service = NotificationLogService()


@router.get("/logs/")
def get_logs(db: Session = Depends(get_db)):
    return notification_service.get_notifications(db)
