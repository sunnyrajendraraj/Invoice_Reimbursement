import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

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
