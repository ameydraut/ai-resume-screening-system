import nltk
from .pdfReader import pdfReader
nltk.download('punkt')
nltk.download('punkt_tab')

def chunking(data,chunk_size, overlap):
    chunk = []
    for entry in data:
        split_sentence=nltk.sent_tokenize(entry['text'])
        buffer = []
        current_length = 0
        chunk_index = 0
        for sentence in split_sentence:
            if current_length + len(sentence) < chunk_size:
                buffer.append(sentence)
                current_length += len(sentence)
            
            else:
                chunk.append({
                    "file_name":entry['file_name'],
                    "page_no":entry['page_no'],
                    "chunk_index": chunk_index,
                    "chunk":" ".join(buffer)
                })
                buffer=buffer[-overlap:]
                current_length = sum(len(s) for s in buffer)
                buffer.append(sentence)
                chunk_index += 1
        if buffer:
            chunk.append({
                "file_name": entry['file_name'],
                "page_no": entry['page_no'],
                "chunk_index": chunk_index,
                "chunk": " ".join(buffer)
            })
            
    return chunk



