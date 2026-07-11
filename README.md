# PDF AI Assistant (RAG)

A simple Retrieval-Augmented Generation (RAG) application built from scratch using **Python**, **FastAPI**, **Ollama**, and **semantic search**.

This project demonstrates the core concepts behind modern RAG systems by manually implementing each stage of the pipeline instead of relying on high-level frameworks.

---

## Features

- Read and extract text from PDF documents
- Split documents into meaningful chunks
- Generate embeddings using Ollama
- Store embeddings locally
- Perform semantic search using cosine similarity
- Retrieve the most relevant document chunks
- Generate context-aware answers using an LLM
- REST API built with FastAPI

---

## Tech Stack

- Python
- FastAPI
- Ollama
- Gemma 3 (1B)
- PyMuPDF (PDF Extraction)
- NumPy
- Cosine Similarity

---

## Project Structure

```
pdf-ai-assistant/
│
├── app.py
├── build_index.py
├── requirements.txt
├── README.md
│
├── data/
│   └── embeddings.json
│
├── documents/
│   └── employee_handbook.pdf
│
└── services/
    ├── chunker.py
    ├── embedding_service.py
    ├── ollama_service.py
    ├── pdf_service.py
    ├── rag_service.py
    ├── search_service.py
    ├── similarity_service.py
    └── storage_service.py
```

---

## How It Works

```
PDF
 │
 ▼
Extract Text
 │
 ▼
Split into Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store Embeddings
 │
 ▼
User Question
 │
 ▼
Generate Question Embedding
 │
 ▼
Cosine Similarity Search
 │
 ▼
Top K Relevant Chunks
 │
 ▼
Prompt Construction
 │
 ▼
Gemma (Ollama)
 │
 ▼
Final Answer
```

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd pdf-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull gemma3:1b
```

Start Ollama:

```bash
ollama serve
```

---

## Build the Embedding Index

Whenever the PDF changes, regenerate the embeddings:

```bash
python build_index.py
```

This creates the local embedding store used during retrieval.

---

## Run the API

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Example Request

```http
POST /ask
```

Request Body

```json
{
  "question": "How many casual leaves are employees entitled to?"
}
```

Example Response

```json
{
  "answer": "Employees are entitled to 20 casual leaves per year."
}
```

---

## Current Limitations

- Uses local JSON storage for embeddings
- Performs linear similarity search
- Supports a single PDF document
- No authentication
- No persistent vector database

---

## Future Improvements

- ChromaDB integration
- FAISS support
- Multi-document support
- Streaming LLM responses
- Docker support
- AWS deployment
- Automated PDF indexing
- Better chunking strategies
- Hybrid search (semantic + keyword)
- Unit tests

---

## Learning Objectives

This project was built to understand the internal workings of a RAG pipeline, including:

- PDF parsing
- Text chunking
- Embeddings
- Vector similarity search
- Prompt engineering
- FastAPI application structure
- LLM integration with Ollama

Instead of relying on external frameworks, each component is implemented manually to better understand how Retrieval-Augmented Generation works under the hood.
