# Pramana — Defense Procurement Intelligence Assistant

Pramana is a RAG-powered assistant that lets analysts query defense procurement
documents — RFPs, federal acquisition regulations, and technical manuals — in plain
English and get answers grounded in the actual source text, with citations.

The name comes from the Sanskrit term for valid evidence or proof — fitting for a
system built specifically to answer only from what it can point back to in the
source documents.

---
# Project Overview

Defense procurement involves dense, compliance-heavy documents that are slow to search
manually. Pramana ingests these documents, indexes them for retrieval, and answers
questions using only the retrieved text — refusing to answer when nothing relevant is
found, rather than guessing.

---
# Core Capabilities

Document Ingestion → Chunking → Embedding → Hybrid Retrieval (BM25 + Vector) →
Reranking → Grounded Answer Generation → Citation Output

---
# System Architecture

PDF Documents (RFPs, regulations, manuals)
       ↓
Parsing & Section-Aware Chunking
       ↓
Embedding Generation
       ↓
pgvector (PostgreSQL)  ←→  BM25 Keyword Index
       ↓
Hybrid Retrieval + Cross-Encoder Reranking
       ↓
Claude API (answer generation with citations)
       ↓
FastAPI Backend
       ↓
React Frontend (auth required)

---
# Technology Stack

Backend Framework:
- FastAPI (async)

RAG:
- LangChain / LlamaIndex, pgvector, BM25 (rank-bm25), cross-encoder reranker

LLM:
- Claude API (Anthropic)

Database:
- PostgreSQL with pgvector extension

Auth:
- JWT

Frontend:
- React

Observability:
- LangSmith (RAG tracing)

Cloud:
- AWS ECS, RDS, S3, CloudFront

Containers:
- Docker, docker-compose

CI/CD:
- GitHub Actions → ECR → ECS

---
# Key Modules

Core Platform
- Config management, logging, auth, modular API routes

RAG Pipeline
- Document ingestion and section-aware chunking
- Embedding generation and pgvector storage
- Hybrid retrieval (semantic + keyword)
- Cross-encoder reranking
- Citation-grounded answer generation

Evaluation
- Retrieval recall@k measurement
- Answer groundedness scoring (% of answer sentences traceable to retrieved chunks)

---
# API Endpoints

Health check
GET /health

Ask a question
POST /query
Body: { "question": "What are the cybersecurity requirements in section 5?" }

Example response:
{
  "answer": "Section 5 requires...",
  "citations": [
    { "document": "RFP-2026-0143.pdf", "section": "5.2", "score": 0.91 }
  ]
}

---
# Installation

git clone https://github.com/yourusername/pramana.git
cd pramana
cp .env.example .env
docker-compose up -d
pip install -r requirements.txt
python scripts/ingest_docs.py
uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs

---
# Project Status

In development — RAG pipeline and hybrid retrieval functional locally. AWS deployment
and CI/CD pipeline in progress.

---
# Author

Built to learn production-grade RAG architecture — hybrid retrieval, reranking,
and hallucination mitigation through grounded citation.
