from typing import Optional

from fastapi import Cookie, FastAPI, File, Header, UploadFile, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Form
from pydantic.networks import EmailStr
from starlette.responses import RedirectResponse

from app.models.auth import LoginResponse
from app.routers.users import router as users_router

app = FastAPI()
app.include_router(users_router)


@app.get("/", status_code=status.HTTP_200_OK)
def home():

    """Redirect to the docs page.

    Returns RedirectResponse
    """
    return RedirectResponse("/docs")


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
        "size-kb": round(len(image.file.read()) / 1024, 2),
    }
