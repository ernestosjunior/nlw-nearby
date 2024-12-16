import uuid
from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional

class MarketBase(SQLModel):
    name: str
    description: str
    coupons: int
    latitude: float
    longitude: float
    address: str
    phone: str
    cover: str

class Market(MarketBase, table=True):
    __tablename__ = "markets"
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    
    category_id: str = Field(foreign_key="categories.id", index=True)
    category: Optional["Category"] = Relationship(back_populates="markets")
    
    rules: List["Rule"] = Relationship(back_populates="market")