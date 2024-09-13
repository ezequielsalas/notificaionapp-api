from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self):
        pass

    def get_user_by_email(self,db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create_user(self,db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    def get_users_by_category(self, db: Session, category_name: str):
        return db.query(User).filter(User.subscribed_categories.any(name=category_name)).all()