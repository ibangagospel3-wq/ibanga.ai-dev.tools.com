from datetime import datetime
from pydantic import BaseModel, ConfigDict
class ProgressPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    lesson_id: int
    completed: bool
    completed_at: datetime | None = None
