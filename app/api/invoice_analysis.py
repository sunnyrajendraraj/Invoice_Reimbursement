# from fastapi import APIRouter, UploadFile, File, Form, HTTPException
# from typing import List
# from app.core import pdf_parser, llm_client, vector_store, utils
# import zipfile
# import io

# router = APIRouter()

# @router.post("/analyze")
# async def analyze_invoices(
#     policy_pdf: UploadFile = File(...),
#     invoices_zip: UploadFile = File(...),
#     employee_name: str = Form(...)
# ):
#     # Parse policy PDF text
#     policy_text = await pdf_parser.extract_text_from_pdf(policy_pdf.file)
    
#     # Extract invoice PDFs from ZIP file
#     zip_bytes = await invoices_zip.read()
#     invoice_files = utils.extract_pdfs_from_zip(io.BytesIO(zip_bytes))
    
#     results = []
#     for invoice_file in invoice_files:
#         invoice_text = await pdf_parser.extract_text_from_pdf(invoice_file)
        
#         # Call LLM to analyze invoice against policy
#         analysis = llm_client.analyze_invoice(policy_text, invoice_text)
        
#         # Store in vector store with metadata
#         vector_store.store_embedding(
#             text=invoice_text + " " + analysis['status'] + " " + analysis['reason'],
#             metadata={
#                 "employee_name": employee_name,
#                 "invoice_id": analysis.get("invoice_id", "unknown"),
#                 "status": analysis["status"],
#                 "reason": analysis["reason"],
#                 "date": analysis.get("date", None)
#             }
#         )
        
#         results.append(analysis)
    
#     return {"success": True, "results": results}


from fastapi import APIRouter, HTTPException
from app.core import llm_client

router = APIRouter()

@router.post("/api/invoice/analyze")
async def analyze_invoices(policy_text: str, invoice_text: str):
    try:
        analysis = llm_client.analyze_invoice(policy_text, invoice_text)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
