# RAG with LLM

This folder builds on the standard RAG pipeline by adding a language model.
It demonstrates how retrieved document context can be passed to an LLM to
produce a grounded answer.

## Workflow

```text
Documents
    ↓
Load and split text
    ↓
Generate embeddings and store vectors
    ↓
Retrieve relevant context
    ↓
Build a prompt with the context
    ↓
Call the Groq-hosted LLM
    ↓
Generate an answer
```

## Includes

- The document loading, chunking, embedding, vector-store, and retrieval steps
- Simple RAG question answering
- Advanced RAG experiments using a Groq language model
- Environment-based API-key configuration

## Notebook and diagram

- [Open the Advanced RAG with LLM notebook](notebook/AdvancedRAGwithLLM.ipynb)
- [View the LangChain document components diagram](notebook/1-langchain-document-components.svg)

## Prerequisites and installation

- Python 3.13+
- [UV](https://docs.astral.sh/uv/) or a Python virtual environment
- VS Code with the Jupyter extension, or Jupyter Lab
- A [Groq API key](https://console.groq.com/keys)

From this folder, install the notebook dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install langchain langchain-core langchain-community pypdf pymupdf sentence-transformers faiss-cpu chromadb langchain-groq python-dotenv ipykernel
```

Create a `.env` file in this folder:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit a real API key. Run the notebook cells in order after selecting
the project virtual environment as the kernel.

## Project structure

```text
RAG-LLM/
├── data/                 # Source documents and persisted vector store
├── notebook/
│   ├── AdvancedRAGwithLLM.ipynb
│   └── 1-langchain-document-components.svg
└── src/                  # Shared ingestion and retrieval helpers
```
