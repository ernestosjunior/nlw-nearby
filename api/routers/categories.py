from fastapi import APIRouter
from sqlmodel import select
from typing import List
from config.database import DatabaseSessionDep
from models import Category

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/")
def index(session: DatabaseSessionDep) -> List[Category]:
    categories = session.exec(
        select(Category)
        .order_by(Category.name)) \
            .all()
            
    return [category.model_dump() for category in categories]
