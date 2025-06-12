from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core import llm_client

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/api/chatbot", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    try:
        reply = llm_client.call_llm_api(request.message)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
