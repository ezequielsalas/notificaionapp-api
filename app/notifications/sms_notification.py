#This is the implementation of the NotificationStrategy. We could use Twilio or any other SMS service to send the SMS.
from app.dtos.message_dto import MessageDTO
from app.dtos.user_dto import UserDTO
from app.notifications.notification_strategy import NotificationStrategy
from tenacity import retry, stop_after_attempt, wait_exponential

class SMSNotification(NotificationStrategy):

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def send(self, user: UserDTO, message: MessageDTO) -> bool:
       # Simulating sending an SMS notification
        print(f"Sending SMS to {user.phone_number}: {message.body}")
        return True
