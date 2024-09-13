from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dtos.user_dto import UserDTO
from app.services.user_service import UserService
from app.database import get_db

router = APIRouter()
user_service = UserService()

@router.post("/users/")
def create_user(user_data: UserDTO, db: Session = Depends(get_db)):
    return user_service.create_user(db, user_data)

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)
