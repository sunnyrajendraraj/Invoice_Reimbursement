from fastapi import APIRouter, Query
from app.core import llm_client, vector_store

router = APIRouter()

@router.get("/query")
async def query_chatbot(
    query: str,
    employee_name: str = None,
    status: str = None,
    date: str = None
):
    # Build metadata filters
    filters = {}
    if employee_name:
        filters["employee_name"] = employee_name
    if status:
        filters["status"] = status
    if date:
        filters["date"] = date
    
    # Retrieve relevant documents from vector store
    docs = vector_store.similarity_search(query, filters)
    
    # Generate chatbot response with context
    response = llm_client.generate_chat_response(query, docs)
    
    return {"response": response}
