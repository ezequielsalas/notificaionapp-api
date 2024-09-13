"""Seed data

Revision ID: 45d1c9e0e369
Revises: 
Create Date: 2024-09-11 14:24:33.019994

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.category import Category
from app.models.channel import Channel



# revision identifiers, used by Alembic.
revision = '45d1c9e0e369'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    try:
        print("Seeding data")
        # Seed Channels
        if not session.query(Channel).all():
            print("Seeding data 1")
            channel_list = ["E-Mail", "SMS", "Push Notification"]
            for channel_name in channel_list:
                print("Seeding data 2")
                session.add(Channel(name=channel_name))
            print("Seeding data 3")
            session.commit()
        print("Seeding data 4")
        # Seed categories
        if not session.query(Category).all():
            category_list = ["Sports", "Finance", "Movies"]
            for category_name in category_list:
                session.add(Category(name=category_name))
            session.commit()
        
        # Seed users
        if not session.query(User).all():
            
            sports_category = session.query(Category).filter_by(name="Sports").first()
            finance_category = session.query(Category).filter_by(name="Finance").first()
            movies_category = session.query(Category).filter_by(name="Movies").first()

            email_channel = session.query(Channel).filter_by(name="E-Mail").first()
            sms_channel = session.query(Channel).filter_by(name="SMS").first()
            push_channel = session.query(Channel).filter_by(name="Push Notification").first()
        
    
            user_1 = User(name="Peter", email="peter@example.com", phone_number="1234567890")
            user_1.subscribed_categories = [sports_category, movies_category]  
            user_1.channels = [email_channel, sms_channel]
            
            user_2 = User(name="Tony", email="tony@example.com", phone_number="0987654321")
            user_2.subscribed_categories = [finance_category]
            user_2.channels = [push_channel]
        
            session.add(user_1)
            session.add(user_2)
            session.commit()
    finally:
        session.close()
        

def downgrade():
    bind = op.get_bind()
    session = Session(bind=bind)
    try:
        session.query(User).filter(User.email.in_(["peter@example.com", "tony@example.com"])).delete()
        session.commit()
    finally:
        session.close()