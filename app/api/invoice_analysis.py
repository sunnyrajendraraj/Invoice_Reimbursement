from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.core import llm_client

router = APIRouter()

@router.post("/api/invoice/analyze")
async def analyze_invoices(
    policy_file: UploadFile = File(..., description="PDF file of the policy"),
    invoices_zip: UploadFile = File(..., description="ZIP file of invoices"),
    name: str = Form(..., description="Your name")
):
    try:
        # Example: Read the uploaded files (you'll need to implement actual PDF/ZIP parsing)
        policy_content = await policy_file.read()
        invoices_content = await invoices_zip.read()
        # For demonstration, just use file names and name in the prompt
        prompt = (
            f"User: {name}\n"
            f"Policy file: {policy_file.filename} ({len(policy_content)} bytes)\n"
            f"Invoices file: {invoices_zip.filename} ({len(invoices_content)} bytes)\n"
            "Analyze the invoices in the ZIP as per the policy PDF."
        )
        analysis = llm_client.call_llm_api(prompt)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
