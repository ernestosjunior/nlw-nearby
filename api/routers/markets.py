from fastapi import APIRouter
from sqlmodel import select
from typing import List
from config.database import DatabaseSessionDep
from models import Market, Rule
from pydantic import BaseModel

class MarketsShowReturn(BaseModel):
    market: Market
    rules: List[Rule]

router = APIRouter(prefix="/markets", tags=["markets"])

@router.get("/category/{category_id}/")
def index(category_id: str, session: DatabaseSessionDep) -> List[Market]:
    markets = session.exec(
        select(Market)
        .where(Market.category_id == category_id)
        .order_by(Market.name)) \
    .all()
    
    return [market.model_dump() for market in markets]

@router.get("/{id}/")
def show(id: str, session: DatabaseSessionDep):
    market = session.exec(
        select(Market, Rule)
        .join(Rule)
        .where(Market.id == id)) \
        .all()
    
    return {
        **market[0][0].model_dump(),
        "rules": [rule.model_dump() for _, rule in market]
    }