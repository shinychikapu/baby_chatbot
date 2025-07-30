from typing import List, Literal, Optional
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None  # Still optional for future flexibility

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatResponse(BaseModel):
    reply: str
    messages: List[ChatMessage]
