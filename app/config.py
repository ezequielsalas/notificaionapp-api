import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./notification.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")


API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = os.getenv("API_PORT", "8000")

