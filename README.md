# Enterprise GenAI RAG Pipeline

An enterprise-grade, asynchronous AI-powered document screening and ranking system. This backend architecture utilizes **FastAPI**, **Retrieval-Augmented Generation (RAG)** paradigms, and advanced NLP techniques to parse textual data and calculate intelligent relevance scores.

## 🚀 Architecture Overview
- **Backend API:** High-performance RESTful API built with `FastAPI` and structured `Pydantic` models.
- **LLM Orchestration:** Automated prompt chaining utilizing OpenAI/Gemini models for complex data extraction.
- **Vector Search:** Integration ready for Vector Databases (ChromaDB/Pinecone) using 1024-dimensional embeddings (`torch` & `transformers`).
- **Data Validation:** Strict type checking and validation for LLM outputs.

## 📂 Project Structure
```text
Enterprise-GenAI-RAG-Pipeline/
│
├── app/
│   ├── main.py            # FastAPI Application & Endpoints
│   └── rag_engine.py      # Core LLM Chaining & Embedding Logic
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
