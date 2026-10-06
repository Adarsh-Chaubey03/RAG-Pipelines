import re


# Clean Text 
def clean_text(text):
    text=re.sub(r'\s+',' ',text)       
    text=re.sub(r'[^\w\s.,!?-]',' ',text)        
    return text.strip()      

# Clean Text -> Chunk Text
def create_chunks(text, chunk_size=500, overlap=100, source="doc.txt"):
    text = clean_text(text)

    if not text:
        return []

    chunks = []
    start = 0
    chunk_id = 1
    step = chunk_size - overlap

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]

# Add metadata
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

        chunk_id += 1
        start += step

    return chunks