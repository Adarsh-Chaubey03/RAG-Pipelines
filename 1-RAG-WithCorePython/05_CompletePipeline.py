''' 
1. clean_text()
       ↓
2. create_chunks()
       ↓
3. create_embeddings()
       ↓
4. VectorIndex.add()
       ↓
5. Query → model.embed()
       ↓
6. VectorIndex.search()
       ↓
7. top_k

'''

import re
import numpy as np
from fastembed import TextEmbedding


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?-]', ' ', text)
    return text.strip()


def create_chunks(text, chunk_size=500, overlap=100, source="doc.txt"):
    if not text:
        return []

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size")

    text = clean_text(text)

    chunks = []
    start = 0
    chunk_id = 1
    step = chunk_size - overlap

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk,
            "start_idx": start,
            "end_idx": end,
            "word_count": len(chunk.split()),
            "metadata": {
                "source": source
            }
        })

        start += step
        chunk_id += 1

    return chunks


def create_embeddings(chunks):
    if not chunks:
        return []

    model = TextEmbedding()

    texts = [chunk["text"] for chunk in chunks]
    vectors = list(model.embed(texts))

    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector

    return chunks


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class VectorIndex:

    def __init__(self):
        self.items = []

    def add(self, chunks):
        self.items.extend(chunks)

    def search(self, query_vector, top_k=3):
        results = []

        for chunk in self.items:
            score = cosine_similarity(
                query_vector,
                chunk["embedding"]
            )

            results.append((score, chunk))

        results.sort(key=lambda x: x[0], reverse=True)

        return results[:top_k]