'''
Suppose:
text = 1200 characters
chunk_size = 500
overlap = 100

The chunks should start approximately:
Chunk 1 → 0 to 500
Chunk 2 → 400 to 900
Chunk 3 → 800 to 1200

Why?
step = chunk_size - overlap
     = 500 - 100
     = 400
'''
# next start = current start + chunk_size − overlap

start = 0

while start < len(text):
    end = min(start+chunk_size,len(text))
    chunk = text[start:end]
    
    start += chunk_size - overlap