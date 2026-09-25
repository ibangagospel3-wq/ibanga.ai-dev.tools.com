from datetime import datetime
from pydantic import BaseModel, Field
class AIChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)
    html_code: str | None = None
    css_code: str | None = None
    javascript_code: str | None = None
    conversation_id: int | None = None
class AIChatResponse(BaseModel):
    response: str
    conversation_id: int
    model: str
    timestamp: datetime
class CodeRequest(BaseModel):
    language: str = Field(min_length=1, max_length=30)
    code: str = Field(min_length=1, max_length=30000)
class DebugRequest(CodeRequest):
    error: str = Field(min_length=1, max_length=5000)
class ImproveRequest(BaseModel):
    html_code: str = ""
    css_code: str = ""
    javascript_code: str = ""
class GenerateRequest(BaseModel):
    request: str = Field(min_length=1, max_length=5000)
class TeachRequest(BaseModel):
    concept: str = Field(min_length=1, max_length=200)
class ConversationPublic(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
class MessagePublic(BaseModel):
    role: str
    content: str
    created_at: datetime
