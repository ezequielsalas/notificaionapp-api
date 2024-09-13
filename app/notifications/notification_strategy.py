from abc import ABC, abstractmethod

from app.dtos.message_dto import MessageDTO
from app.dtos.user_dto import UserDTO

class NotificationStrategy(ABC):
    @abstractmethod
    async def send(self, user: UserDTO, message: MessageDTO) -> bool:
        pass
