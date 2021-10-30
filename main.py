from typing import Optional

from fastapi import Body, Cookie, FastAPI, File, Header, Path, UploadFile, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Form
from pydantic.networks import EmailStr

from models import LoginResponse, User, UserBase, UserCreated

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}


@app.post("/user", response_model=UserCreated, status_code=status.HTTP_201_CREATED)
def create_user(user: User = Body(...)):
    return user


@app.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user(
    user_id: int = Path(..., gt=0, title="User ID", description="ID of the user")
):
    return {"user_id": user_id}


@app.put("/user/{user_id}", status_code=status.HTTP_200_OK)
def update_user(
    user_id: int = Path(
        ..., gt=0, title="User ID", description="ID of the user", example=1
    ),
    user: UserBase = Body(...),
):
    return {"user_id": user_id, "user": user}


@app.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(
    username: str = Form(...),
    password: str = Form(...),
):
    return LoginResponse(username=username)


# Cookies & Headers


@app.post("/contact", status_code=status.HTTP_200_OK)
def contact(
    name: str = Form(..., min_length=3, max_length=20),
    email: EmailStr = Form(...),
    message: str = Form(..., min_lenght=20, max_length=200),
    user_agent: str = Header(None),
    ads: Optional[str] = Cookie(None),
):
    return user_agent


# Files & Uploads
@app.post("/post-image")
def post_image(
    image: UploadFile = File(...),
):
    return {
        "filename": image.filename,
        "format": image.content_type,
        "size-kb": round(len(image.file.read())/1024, 2),
    }
