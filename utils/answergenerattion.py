import ollama
from .VectoreSearch import searchDB
from .extarxtdata import extraxtInfo
from .cosineSimilarity import cosineSimilarity
from .embedding import embedding
from .embedding import queryEmbedding
from .pdfReader import pdfReader
from .chunker import chunking
from .verctorDB import vectorDB

def candidate_formater(meta ,index):
    return f"""Candidate -{index+1}
            Name: {meta['name']}
            Email: {meta['email']}
            Phone: {meta['phone']}
            LinkedIn: {meta['linkedIn']}
            GitHub: {meta['github']}
            Skills: {meta['skills']}
            Education: {meta['education']}"""

def generateAnser(query,db):
    retrieved_data= searchDB(db,query,3)
    candidate_text = " ".join([candidate_formater(meta, i) for i , meta in enumerate(retrieved_data)])
    prompt = f"""
            You are an AI Resume Screening Agent. Compare the job requirements with the candidate’s resume.

            Only use the exact job description provided. Do NOT generate extra job requirements.

            Job Description:
            {query}

            Candidate Information:{candidate_text}

            Return the list of candidates and result in this JSON format only:

            {{
            "Candidate Name": "<Name>"
            "email": "<candidate email>",
            "match_score": "<percentage>",
            "reason": "<why the candidate is or isn't a good match>",
            "matched_skills": [...],
            "missing_skills": [...],
            "recommendation": "<hire / interview / reject>"
            "candiadte skills": "<dislpay all the skills he/she has>"
            }}
            """

    genRespose = ollama.generate(model="llama3.2", prompt=prompt)

    return genRespose['response'].strip()
    
    


"""db = vectorDB()
db.load()
pages = pdfReader("C:/Users/ameyd/OneDrive/Desktop/AI Reume Screaning/resume/VatsalChudasama_resume.pdf.")
chunks = chunking(pages, 250, 2)
embeddingoutput = embedding(chunks)
full_text = " ".join([c["chunk"] for c in chunks])
data = extraxtInfo(full_text)
db.add(embeddingoutput,data)
db.save()
query =
Answer = generateAnser(query,db.getAll())
print(data)
print("Response", Answer)"""
"""Solid grip on Android fundamentals and the Android SDK
Comfort with Kotlin, REST APIs, Git, and third-party libraries
Bonus points if you’ve done a prior internship in Android development
Most importantly: a curious mind and a builder’s mindset"""