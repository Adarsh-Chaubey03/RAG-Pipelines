# RAG Standard Pipeline

This folder contains the standard Retrieval-Augmented Generation (RAG) pipeline
without a language model. It focuses on preparing documents, storing their
embeddings, and retrieving relevant context for a query.

## Workflow

```text
Documents (PDF/TXT)
        ↓
Load and extract text
        ↓
Split text into overlapping chunks
        ↓
Generate embeddings
        ↓
Persist embeddings in ChromaDB
        ↓
Retrieve the most relevant chunks
```

## Includes

- PDF and text document loading
- Text chunking with overlap
- Sentence-transformer embeddings
- ChromaDB vector storage
- Similarity search and context retrieval

The pipeline stops after retrieval. It does not call an LLM or generate a
natural-language answer.

## Notebook and diagram

- [Open the Standard RAG notebook](notebook/StandardRAG.ipynb)
- [View the LangChain document components diagram](notebook/1-langchain-document-components.svg)

## Prerequisites and installation

- Python 3.13+
- [UV](https://docs.astral.sh/uv/) or a Python virtual environment
- VS Code with the Jupyter extension, or Jupyter Lab

From this folder, install the dependencies with:

```powershell
uv sync
```

Alternatively, create a virtual environment and install
[`requirements.txt`](requirements.txt):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Place source documents in [`data/`](data/) and run the notebook cells in order.

## Project structure

```text
RAG-StandardPipeline/
├── data/                 # Source documents and persisted vector store
├── notebook/
│   ├── StandardRAG.ipynb
│   └── 1-langchain-document-components.svg
├── src/                  # Reusable loading, embedding, search, and storage code
├── pyproject.toml
└── requirements.txt
```
