''' 
chunks
  ↓
extract text
  ↓
FastEmbed
  ↓
vectors
  ↓
zip(chunk, vector)
  ↓
attach embedding
'''
from fastembed import TextEmbedding          # Import FastEmbed's text embedding model

def create_embeddings(chunks):               # Define a function to create embeddings
    if not chunks:                       
        return []                             # Return an empty list if there are no chunks
    
    model = TextEmbedding()                   # Create the FastEmbed model
    
    texts = [chunk["text"] for chunk in chunks]  # Extract text from each chunk
    vectors = list(model.embed(texts))        # Convert each text into an embedding vector
    
    for chunk, vector in zip(chunks, vectors):  # Pair each chunk with its corresponding vector
        chunk["embedding"] = vector           # Store the embedding inside the chunk
    
    return chunks                            