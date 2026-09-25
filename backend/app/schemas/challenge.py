from datetime import datetime
from pydantic import BaseModel, ConfigDict
class ChallengePublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    category: str
    difficulty: str
    starter_html: str
    starter_css: str
    starter_javascript: str
    expected_behavior: str
    created_at: datetime
class SubmissionCreate(BaseModel):
    html_code: str = ""
    css_code: str = ""
    javascript_code: str = ""
class SubmissionResult(BaseModel):
    passed: bool
    message: str
