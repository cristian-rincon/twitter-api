from fastapi import FastAPI

from app.api.v1.endpoints.users import router as users_router
from app.api.v1.endpoints.tweets import router as tweets_router


app = FastAPI()
app.include_router(users_router)
app.include_router(tweets_router)
