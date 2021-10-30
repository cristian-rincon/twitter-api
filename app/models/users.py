from enum import Enum
from typing import Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    user_id: UUID
    email: EmailStr = Field(...)

    is_active: bool = Field(True)
    is_superuser: bool = Field(False)
    username: str = Field(..., min_length=2, max_length=20)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "f5f8c9c0-e8e3-4e7b-b8e0-f9b8c8f9f9f9",
                "email": "johndoe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "birth_date": "2020-01-01",
                "is_active": True,
                "is_superuser": False,
                "username": "johndoe",
                "password": "password",
            }
        }


class User(UserBase):

    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    birth_date: Optional[date] = Field(None)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=20)
