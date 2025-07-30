from fastapi import APIRouter
from app.models.chat import ChatRequest, ChatResponse, ChatMessage
from app.services.openai_service import get_openai_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply, messages = await get_openai_response(request.message)
    
    # Convert raw message dicts to ChatMessage models for Pydantic validation
    message_objects = [ChatMessage(**msg) for msg in messages]
    
    return ChatResponse(reply=reply, messages=message_objects)
