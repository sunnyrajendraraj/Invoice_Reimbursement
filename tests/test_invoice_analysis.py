import pytest
from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO

client = TestClient(app)

def test_invoice_analysis_endpoint():
    # Load sample policy PDF and invoices ZIP from data folder
    with open("data/policy.pdf", "rb") as policy_file, open("data/invoices.zip", "rb") as invoices_file:
        files = {
            "policy_pdf": ("policy.pdf", policy_file, "application/pdf"),
            "invoices_zip": ("invoices.zip", invoices_file, "application/zip"),
        }
        data = {
            "employee_name": "John Doe"
        }
        response = client.post("/api/invoice/analyze", files=files, data=data)
    
    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp.get("success") is True
    assert isinstance(json_resp.get("results"), list)
    # Each result should have status and reason
    for result in json_resp["results"]:
        assert "status" in result
        assert "reason" in result
