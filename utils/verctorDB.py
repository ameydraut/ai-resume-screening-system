from .pdfReader import pdfReader
from .chunker import chunking
from .embedding import embedding
import json
class vectorDB:
    def __init__(self):
        self.db = []
    def add(self,data,meta):
        for entry in data:
            self.db.append({
                "file_name": entry['file_name'],
                "page_no": entry['page_no'],
                "chunk_index":entry['chunk_index'],
                "chunk": entry['chunk'],
                "embedding": entry['embedding'],
                "name": meta["name"],
                "email": meta["email"],
                "phone": meta["phone"],
                "linkedIn": meta["linkedIn"],
                "github": meta["github"],
                "skills": meta["skills"],
                "education": meta["education"]
            })
    def getAll(self):
        return self.db
    def save(self,file_name = "resume.json"):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(self.db, file, indent=4)
    def load(self,file_name="resume.json"):
        with open(file_name, "r") as file:
            self.db=json.load(file)
            return self.db
    def clear(self):
        self.db = []

    

