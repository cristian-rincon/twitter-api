import json
from typing import List

from fastapi import APIRouter, status
from fastapi.param_functions import Body

from app.api.v1.models.tweets import Tweet
from app.utils import load_json

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
    return load_json("app/mocks/tweets.json")


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
def create_tweet(tweet: Tweet= Body(...)):
    with open("app/mocks/tweets.json", "r+") as f:
        result = json.loads(f.read())
        new_tweet = tweet.dict()
        new_tweet["tweet_id"] = str(new_tweet["tweet_id"])
        new_tweet["created_at"] = str(new_tweet["created_at"])
        new_tweet["updated_at"] = str(new_tweet["updated_at"])
        new_tweet["by"]["user_id"] = str(new_tweet["by"]["user_id"])
        new_tweet["by"]["birth_date"] = str(new_tweet["by"]["birth_date"])
        result.append(new_tweet)
        f.seek(0)
        f.write(json.dumps(result))
        return new_tweet


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
