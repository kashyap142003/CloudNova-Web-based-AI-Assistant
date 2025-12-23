# CloudNova AI Web Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant for CloudNova CRM - a fictional company created for demonstration purposes.

## Overview

This AI assistant helps users get accurate answers about CloudNova CRM products, services, pricing, and features using RAG architecture to prevent hallucinations.

## Features

- **RAG Architecture** - Retrieves relevant context before generating responses
- **Vector Database** - Uses ChromaDB for efficient similarity search
- **Controlled Responses** - Only answers based on provided documentation
- **Web Interface** - Built with Streamlit for easy interaction

## Tech Stack

- **Streamlit** - Web interface
- **LangChain** - RAG pipeline orchestration
- **ChromaDB** - Vector database for embeddings
- **OpenAI API** - Language model and embeddings (via OpenRouter)

## Architecture

```
User Query
    ↓
Streamlit UI
    ↓
RAG Pipeline (LangChain)
    ↓
Retriever (ChromaDB with MMR search)
    ↓
Prompt + Context + LLM
    ↓
Answer to User
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/cloudnova-ai-assistant.git
   cd cloudnova-ai-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `config.py` file:
   ```python
   OPENAI_API_KEY = "your-api-key-here"
   ```

4. Run the application:
   ```bash
   streamlit run webdemo.py
   ```

## Project Structure

```
CloudNova AI Web Assistant/
├── webdemo.py              # Main Streamlit app
├── config.py               # API configuration (not in repo)
├── about.txt               # Company information
├── ai_prompt.txt           # AI assistant guidelines
├── faq.txt                 # Frequently asked questions
├── help_docs.txt           # Help documentation
├── pricing.txt             # Pricing plans
├── product_overview.txt    # Product features
├── services.txt            # Services offered
├── support_policies.txt    # Support information
└── chroma_store/           # Vector database (auto-generated)
```

## How It Works

1. **Document Loading**: All `.txt` files are loaded and split into chunks
2. **Embedding**: Text chunks are converted to embeddings using OpenAI's embedding model
3. **Storage**: Embeddings are stored in ChromaDB vector database
4. **Retrieval**: User queries trigger MMR-based similarity search
5. **Generation**: Retrieved context is injected into prompt for LLM to generate accurate answers

## Key Features

- **No Hallucination**: Only answers based on provided documentation
- **Fallback Response**: Returns safe message when context is insufficient
- **MMR Search**: Maximal Marginal Relevance for diverse, relevant results
- **Low Temperature**: Set to 0 for consistent, factual responses

## Disclaimer

CloudNova Systems, Inc. is a fictional company created for demonstration and educational purposes only.

## License

MIT License
