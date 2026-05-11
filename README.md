# Enterprise GenAI RAG Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103-009688)
![LLM](https://img.shields.io/badge/LLM-OpenAI%20%7C%20Gemini-orange)

An enterprise-grade AI-powered document screening system utilizing FastAPI, RAG paradigms, and advanced NLP.

---

## Architecture Diagram

```mermaid
graph TD
    A[Client Request] --> B[FastAPI Backend]
    B --> C[RAG Engine]
    C --> D[Embeddings]
    C --> E[Vector DB]
    E --> C
    C --> F[LLM API]
    F --> B
    B --> G[JSON Response]
Key Features and Tech Stack
Features
Asynchronous Processing: Built with asyncio for non-blocking LLM API calls.

Dynamic Prompt Engineering: Optimized for high-accuracy technical skill extraction.

Vector Search Integration: Supports 1024-dimensional embeddings for semantic retrieval.

Tech Stack
Core: Python 3.10+, FastAPI, Pydantic

AI/ML: OpenAI API, Gemini, LangChain, PyTorch

Database: ChromaDB (Vector Search)

Setup and Installation
Clone and Install

Bash
git clone [https://github.com/kingryukendo/Enterprise-GenAI-RAG-Pipeline.git](https://github.com/kingryukendo/Enterprise-GenAI-RAG-Pipeline.git)
pip install -r requirements.txt
Run the Server

Bash
uvicorn app.main:app --reload
API Documentation
POST /api/v1/query
Example Request:

JSON
{
  "document_id": "doc_98765",
  "user_query": "Extract backend skills.",
  "relevance_threshold": 0.85
}
Future Roadmap
RLHF Integration: Reinforcement Learning from Human Feedback.

Agentic Workflows: Autonomous LangGraph agents.
