from .cosineSimilarity import cosineSimilarity
from .embedding import embedding
from .embedding import queryEmbedding
from .pdfReader import pdfReader
from .chunker import chunking
from .verctorDB import vectorDB
from collections import defaultdict

def searchDB(db,query,topk):
    query_embedding = queryEmbedding(query)
    candidate_group = defaultdict(list)
    similarity= 0
    score = []
    best_candidate = []
    for entry in db :
        similarity = cosineSimilarity(entry['embedding'],query_embedding)
        score.append({
            "score": similarity,
            "file_name": entry['file_name'],
            "page_no": entry['page_no'],
            "chunk_index":entry['chunk_index'],
            "chunk": entry['chunk'],
            "embedding": entry['embedding'],
            "name": entry["name"],
            "email": entry["email"],
            "phone": entry["phone"],
            "linkedIn": entry["linkedIn"],
            "github": entry["github"],
            "skills": entry["skills"],
            "education": entry["education"]
        })

    for s in score:
        candidate_group[s["name"]].append(s)

    for name , chunks in candidate_group.items():
        best_chunk = max(chunks ,key=lambda x:x["score"])
        best_candidate.append(best_chunk)

    best_candidate.sort(key=lambda x:x["score"], reverse=True)
    return best_candidate[:topk]

