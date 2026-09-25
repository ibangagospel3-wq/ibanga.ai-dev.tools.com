from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field
class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    uuid: str
    full_name: str
    email: EmailStr
    learning_goal: str | None = None
    created_at: datetime
    last_login: datetime | None = None
class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic
