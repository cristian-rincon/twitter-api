from typing import List
from fastapi import APIRouter, Body, HTTPException, Path
from starlette import status

from app.models.users import User, UserBase

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)

mock_users = {
    1: User(
        user_id="f5f8c9c0-e8e3-4e7b-b8e0-f9b8c8f9f9f9",
        username="johndoe",
        email="johndoe@example.com",
        first_name="John",
        last_name="Doe",
        is_active=True,
        is_superuser=False,
        password="hunter21",
    ),
    2: User(
        user_id="f5f8c9c0-e8e3-4e7b-b8e0-f9b8c8f9f9f8",
        username="janesmith",
        email="janesmith@example.com",
        first_name="Jane",
        last_name="Smith",
        is_active=False,
        is_superuser=False,
        password="abcdefga",
    ),
}

# Signup & Login


@router.post(
    "/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up",
)
def sign_up(user: User = Body(...)):
    ...


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
    ...


@router.get(
    "/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get user by id",
)
def get_user(
    user_id: int = Path(..., gt=0, title="User ID", description="ID of the user")
):
    """Get a user.

    Parameters
    ----------
    -   user_id : int

    Returns
    -------
    -   User

    """

    if user_id not in mock_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Userid not found"
        )
    return {"data": mock_users[user_id]}


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
