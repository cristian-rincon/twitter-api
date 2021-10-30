from pydantic import BaseModel, Field



class LoginResponse(BaseModel):
    username: str = Field(
        ...,
        min_length=2,
        max_length=20,
        description="Username of the user",
        example="johndoe",
    )
    message: str = Field(default="You have successfully logged in")
