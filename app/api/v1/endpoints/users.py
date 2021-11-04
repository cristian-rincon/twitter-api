import json
from typing import List

from fastapi import APIRouter, Body, HTTPException, Path
from starlette import status

from app.api.v1.models.users import User, UserBase, UserRegister
from app.utils import load_json
router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)


# Signup & Login


@router.post(
    "/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up",
)
def sign_up(user: UserRegister = Body(...)):
    with open("app/mocks/users.json", "r+", encoding="utf-8") as f:
        result = json.loads(f.read())
        new_user = user.dict()
        new_user["user_id"] = str(new_user["user_id"])
        new_user["birth_date"] = str(new_user["birth_date"])
        result.append(new_user)
        f.seek(0)
        f.write(json.dumps(result))
        return new_user



@router.post(
    "/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login"
)
def login(user: User = Body(...)):
    ...


@router.get(
    "/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="List of users",
)
def get_users():
    """List all users"""
    return load_json("app/mocks/users.json")



@router.get(
    "/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get user by id",
)
def get_user(
    user_id: int = Path(..., gt=0, title="User ID", description="ID of the user")
):
    ...


@router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a user"
)
def delete_user():
    ...


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(
    user_id: int = Path(
        ..., gt=0, title="User ID", description="ID of the user", example=1
    ),
    user: UserBase = Body(...),
):
    """Update a user.

    Parameters
    ----------
    -   user_id : int
    -   user : UserBase

    Returns
    -------
    -   User

    """
    return {"user_id": user_id, "user": user}
