# Enterprise GenAI RAG Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103-009688?style=flat-square&logo=fastapi)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI%20%7C%20Gemini-orange?style=flat-square)
![ChromaDB](https://img.shields.io/badge/Vector_DB-Chroma-181717?style=flat-square)

An enterprise-grade, asynchronous AI-powered document screening system. This backend architecture utilizes **FastAPI**, **Retrieval-Augmented Generation (RAG)** paradigms, and advanced NLP techniques to parse textual data and calculate intelligent relevance scores.

---

## ⚙️ System Architecture & Data Flow

Instead of a traditional diagram, the pipeline follows a strict, low-latency asynchronous data flow:

1. 📥 **API Gateway:** FastAPI receives the user query and document metadata.
2. 🧠 **Embedding Generation:** The query is converted into a 1024-dimensional vector.
3. 🔍 **Semantic Retrieval:** Vector Database (ChromaDB) performs a similarity search against stored context.
4. 🔗 **Prompt Orchestration:** Context and query are dynamically chained and sent to the LLM.
5. 📤 **JSON Delivery:** Structured analysis and confidence scores are returned to the client.

---

## ✨ Key Features & Tech Stack

### High-Performance Features
* **Asynchronous Processing:** Built with `asyncio` for non-blocking LLM API calls.
* **Dynamic Prompt Engineering:** Optimized for high-accuracy technical skill extraction.
* **Robust Data Validation:** Strict input/output validation using Pydantic models.

### Core Tech Stack
* **Backend:** Python 3.10+, FastAPI, Pydantic, Uvicorn
* **AI/ML Models:** OpenAI API, Google Gemini, LangChain
* **Embeddings & NLP:** PyTorch, HuggingFace Transformers
* **Database:** ChromaDB (Vector Search), SQLAlchemy

---

## 🛠️ Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/kingryukendo/Enterprise-GenAI-RAG-Pipeline.git](https://github.com/kingryukendo/Enterprise-GenAI-RAG-Pipeline.git)
cd Enterprise-GenAI-RAG-Pipeline
2. Install Dependencies

Bash
pip install -r requirements.txt
3. Run the Server

Bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
📖 API Documentation
Access the interactive Swagger UI at http://localhost:8000/docs.

POST /api/v1/query
Request Payload:

JSON
{
  "document_id": "doc_98765",
  "user_query": "Extract backend and AI skills from this profile.",
  "relevance_threshold": 0.85
}
Success Response (200 OK):

JSON
{
  "status": "success",
  "extracted_skills": ["Python", "FastAPI", "RAG"],
  "confidence_score": 0.92
}
🗺️ Future Roadmap
[ ] RLHF Integration: Reinforcement Learning from Human Feedback for accurate scoring.

[ ] Agentic Workflows: Autonomous LangGraph agents for multi-step reasoning.

[ ] Multi-Modal Support: Parsing images and charts within PDF documents.
