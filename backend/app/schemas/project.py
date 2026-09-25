from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
class ProjectBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str | None = None
    html_code: str = ""
    css_code: str = ""
    javascript_code: str = ""
class ProjectCreate(ProjectBase): pass
class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = None
    html_code: str | None = None
    css_code: str | None = None
    javascript_code: str | None = None
class ProjectPublic(ProjectBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
