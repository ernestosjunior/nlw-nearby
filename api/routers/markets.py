from fastapi import APIRouter, Request
from sqlmodel import select
from typing import List
from config.database import DatabaseSessionDep
from models import Market, Rule
from pydantic import BaseModel
from sqlalchemy.sql import func
from sqlalchemy import and_

class MarketsShowReturn(BaseModel):
    market: Market
    rules: List[Rule]

router = APIRouter(prefix="/markets", tags=["markets"])

@router.get("/category/{category_id}/")
def index(category_id: str, request: Request, session: DatabaseSessionDep) -> List[Market]:
    query_params = dict(request.query_params)
    latitude = float(query_params.get("latitude", 0))
    longitude = float(query_params.get("longitude", 0))
    max_distance_km = float(query_params.get("max_distance", 50))
    
    haversine_formula = (
        6371 * func.acos(
            func.cos(func.radians(latitude))
            * func.cos(func.radians(Market.latitude))
            * func.cos(func.radians(Market.longitude) - func.radians(longitude))
            + func.sin(func.radians(latitude))
            * func.sin(func.radians(Market.latitude))
        )
    )
    
    markets = session.exec(
        select(Market)
        .where(
            and_(
                Market.category_id == category_id,
                haversine_formula <= max_distance_km
            )
        )
        .order_by(haversine_formula)) \
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