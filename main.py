from typing import Optional
from fastapi import FastAPI, Body, Query, Path
from models import UserBase

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/user")
def create_user(user: UserBase = Body(...)):
    return user


@app.get("/user")
def get_user(
    name: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        title="Name",
        description="Name of the user",
        example="John Doe",
    ),
    age: Optional[int] = Query(
        ..., gt=0, lt=100, title="User's Age", description="Age of the user", example=42
    ),
):
    return {"name": name, "age": age}


@app.get("/user/{user_id}")
def get_user_by_id(
    user_id: int = Path(..., gt=0, title="User ID", description="ID of the user")
):
    return {"user_id": user_id}


@app.put("/user/{user_id}")
def update_user(
    user_id: int = Path(
        ..., gt=0, title="User ID", description="ID of the user", example=1
    ),
    user: UserBase = Body(...),
):
    return {"user_id": user_id, "user": user}
