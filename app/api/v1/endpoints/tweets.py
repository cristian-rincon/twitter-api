from typing import List

from fastapi import APIRouter, status

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
def get_tweets():
    ...


@router.get(
    "/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Get a tweet",
)
def get_tweet():
    ...


@router.post(
    "/",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Create a tweet",
)
def create_tweet():
    ...


@router.put(
    "/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
)
def update_tweet():
    ...


@router.delete(
    "/{tweet_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a tweet",
)
def delete_tweet():
    ...
