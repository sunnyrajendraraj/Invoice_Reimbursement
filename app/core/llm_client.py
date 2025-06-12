# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def call_llm_api(prompt: str):
#     """
#     Call OpenAI GPT-4 API with the given prompt.
#     """
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "system", "content": "You are an assistant for invoice reimbursement analysis."},
#                   {"role": "user", "content": prompt}],
#         temperature=0
#     )
#     return response.choices[0].message.content

# def analyze_invoice(policy_text: str, invoice_text: str):
#     """
#     Analyze invoice against policy using LLM.
#     Returns dict with keys: status, reason, invoice_id, date.
#     """
#     prompt = f"""
# You are a reimbursement assistant. Given the HR reimbursement policy below:

# {policy_text}

# Analyze the following invoice text:

# {invoice_text}

# Determine the reimbursement status: Fully Reimbursed, Partially Reimbursed, or Declined.
# Explain the reason for your decision.

# Return the answer in JSON format with keys:
# - status
# - reason
# - invoice_id (if available)
# - date (if available)
# """
#     response = call_llm_api(prompt)
#     import json
#     try:
#         return json.loads(response)
#     except json.JSONDecodeError:
#         # fallback if response is not valid JSON
#         return {"status": "Declined", "reason": "Could not parse LLM response", "invoice_id": None, "date": None}

# def generate_chat_response(query: str, docs: list):
#     """
#     Generate chatbot response using LLM with context documents.
#     """
#     context = "\n\n".join([f"Invoice Analysis:\n{doc['document']}\nMetadata: {doc['metadata']}" for doc in docs])
#     prompt = f"""
# You are a helpful assistant answering questions about invoice reimbursements.

# Context:
# {context}

# User question:
# {query}

# Answer in markdown format.
# """
#     return call_llm_api(prompt)


import openai

# Instantiate the OpenAI client (ensure your API key is securely loaded)
client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")

def call_llm_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # or your preferred model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def analyze_invoice(policy_text, invoice_text):
    prompt = f"Policy: {policy_text}\nInvoice: {invoice_text}\nAnalyze the invoice as per the policy."
    return call_llm_api(prompt)
