from fastapi import FastAPI
from app.api import invoice_analysis

app = FastAPI(
    title="Invoice Analysis API",
    description="API for analyzing invoices against company policies using LLM.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Invoice Analysis API"}

app.include_router(invoice_analysis.router)
