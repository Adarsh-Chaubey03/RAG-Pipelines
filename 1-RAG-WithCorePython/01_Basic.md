# RAG          (Retrieval-Augmented Generation)

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
## 5. In-Memory Vector Indexing

### Basic Concept

Store chunk embeddings in memory so that a query can be compared against them.

```text
Chunks
   ↓
Embeddings
   ↓
Vector Index
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-K Relevant Chunks
```
### What do we store?
Suppose we have:
```
vectors = [    [0.1, 0.2, 0.3],    [0.8, 0.1, 0.4],    [0.2, 0.9, 0.1]]
```

Each vector belongs to a chunk:

Vector 0 → Chunk 0

Vector 1 → Chunk 1

Vector 2 → Chunk 2

For a simple assessment, we can keep them in memory using a Python list.

### Cosine Similarity

Used to measure similarity between two vectors.

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

**Higher score → more similar/relevant.**

### Simple Vector Index

```python
class VectorIndex:
    def __init__(self):
        self.items = []

    def add(self, chunks):
        self.items.extend(chunks)
```

### Search

```python
def search(self, query_vector, top_k=3):
    results = []

    for chunk in self.items:
        score = cosine_similarity(query_vector, chunk["embedding"])
        results.append((score, chunk))

    results.sort(key=lambda x: x[0], reverse=True)

    return results[:top_k]
```

### Remember

```text
Compare → Score → Sort → Top-K
```

**Key Python:**
- `np.dot()` → dot product
- `np.linalg.norm()` → vector magnitude
- `sort(..., reverse=True)` → highest score first
- `[:top_k]` → select top results

## 6 — Module Separation



The idea is simply:

> Don't put cleaning, chunking, embedding, and indexing into one huge function. Separate them into modules/functions/classes.

### Remember this structure

```text
RAG Pipeline
│
├── preprocessing.py
│      ├── clean_text()
│      └── create_chunks()
│
├── embeddings.py
│      └── create_embeddings()
│
├── vector_index.py
│      └── VectorIndex
│
└── main.py
       └── connects everything
```

### What each module does

| Module | Responsibility |
|---|---|
| `preprocessing.py` | Clean + chunk |
| `embeddings.py` | Text → vectors |
| `vector_index.py` | Store + search vectors |
| `main.py` | Run the pipeline |

### Basic import pattern

```python
from preprocessing import clean_text, create_chunks
from embeddings import create_embeddings
from vector_index import VectorIndex
```

### Pipeline in `main.py`

```python
text
 ↓
clean_text()
 ↓
create_chunks()
 ↓
create_embeddings()
 ↓
VectorIndex.add()
 ↓
VectorIndex.search()
```


```text
One module → One main responsibility
```



