from datetime import datetime
from pydantic import BaseModel, ConfigDict
class LessonPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    slug: str
    category: str
    description: str
    content: str
    difficulty: str
    order_number: int
    created_at: datetime
