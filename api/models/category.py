import uuid
from sqlmodel import Field, Relationship, SQLModel
from typing import List

class CategoryBase(SQLModel):
    name: str

class Category(CategoryBase, table=True):
    __tablename__ = "categories"

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    
    markets: List["Market"] = Relationship(back_populates="category")