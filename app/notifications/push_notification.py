#This is the implementation of the Push notification. Maybe we could use Firebase or any other Push notification service to send the Push notification. 
from app.dtos.message_dto import MessageDTO
from app.dtos.user_dto import UserDTO
from app.notifications.notification_strategy import NotificationStrategy
from tenacity import retry, stop_after_attempt, wait_exponential

class PushNotification(NotificationStrategy):

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def send(self, user: UserDTO, message: MessageDTO) -> bool:
        # Simulate Push notification sending
        print(f"Sending Push notification to {user.phone_number}: {message.body}")
        return True
