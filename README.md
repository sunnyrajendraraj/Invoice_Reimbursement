# Invoice Reimbursement System

## Overview

Automates invoice PDF analysis against HR policy using LLMs, stores results in a vector DB, and provides a RAG chatbot API for querying.

## Setup

1. **Install Python 3.8+** from [python.org](https://www.python.org/downloads/).  
   Ensure you select "Add Python to PATH" during installation.

2. **Clone this repository and enter the folder:**

### ChromaDB Vector Store

This project uses the latest [ChromaDB PersistentClient API](https://docs.trychroma.com/deployment/migration) for storing and querying invoice embeddings.  
No manual DB setup is required; the database is created in the `.chromadb` folder in your project directory.

