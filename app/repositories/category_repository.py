from sqlalchemy.orm import Session
from app.models.category import Category

class CategoryRepository:
    def __init__(self):
        pass

    
    def create_category(self, db: Session, category_name: str):
        category = Category(name=category_name)
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    def get_categories(self,  db: Session):
        return db.query(Category).all()
    
    def get_category_by_name(self,  db: Session, name: str):
        return db.query(Category).filter(Category.name == name).first()