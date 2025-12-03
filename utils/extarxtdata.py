import re
import ast
import ollama
from .cosineSimilarity import cosineSimilarity
from .embedding import embedding
from .embedding import queryEmbedding
from .pdfReader import pdfReader
from .chunker import chunking
from .verctorDB import vectorDB
import json

def preprocess(text):
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = " ".join(text.split())  # collapse extra spaces
    
    # Fix common PDF breaks for emails
    text = text.replace(" @ ", "@")
    text = text.replace(" . ", ".")
    
    return text

def extract_email(text):
    text = preprocess(text)
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else ""

def extract_phone(text):
    text = preprocess(text)
    pattern = r"(\+?\d[\d\s\-]{8,15}\d)"
    match = re.search(pattern, text)
    return match.group().strip() if match else ""

def extract_skills_fallback(text):
    # Add a dictionary of common tech skills
    skill_keywords = [
        "python","java","javascript","c","c++","c#",
        "html","css","react","node","express","django","flask",
        "sql","mysql","postgres","mongodb",
        "aws","azure","gcp","docker","kubernetes",
        "git","linux","bash","powershell",
        "tensorflow","pytorch","sklearn","machine learning",
        "android","kotlin","swift","flutter","dart"
    ]

    # Make text lowercase
    lower_text = text.lower()

    found = []

    for skill in skill_keywords:
        if skill in lower_text:
            found.append(skill.capitalize())

    return list(set(found))


# ---- MAIN EXTRACTION FUNCTION ----
def extract_skills(text):
    prompt = f"""
    Extract all technical skills from this resume.
    Return ONLY a JSON array of strings. No explanation.
    Example:
    ["Java","Python","Android"]

    Text:
    {text}
    """

    resp = ollama.generate(model="llama3.2", prompt=prompt)["response"].strip()

    # STEP 1 — Try direct JSON
    try:
        skills = json.loads(resp)
        if isinstance(skills, list) and skills:
            return skills
    except:
        pass

    # STEP 2 — Extract JSON array inside messy output
    try:
        match = re.search(r"\[.*?\]", resp, re.S)
        if match:
            skills = json.loads(match.group())
            if isinstance(skills, list) and skills:
                return skills
    except:
        pass

    # STEP 3 — Fallback
    fallback = extract_skills_fallback(text)
    return fallback if fallback else []


def extraxtInfo(text):
    info = {}

    info["email"] = extract_email(text)
    info["phone"] = extract_phone(text)
    info["skills"] = extract_skills(text)

    prompt_linkedIn = f"""
    Extract LinkedIn profile name from this resume text.
    Return only the LinkedIn profile name, nothing else.
    Text: {text}
    """
    linkedIn_resp = ollama.generate(model="llama3.2", prompt=prompt_linkedIn)
    info["linkedIn"] = linkedIn_resp["response"].strip()

    prompt_github = f"""
    Extract Github profile name from this resume text.
    Return only the Github profile name, nothing else.
    Text: {text}
    """
    github_resp = ollama.generate(model="llama3.2", prompt=prompt_github)
    info["github"] = github_resp["response"].strip()

    promptName = f""" Extract ONLY the candidate's full name from this text.
    Text: {text},  Return only the name, nothing else."""
    
    nameResponse = ollama.generate(model="llama3.2",prompt=promptName)
    info['name'] = nameResponse["response"].strip()

    prompt_skills = f"""
    Extract all technical skills from this resume text.
    Return them as a Python list.
    Text: {text}
    """

    prompt_edu = f"""
    Extract education details from this resume text.
    Include degree, college and year if present.
    Text: {text}
    """

    edu_resp = ollama.generate(model="llama3.2", prompt=prompt_edu)
    info["education"] = edu_resp["response"].strip()

    return info


