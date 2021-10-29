from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class HairColor(str, Enum):
    BLACK = "black"
    BLOND = "blond"
    BROWN = "brown"
    RED = "red"
    GREY = "grey"
    WHITE = "white"


class UserBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=20)
    last_name: str = Field(..., min_length=2, max_length=20)
    age: int = Field(..., ge=18, le=100)
    hair_color: Optional[HairColor] = Field(None)
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    is_active: bool = Field(True)
    is_superuser: bool = Field(False)
    username: str = Field(..., min_length=2, max_length=20)
    

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "age": 25,
                "hair_color": "black",
                "email": "johndoe@example.com",
                "is_active": True,
                "is_superuser": False,
                "username": "johndoe",
                "password": "password",
            }
        }

class User(UserBase):
    password: str = Field(..., min_length=8, max_length=20)

class UserCreated(UserBase):...
    