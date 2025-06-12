from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core import llm_client

router = APIRouter()

class InvoiceRequest(BaseModel):
    policy_text: str
    invoice_text: str

class InvoiceResponse(BaseModel):
    analysis: str

@router.post("/api/invoice/analyze", response_model=InvoiceResponse)
async def analyze_invoices(request: InvoiceRequest):
    try:
        analysis = llm_client.analyze_invoice(request.policy_text, request.invoice_text)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
