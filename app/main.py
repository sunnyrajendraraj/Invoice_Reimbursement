# from dotenv import load_dotenv
# load_dotenv()

# from fastapi import FastAPI
# from app.api import invoice_analysis, chatbot

# app = FastAPI(title="Invoice Reimbursement System")

# app.include_router(invoice_analysis.router, prefix="/api/invoice", tags=["Invoice Analysis"])
# app.include_router(chatbot.router, prefix="/api/chatbot", tags=["Chatbot"])


from fastapi import FastAPI
from app.api import invoice_analysis

app = FastAPI()

app.include_router(invoice_analysis.router)
