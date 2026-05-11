# 🚀 Enterprise GenAI RAG Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103-009688)
![LLM](https://img.shields.io/badge/LLM-OpenAI%20%7C%20Gemini-orange)

An enterprise-grade AI-powered document screening system utilizing **FastAPI**, **RAG** paradigms, and advanced NLP.

---

## 🏗️ Architecture Diagram

```mermaid
graph TD
    A[Client Request] -->|POST /api/v1/query| B(FastAPI Backend)
    B --> C{RAG Engine Orchestrator}
    C -->|1. Generate Embeddings| D[Torch / Transformers]
    C -->|2. Semantic Search| E[(ChromaDB / Vector Store)]
    E -->|3. Retrieved Context| C
    C -->|4. Prompt Chaining| F[OpenAI / Gemini LLM API]
    F -->|5. Analyzed Output| B
    B -->|JSON Response| A
    
    style B fill:#009688,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#f39c12,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#3498db,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#9b59b6,stroke:#fff,stroke-width:2px,color:#fff



✨ Key Features & Tech Stack

Features
Asynchronous Processing: Built with asyncio to handle concurrent LLM API calls without blocking.

Dynamic Prompt Engineering: Multi-stage prompts optimized for extracting technical skills and scoring them against job requirements.

Vector Search Integration: Supports high-dimensional (1024) vector embeddings for accurate semantic retrieval.

Robust Validation: Strict input/output validation using Pydantic models.

Tech Stack
Core: Python 3.10+, FastAPI, Pydantic, Uvicorn

AI/ML: OpenAI API, Google Gemini, LangChain

Embeddings & NLP: PyTorch, HuggingFace Transformers

Database: ChromaDB (Vector Search), SQLAlchemy (Metadata)

Data Handling: NumPy, Pandas

🛠️ Setup & Installation Instructions
1. Clone the repository

Bash
git clone [https://github.com/kingryukendo/Enterprise-GenAI-RAG-Pipeline.git](https://github.com/kingryukendo/Enterprise-GenAI-RAG-Pipeline.git)
cd Enterprise-GenAI-RAG-Pipeline
2. Create a Virtual Environment

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies

Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory:

Code snippet
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
VECTOR_DB_PATH=./data/chroma_db
5. Run the Server

Bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
📖 API Documentation
Access the interactive Swagger UI at http://localhost:8000/docs.

POST /api/v1/query
Processes a document against a user query using the RAG pipeline.

Request Body (JSON):

JSON
{
  "document_id": "doc_98765",
  "user_query": "Extract top backend and AI skills from this candidate's profile.",
  "relevance_threshold": 0.85
}
Success Response (200 OK):

JSON
{
  "status": "success",
  "extracted_skills": ["Python", "FastAPI", "Generative AI", "RAG"],
  "confidence_score": 0.92,
  "llm_response": "Based on the context, the primary skills are strongly aligned with backend AI architecture. Relevant Context found in sections..."
}
🗺️ Future Roadmap
[ ] RLHF Integration: Implement Reinforcement Learning from Human Feedback to improve scoring accuracy.

[ ] Multi-Modal RAG: Add support for parsing images and charts within PDF documents.

[ ] CI/CD Pipeline: Automate testing and deployment using GitHub Actions and Docker.

[ ] Agentic Workflows: Upgrade from simple chaining to autonomous LangGraph/AutoGen agents.
