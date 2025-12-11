from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Authentication Schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# User Response Schema
class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

#Category Schema
class CategoryBase(BaseModel):
    name: str
    type: str

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

# Transaction Schemas
class TransactionCreate(BaseModel):
    amount: Decimal = Field(..., gt=0, description="Transaction amount must be positive")
    description: Optional[str] = None
    category_id: Optional[int] = None
    transaction_date: datetime
    merchant: Optional[str] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "amount": 125.50,
                "description": "Grocery shopping",
                "category_id": 1,
                "transaction_date": "2024-11-29T10:30:00",
                "merchant": "Whole Foods",
                "location": "New York, NY"
            }
        }

class TransactionUpdate(BaseModel):
    amount: Optional[Decimal] = Field(None, gt=0)
    description: Optional[str] = None
    category_id: Optional[int] = None
    transaction_date: Optional[datetime] = None
    merchant: Optional[str] = None
    location: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: Decimal
    description: Optional[str]
    category_id: Optional[int]
    category: Optional[CategoryResponse]
    transaction_date: datetime
    merchant: Optional[str]
    location: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class TransactionListResponse(BaseModel):
    transactions: list[TransactionResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
