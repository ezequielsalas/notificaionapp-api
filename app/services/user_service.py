from sqlalchemy.orm import Session
from app.dtos.user_dto import UserDTO
from app.repositories.user_repository import UserRepository
from app.repositories.category_repository import CategoryRepository

from app.models.user import User
from app.utils.exceptions import NotFoundException, ConflictException

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.category_repo = CategoryRepository()

    def create_user(self, db: Session, user_data: UserDTO):
        # Check if user already exists
        existing_user = self.user_repo.get_user_by_email(db, user_data.email)
        if existing_user:
            raise ConflictException("User already registered with this email")
        
        # Retrieve categories and channels
        categories = self.category_repo.get_categories_by_names(db,user_data.subscribed_categories)
        channels = self.channel_repo.get_channels_by_names(db, user_data.channels)
        
        if not categories or not channels:
            raise NotFoundException("One or more categories or channels are invalid")

        # Create and save the user
        new_user = User(name=user_data.name, email=user_data.email, phone=user_data.phone)
        new_user.subscribed_categories = categories
        new_user.channels = channels
        return self.user_repo.create_user(new_user)
    
    def get_user_by_id(self, db: Session, user_id: int):
        user = self.user_repo.get_user_by_id(db, user_id)
        if not user:
            raise NotFoundException("User not found")
        return user
