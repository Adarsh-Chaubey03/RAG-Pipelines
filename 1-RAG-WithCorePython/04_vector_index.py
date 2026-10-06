'''Chunks
   ↓
Embeddings
   ↓
Vector Index
   ↓
Search'''

#  Store vectors so that when a query comes in, we can find the most similar chunks.

'''Query Vector
     ↓
Compare with all stored vectors
     ↓
Similarity scores
     ↓
Sort highest → lowest
     ↓
Top-K chunks'''

import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))             # Calculate cosine similarity


class VectorIndex:

    def __init__(self):
        self.items = []                                                       # Store chunks and embeddings

    def add(self, chunks):
        self.items.extend(chunks)                                             # Add chunks to the index

    def search(self, query_vector, top_k=3):
        results = []                                                         # Store similarity scores and chunks

        for chunk in self.items:
            score = cosine_similarity(query_vector, chunk["embedding"])      # Compare query with chunk
            results.append((score, chunk))                                   # Store score and chunk

        results.sort(key=lambda x: x[0], reverse=True)                       # Sort by highest similarity

        return results[:top_k]                                               # Return top-K relevant chunks