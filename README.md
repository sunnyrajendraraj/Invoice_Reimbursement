# 📄 Invoice Reimbursement System

## 🌐 Live Demo

👉 [Click here to view the live project]( https://invoice-reimbursement.onrender.com/docs)

## 1. 💡 Project Overview: What and Why

The **Invoice Reimbursement System** is an intelligent automation solution designed to simplify and streamline the process of employee invoice reimbursement in an organization. It addresses a common pain point in many companies: manual, error-prone review of expense invoices against complex HR reimbursement policies.

### Why this system?

- ❌ Manual invoice review is time-consuming and inconsistent.
- 🧠 Policies can be complex, requiring detailed interpretation.
- ⏱ Employees and finance teams need transparency and quick feedback.
- 📊 Storing and querying reimbursement decisions efficiently is critical for audits and queries.

This system automates invoice analysis using the power of **Large Language Models (LLMs)**, stores results intelligently, and provides a **natural language chatbot interface** for querying invoice statuses.

---

## 2. ⚙️ Core Components: What the System Does

The system consists of **two main API endpoints** built using **FastAPI**:

### 🧾 Part One: Invoice Reimbursement Analysis Endpoint

#### 🔽 Input:
- HR reimbursement **policy PDF** file describing the company’s rules.
- A **ZIP** file containing one or more employee invoice PDFs.
- **Employee name** to link the invoices to a specific individual.

#### ⚙️ Processing:
- **PDF Parsing**: Extract text using robust tools like `PyMuPDF`.
- **LLM Analysis**: Use OpenAI GPT (or similar) to analyze invoice against policy:
  - Classify as `Fully Reimbursed`, `Partially Reimbursed`, or `Declined`
  - Provide detailed reasoning using policy clauses.
- **Vector Embeddings**: Use `Sentence-Transformers` or OpenAI to generate embeddings.
- **Storage**: Save invoice metadata and embeddings into a **vector database** like `ChromaDB`.

#### 📤 Output:
A JSON response indicating task success/failure and detailed reimbursement decisions.

---

### 💬 Part Two: RAG LLM Chatbot Endpoint

#### 🔽 Input:
A **natural language query** from a user (e.g., filters like name, date, status).

#### ⚙️ Processing:
- **Vector Search**: Embed query, retrieve matching invoice analyses.
- **Metadata Filtering**: Filter by employee, status, date, etc.
- **RAG (Retrieval Augmented Generation)**: LLM generates a coherent response in markdown using retrieved context.

#### 📤 Output:
A helpful, human-readable **markdown-formatted** response summarizing relevant invoice data.

---

## 3. 🔄 Technical Workflow: How It Works

### Step 1: Upload to Invoice Analysis Endpoint
- User POSTs policy PDF + invoices ZIP + employee name.
- System extracts text, constructs prompt, calls LLM.
- Structured JSON result returned per invoice.
- Embeddings are generated and stored in ChromaDB.

### Step 2: Query via Chatbot Endpoint
- User submits a query via `/query-invoices`.
- Query is embedded and used to perform semantic + metadata-based search.
- LLM generates a context-aware markdown answer.

---

## 4. 🤖 Why Use LLMs and Vector Stores?

- **LLMs** provide deep understanding of policy language & invoice reasoning.
- **Vector stores** enable semantic search beyond keyword matching.
- **RAG** blends LLM reasoning with relevant document retrieval = accurate & reliable output.

---

## 5. 🛠️ Technology Stack and Tools

| Layer           | Tool/Library                      |
|----------------|-----------------------------------|
| Language        | Python                            |
| API Framework   | FastAPI                           |
| PDF Parsing     | PyMuPDF                           |
| LLMs            | OpenAI GPT / HuggingFace Models   |
| Embeddings      | Sentence-Transformers / OpenAI    |
| Vector Database | ChromaDB                          |
| Prompt Engine   | Custom prompt engineering         |
| Testing         | Pytest                            |

---

## 6. 📜 Detailed Explanation of Prompts

### 🧾 Invoice Analysis Prompt
- Instructs the LLM to:
  - Compare invoice to policy.
  - Decide status (fully / partial / declined).
  - Explain reasoning.
- Prompt ensures **structured JSON** output.

### 💬 Chatbot Prompt
- Instructs the LLM to:
  - Use retrieved invoices as context.
  - Respond clearly and accurately.
  - Format response in **Markdown**.
  - Consider **chat history** (context-awareness).

---

## 7. 🧩 Challenges and Solutions

| Challenge                  | Solution                                              |
|---------------------------|-------------------------------------------------------|
| Parsing PDFs              | Used PyMuPDF for robustness across formats            |
| LLM Output Consistency    | Enforced structured JSON via prompt design            |
| Efficient Search          | Combined semantic vector search + metadata filtering  |
| Input Error Handling      | API validates files and returns informative messages  |

---

## 8. 🚀 How the System Runs

1. FastAPI server runs two endpoints: `/analyze-invoices`, `/query-invoices`
2. User interacts via Swagger UI or any HTTP client (e.g., curl, Postman).
3. Files are processed asynchronously using LLMs.
4. Embeddings + metadata are stored in vector DB.
5. Chatbot leverages retrieval + LLM to answer invoice queries in markdown.

---

## 9. 📈 Use Cases and Benefits

| User Type    | Benefits                                                  |
|--------------|-----------------------------------------------------------|
| Employees    | Get quick answers to "Was my invoice reimbursed?"        |
| Finance Team | Automate bulk validation with full audit trail           |
| Managers     | Track employee reimbursements over time                  |
| Auditors     | Access well-organized, explainable reimbursement history |

---

## 10. ✅ Summary

This **Invoice Reimbursement System** combines cutting-edge NLP, prompt engineering, and vector search to revolutionize how companies handle expense reimbursements.

It provides:
- 🔍 Transparency
- ⚡ Speed
- ✅ Accuracy
- 🔄 Scalability

With modular components and robust APIs, the system is ready for real-world deployment or extension into full web interfaces.

---
