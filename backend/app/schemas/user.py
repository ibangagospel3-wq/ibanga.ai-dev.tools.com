from pydantic import BaseModel, Field
class UserUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=2, max_length=120)
    learning_goal: str | None = Field(default=None, max_length=120)
