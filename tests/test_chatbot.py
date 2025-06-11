import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chatbot_query():
    query_params = {
        "query": "Show all fully reimbursed invoices for John Doe",
        "employee_name": "John Doe",
        "status": "Fully Reimbursed"
    }
    response = client.get("/api/chatbot/query", params=query_params)
    
    assert response.status_code == 200
    json_resp = response.json()
    assert "response" in json_resp
    assert isinstance(json_resp["response"], str)
