from app.dtos.message_dto import MessageDTO
from app.dtos.user_dto import UserDTO
from app.notifications.notification_strategy import NotificationStrategy

class NotificationContext:
    def __init__(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def send(self, user: UserDTO, message: MessageDTO):
        return  self._strategy.send( user, message)
