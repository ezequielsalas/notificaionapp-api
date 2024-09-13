from pydantic import BaseModel, EmailStr
from typing import List

class UserDTO(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    subscribed_categories: List[str]
    channels: List[str]  