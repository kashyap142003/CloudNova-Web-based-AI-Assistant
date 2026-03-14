# CloudNova AI Web Assistant

A production-ready **Retrieval-Augmented Generation (RAG)** AI assistant for CloudNova CRM - demonstrating both **LangChain** and **LlamaIndex** implementations.

## Overview

This project showcases two implementations of the same RAG application:
- **LangChain Version** (`webdemo.py`) - Demonstrates chain-based orchestration
- **LlamaIndex Version** (`webdemo_llamaindex.py`) - Demonstrates data-centric RAG

Both implementations help users get accurate answers about CloudNova CRM products, services, pricing, and features using RAG architecture to prevent hallucinations.

## Features

- **RAG Architecture** - Retrieves relevant context before generating responses
- **Vector Storage** - Persistent embeddings with caching
- **Controlled Responses** - Only answers based on provided documentation
- **Web Interface** - Built with Streamlit for easy interaction
- **Source Attribution** - Shows retrieved documents (LlamaIndex version)
- **Production Practices** - Logging, error handling, caching

## Tech Stack Comparison

| Component | LangChain Version | LlamaIndex Version |
|-----------|------------------|-------------------|
| **Orchestration** | LangChain LCEL | LlamaIndex QueryEngine |
| **Vector DB** | ChromaDB | LlamaIndex VectorStore |
| **Chunking** | RecursiveCharacterTextSplitter | SentenceSplitter |
| **Retrieval** | MMR Search | Similarity Search |
| **Caching** | Persistent ChromaDB | Streamlit + Storage |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │ .txt     │ → │ Chunking │ → │Embedding │              │
│  │Documents │    │(800 char)│    │(OpenAI)  │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                       ↓                     │
│                              ┌──────────────┐               │
│                              │ Vector Store │               │
│                              │ (Persisted)  │               │
│                              └──────────────┘               │
│                                       ↑                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │  Answer  │ ← │   LLM    │ ← │ Retriever│              │
│  │          │    │(GPT-4o)  │    │ (Top K)  │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                       ↑                     │
│                              ┌──────────────┐               │
│                              │ User Query   │               │
│                              └──────────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cloudnova-ai-assistant.git
cd cloudnova-ai-assistant
```

### 2. Create `config.py` file
```python
OPENAI_API_KEY = "your-openrouter-api-key-here"
```

### 3. Choose your implementation

**Option A: LangChain Version**
```bash
pip install -r requirements.txt
streamlit run webdemo.py
```

**Option B: LlamaIndex Version**
```bash
pip install -r requirements_llamaindex.txt
streamlit run webdemo_llamaindex.py
```

## Project Structure

```
CloudNova AI Web Assistant/
├── webdemo.py                  # LangChain implementation
├── webdemo_llamaindex.py       # LlamaIndex implementation
├── config.py                   # API configuration (not in repo)
├── config.example.py           # Example configuration
├── requirements.txt            # LangChain dependencies
├── requirements_llamaindex.txt # LlamaIndex dependencies
├── README.md                   # This file
│
├── # Knowledge Base Documents
├── about.txt                   # Company information
├── faq.txt                     # Frequently asked questions
├── help_docs.txt               # Help documentation
├── pricing.txt                 # Pricing plans
├── product_overview.txt        # Product features
├── services.txt                # Services offered
├── support_policies.txt        # Support information
│
├── # Auto-generated directories
├── chroma_store/               # LangChain vector store
└── llama_index_store/          # LlamaIndex vector store
```

## LangChain vs LlamaIndex

### When to use LangChain (`webdemo.py`)
- Building complex multi-step workflows
- Need fine-grained control over each pipeline step
- Building agents with multiple tools
- Complex conversation management

### When to use LlamaIndex (`webdemo_llamaindex.py`)
- Pure RAG applications (like this one)
- Quick prototyping
- Need advanced document loading (PDFs, databases, APIs)
- Want built-in query optimization

## Key Concepts Demonstrated

### RAG (Retrieval-Augmented Generation)
Combines retrieval system with LLM to answer questions using custom data.

### Embeddings
Numerical vector representations of text for semantic similarity search.

### Chunking
Breaking documents into smaller pieces for efficient retrieval and processing.

### Vector Search
Finding similar documents using cosine similarity between embedding vectors.

### Prompt Engineering
Crafting system prompts to control LLM behavior and output quality.

## Configuration Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `chunk_size` | 800 | Characters per chunk |
| `chunk_overlap` | 150 | Overlap between chunks |
| `similarity_top_k` | 3 | Number of chunks to retrieve |
| `temperature` | 0 | LLM randomness (0 = deterministic) |
| `model` | gpt-4o-mini | Language model |
| `embedding_model` | text-embedding-3-small | Embedding model |

## Interview Talking Points

1. **Why RAG over Fine-Tuning?** - RAG is cheaper, easier to update, and better for factual Q&A
2. **Why persist embeddings?** - API costs, faster startup, production best practice
3. **Why low temperature?** - Consistent, factual responses for Q&A applications
4. **LangChain vs LlamaIndex?** - LangChain for orchestration, LlamaIndex for data-centric RAG

## Disclaimer

CloudNova Systems, Inc. is a fictional company created for demonstration and educational purposes only.

## License

MIT License
