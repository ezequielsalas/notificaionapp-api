from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.user_category_association import user_category_association
from app.models.user_channel_association import user_channel_association



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    subscribed_categories = relationship(
        "app.models.category.Category",
        secondary=user_category_association
    )
    channels = relationship(
        "app.models.channel.Channel",
        secondary=user_channel_association
    )