# RAG — Quick Notes

## RAG Pipeline

```text
Raw Document
     ↓
Clean Text
     ↓
Split into Chunks
     ↓
Create Embeddings
     ↓
Store Vectors
     ↓
Embed Query
     ↓
Similarity Search
     ↓
Top-K Relevant Chunks
```

**Clean → Chunk → Embed → Index → Search**

---

## 1. Cleaning

```python
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?-]', ' ', text)
    return text.strip()
```

- `r'\s+'` → extra whitespace
- `.strip()` → removes leading and trailing whitespace

---

## 2. Chunking

Suppose:

```text
text = 1200 characters
chunk_size = 500
overlap = 100
```

Chunks:

```text
Chunk 1 → 0 to 500
Chunk 2 → 400 to 900
Chunk 3 → 800 to 1200
```

```text
step = chunk_size - overlap
     = 500 - 100
     = 400
```

---

## 3. Chunk Metadata

```python
{
    "chunk_id": chunk_id,
    "text": chunk,
    "start_idx": start,
    "end_idx": end,
    "word_count": len(chunk.split()),
    "metadata": {
        "source": source
    }
}
```

```text
start_idx = start
end_idx = end
word_count = len(chunk.split())
```

---

## 4. Embedding — Basic Concept

An **embedding** converts text into a numerical vector.

```text
Text
 ↓
Embedding Model
 ↓
Numerical Vector
```

Example:

```text
"RAG retrieves relevant documents"
              ↓
       [0.12, -0.34, 0.08, ...]
```

For FastEmbed:

```python
from fastembed import TextEmbedding

model = TextEmbedding()
vectors = list(model.embed(texts))
```

Basic idea:

```text
Text → FastEmbed → Vector
```
