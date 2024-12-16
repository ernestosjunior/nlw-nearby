import hashlib
from fastapi import APIRouter, HTTPException, status
from config.database import DatabaseSessionDep
from models import Market
from pydantic import BaseModel

class CouponsUpdateReturn(BaseModel):
    coupon: str
    
router = APIRouter(prefix="/coupons", tags=["coupons"])

@router.patch("/{market_id}/")
def update(market_id: str, session: DatabaseSessionDep) -> CouponsUpdateReturn:
    market = session.get(Market, market_id)
    
    if market is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Estabelecimento não encontrado!"
        )
        
    if market.coupons <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Não há cupom disponível no momento!"
        )
        
    market.coupons -= 1
    
    session.commit()
    
    coupon = hashlib.sha256(str(market_id).encode('utf-8')).hexdigest()[:8].upper()
    
    return {"coupon": coupon}