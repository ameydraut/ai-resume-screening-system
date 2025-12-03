from sentence_transformers import SentenceTransformer
from .chunker import chunking
from .pdfReader import pdfReader

model = SentenceTransformer("all-MiniLM-L6-v2")
def embedding(chunks):
    text = [entry['chunk'] for entry in chunks]
    vectors = model.encode(text, batch_size=16)
    embed = []
    for entry, vector in zip(chunks,vectors):
        embed.append({
            "file_name": entry['file_name'],
            "page_no": entry['page_no'],
            "chunk_index":entry['chunk_index'],
            "chunk": entry['chunk'],
            "embedding": vector.tolist() 
        })
    return embed

def queryEmbedding(query):
    return model.encode(query)


