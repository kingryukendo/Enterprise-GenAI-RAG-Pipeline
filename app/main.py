import os
import asyncio
import logging
from fastapi import FastAPI, HTTPException, BackgroundTasks, Security
from pydantic import BaseModel, Field
from rag_engine import RAGPipeline

# Initialize Logging and App
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Enterprise GenAI RAG Pipeline API",
    description="API for document screening and technical skill extraction using LLMs and Vector DBs.",
    version="1.0.0"
)

# Initialize the RAG Engine
rag_engine = RAGPipeline()

class QueryRequest(BaseModel):
    document_id: str = Field(..., description="Unique ID of the document")
    user_query: str = Field(..., description="Query to run against the document")
    relevance_threshold: float = Field(default=0.75, description="Minimum similarity score")

class QueryResponse(BaseModel):
    status: str
    extracted_skills: list
    confidence_score: float
    llm_response: str

@app.post("/api/v1/query", response_model=QueryResponse)
async def process_document_query(request: QueryRequest):
    try:
        logger.info(f"Processing query for document: {request.document_id}")
        
        # Asynchronous call to RAG Engine
        result = await rag_engine.process_query(
            doc_id=request.document_id,
            query=request.user_query,
            threshold=request.relevance_threshold
        )
        
        return QueryResponse(
            status="success",
            extracted_skills=result.get("skills", []),
            confidence_score=result.get("score", 0.0),
            llm_response=result.get("answer", "")
        )
        
    except Exception as e:
        logger.error(f"Pipeline Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal RAG Pipeline Error")

@app.get("/health")
def health_check():
    return {"status": "System Operational", "vector_db": "Connected"}
