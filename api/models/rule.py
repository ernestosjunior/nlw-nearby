import uuid
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional

class RuleBase(SQLModel):
    description: str

class Rule(RuleBase, table=True):
    __tablename__ = "rules"
        
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    
    market_id: str = Field(foreign_key="markets.id", index=True)
    market: Optional["Market"] = Relationship(back_populates="rules")