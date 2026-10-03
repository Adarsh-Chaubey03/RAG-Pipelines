# RAG Pipelines

A learning and implementation repository for building Retrieval-Augmented
Generation systems, from document retrieval to LLM-powered answers.

## Repository structure

The repository is organized into two focused pipelines:

```text
RAG-Pipelines/
|-- RAG-StandardPipeline/   # Document loading, chunking, embeddings, vector store, and retrieval
`-- RAG-LLM/                # Standard RAG plus prompt construction and LLM-generated answers
```

### [RAG Standard Pipeline](RAG-StandardPipeline/README.md)

The standard pipeline covers document ingestion through vector-store retrieval.
It is useful when you want to inspect or reuse the retrieved context without
calling a language model.

- [Standard RAG notebook](RAG-StandardPipeline/notebook/StandardRAG.ipynb)
- [Document components diagram](RAG-StandardPipeline/notebook/1-langchain-document-components.svg)

### [RAG with LLM](RAG-LLM/README.md)

The LLM pipeline includes all standard RAG stages and adds prompt construction,
Groq LLM calls, and answer generation.

- [Advanced RAG with LLM notebook](RAG-LLM/notebook/AdvancedRAGwithLLM.ipynb)
- [Document components diagram](RAG-LLM/notebook/1-langchain-document-components.svg)

See each folder's README for its workflow, prerequisites, installation steps,
and notebook instructions.
