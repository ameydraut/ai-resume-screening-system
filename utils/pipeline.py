from .pdfReader import pdfReader
from .chunker import chunking
from .embedding import embedding
from .extarxtdata import extraxtInfo
from .verctorDB import vectorDB

from pathlib import Path

db = vectorDB()     # keep one DB instance globally

def add_resume_to_db(upload_path):

    pages = pdfReader(upload_path)
    chunks = chunking(pages, 250, 2)

    embeddingOutput = embedding(chunks)
    full_text = " ".join([c["chunk"] for c in chunks])

    extracted = extraxtInfo(full_text)

    db.add(embeddingOutput, extracted)
    db.save()

def generate_final_results(job_description):
    from .answergenerattion import generateAnser
    import json, re
    
    storedData = db.load()
    raw_output = generateAnser(job_description, storedData)

    
    print("\nRAW OUTPUT:\n", raw_output, "\n")

    
    cleaned = raw_output.replace("```", "").strip()

    
    try:
        if cleaned.strip().startswith("["):
            return json.loads(cleaned)
    except:
        pass

   
    list_match = re.search(r"\[.*\]", cleaned, re.S)
    if list_match:
        try:
            return json.loads(list_match.group())
        except:
            pass

   
    objects = re.findall(r"\{.*?\}", cleaned, re.S)
    results = []
    for obj in objects:
        try:
            results.append(json.loads(obj))
        except:
            continue

    if results:
        return results

    
    print("FAILED TO PARSE JSON")
    return []
