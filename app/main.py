from fastapi import FastAPI
from app.api import invoice_analysis, chatbot

app = FastAPI(
    title="Invoice Reimbursement System",
    description="API for invoice analysis and chatbot using LLM.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Invoice Reimbursement System API"}

app.include_router(invoice_analysis.router)
app.include_router(chatbot.router)
