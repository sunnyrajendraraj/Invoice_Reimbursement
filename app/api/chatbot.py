from fastapi import APIRouter, HTTPException, Form
from app.core import llm_client

router = APIRouter()

@router.post("/api/chatbot")
async def chat_with_bot(message: str = Form(...)):
    try:
        reply = llm_client.call_llm_api(message)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
