from pydantic import BaseModel, Field

from pydantic import BaseModel

class MessageDTO(BaseModel):
    category: str
    body: str