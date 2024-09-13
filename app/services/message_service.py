from sqlalchemy.orm import Session
from app.dtos.message_dto import MessageDTO
from app.notifications.notification import NotificationContext
from app.repositories.user_repository import UserRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.notification_log_repository import NotificationLogRepository
from app.utils.exceptions import NotFoundException, NotificationFailedException
from app.notifications.sms_notification import SMSNotification
from app.notifications.push_notification import PushNotification
from app.notifications.email_notification import EmailNotification
from app.utils.constants import  ChannelType

class MessageService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.category_repo = CategoryRepository()
        self.notification_log_repo = NotificationLogRepository()
        self.context = NotificationContext(SMSNotification())

    
    async def send_notification(self, db: Session, message: MessageDTO):
            try:
                success = False
                notification_type = "N/A"

                # Get category
                category = self.category_repo.get_category_by_name(db, message.category)
        
                if not category:
                    raise NotFoundException("Category not found")

                # Get subscribed users
                subscribed_users = self.user_repo.get_users_by_category(db, category.name ) 
                if not subscribed_users:
                    raise NotFoundException("No users subscribed to this category")

                # Send notifications
                for user in subscribed_users:
                    channel_names = [channel.name for channel in user.channels]
                    
                    if ChannelType.SMS in channel_names :
                        self.context.set_strategy(SMSNotification())
                        notification_type = ChannelType.SMS
                    elif ChannelType.EMAIL in channel_names:
                        self.context.set_strategy(EmailNotification())
                        notification_type = ChannelType.EMAIL
                    elif ChannelType.PUSH in channel_names:
                        self.context.set_strategy(PushNotification())
                        notification_type = ChannelType.PUSH
                    else:
                        raise ValueError(f"Unknown notification method")
                    
                    success = await self.context.send(user, message)

                    if success:
                        print(f"Notification sent to logs")
                        self.notification_log_repo.create_notification_log(db, user.id,message.category, notification_type, "success")
                    else:
                        print(f"Failed to send notification to logs")
                return success
            except Exception as e:
                raise NotificationFailedException("Failed to send notification") from e

          