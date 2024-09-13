from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dtos.message_dto import  MessageDTO
from app.services.message_service import MessageService
from app.database import get_db
from app.utils.exceptions import HTTPException, NotificationFailedException

router = APIRouter()
message_service = MessageService()

@router.post("/send-notification/")
async def send_message(message: MessageDTO, db: Session = Depends(get_db)):
    try:
        success = await message_service.send_notification(
            db, message=message
        )

        if success:
            return {"status": "success", "detail": "Notification sent successfully"}
        else:
            raise NotificationFailedException("Failed to send notification")
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
