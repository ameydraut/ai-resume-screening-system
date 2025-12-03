#from sentence_transformers import SentenceTransformer
import math
#import ollama
import pdfplumber
from pathlib import Path
import json

def pdfReader(filename):
    data = []
    i = 0
    file_path = Path(filename)
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            i += 1
            data.append({
                "file_name":file_path.name,
                "page_no": i,
                "text":page.extract_text()+"\n"})
    return data

filename = "C:/Users/ameyd/OneDrive/Desktop/AI Reume Screaning/resume/VatsalChudasama_Resume.pdf"
#print(pdfReader(filename))