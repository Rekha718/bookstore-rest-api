from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=100, description="Title of the book")
    author: str = Field(..., min_length=2, max_length=50, description="Author of the book")
    genre: Optional[str] = Field(None, max_length=30, description="Genre of the book")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    quantity: int = Field(..., ge=0, description="Quantity cannot be negative")

class BookCreate(BookBase):
    """Schema for creating a new book"""
    pass

class Book(BookBase):
    """Schema for returning book data"""
    id: int

    class Config:
        from_attributes = True
