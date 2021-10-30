from fastapi import APIRouter, Body, HTTPException, Path
from starlette import status

from app.models.user import User, UserBase, UserCreated

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=UserCreated, status_code=status.HTTP_201_CREATED)
def create_user(user: User = Body(...)):
    """Create a new user.

    Parameters
    ----------
    -   user : User

    Returns
    -------
    -   UserCreated

    """
    return user


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
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
    mock_users = {
        1: User(
            id=1,
            username="johndoe",
            email="johndoe@example.com",
            first_name="John",
            last_name="Doe",
            age=32,
            hair_color="brown",
            is_active=True,
            is_superuser=False,
            password="hunter21",
        ),
        2: User(
            id=2,
            username="janesmith",
            email="janesmith@example.com",
            first_name="Jane",
            last_name="Smith",
            age=30,
            hair_color="black",
            is_active=False,
            is_superuser=False,
            password="abcdefga",
        ),
    }
    if user_id not in mock_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Userid not found"
        )
    return {"data": mock_users[user_id]}


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
