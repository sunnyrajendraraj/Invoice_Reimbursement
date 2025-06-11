from pydantic import BaseModel
from typing import Optional, List

class InvoiceAnalysisRequest(BaseModel):
    employee_name: str

class InvoiceAnalysisResponse(BaseModel):
    status: str
    reason: str
    invoice_id: Optional[str]
    date: Optional[str]

class ChatbotResponse(BaseModel):
    response: str
