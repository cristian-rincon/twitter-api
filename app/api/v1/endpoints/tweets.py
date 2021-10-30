from typing import List

from fastapi import APIRouter, RedirectResponse, status

from app.api.v1.models.tweets import Tweet

router = APIRouter(
    prefix="/api/v1", tags=["tweets"], responses={404: {"description": "Not found"}}
)


@router.get(
    "/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get all tweets",
)
def home():

    """Redirect to the docs page.

    Returns RedirectResponse
    """
    return RedirectResponse("/docs")
