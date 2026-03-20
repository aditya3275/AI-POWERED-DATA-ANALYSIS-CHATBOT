# AI-POWERED-DATA-ANALYSIS-CHATBOT
### Conversational AI for Multi-Format Document Analysis

---

## Overview
An AI-powered chatbot that enables natural language querying over 
structured and unstructured data. Built with LangChain and OpenAI LLMs, 
it supports multi-format document ingestion (PDF, CSV, text) and delivers 
context-aware responses using semantic search via FAISS vector database.

No SQL. No manual filtering. Just ask your data a question.

---

## Key Features
- Multi-format document processing — PDF, CSV, and text files
- FAISS vector database for semantic similarity search
- Document chunking and embeddings generation pipeline
- Context-aware responses over both structured and unstructured data
- Real-time business insights through natural language queries
- Conversational memory for multi-turn query sessions

---

## Architecture
```
User Query
    ↓
Document Ingestion (PDF / CSV / TXT)
    ↓
Text Chunking → Embeddings Generation (OpenAI)
    ↓
FAISS Vector Store
    ↓
Similarity Search → Context Retrieval
    ↓
LangChain LLM Chain (OpenAI)
    ↓
Context-Aware Response
```

---

## Tech Stack
| Layer | Tools |
|-------|-------|
| LLM & Orchestration | LangChain, OpenAI API |
| Vector Database | FAISS |
| Document Processing | PyPDF, CSV Loaders |
| Data Handling | Pandas, NumPy |
| Language | Python |

---

## Use Cases
- Query financial reports in natural language
- Extract insights from large CSV datasets without SQL
- Ask questions over unstructured PDF documents
- Multi-document cross-referencing through semantic search

---

## Getting Started

### Prerequisites
```bash
pip install langchain openai faiss-cpu pandas numpy pypdf streamlit
```

### Environment Setup
```bash
# Add your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

### Run the App
```bash
python app.py
```

---

## Project Structure
```
ai-data-chatbot/
├── app.py                  # Main application entry point
├── document_loader.py      # PDF, CSV, text file loaders
├── embeddings.py           # Embeddings generation pipeline
├── vector_store.py         # FAISS vector store management
├── chain.py                # LangChain LLM chain setup
├── requirements.txt        # Dependencies
└── README.md
```

---

## Results
| Metric | Detail |
|--------|--------|
| Supported formats | PDF, CSV, TXT |
| Search method | Semantic similarity (FAISS) |
| Query type | Natural language, multi-turn |
| Response type | Context-aware, grounded |

---

## Author
Muthyala Aditya
am5771@srmist.edu.in
[LinkedIn] | [GitHub]
