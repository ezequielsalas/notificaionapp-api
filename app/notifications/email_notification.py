from app.dtos.message_dto import MessageDTO
from app.dtos.user_dto import UserDTO
from app.notifications.notification_strategy import NotificationStrategy
from tenacity import retry, stop_after_attempt, wait_exponential
# This is the implementation of the EmailNotification. We could use SendGrid or any other Email service to send the Email.
class EmailNotification(NotificationStrategy):
     
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def send(self, user: UserDTO, message: MessageDTO) -> bool:
        # Simulate Email sending
        print(f"Sending Email to {user.email}: {message.body}")
        return True