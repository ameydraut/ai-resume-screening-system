📌 AI Resume Screening System (RAG + Flask + LLM)

This is an AI-powered resume screening system that:

✔ Analyzes multiple resumes
✔ Extracts skills + experience
✔ Matches candidates with job descriptions
✔ Scores and ranks them
✔ Displays results in a clean UI
✔ Allows selecting candidates
✔ Sends interview emails automatically
✔ Uses a custom-built vector database

🚀 Features

🧠 RAG Pipeline (Retrieval + Generation)

📄 Multi-PDF Resume Upload

🔍 Custom Vector Database Built From Scratch

⚡ Semantic Search using MiniLM Embeddings

🤖 LLM (Ollama) for structured candidate evaluation

📧 Automated Interview Email Sending

🌐 Flask Web Interface (Frontend + Backend)

🏗️ Architecture Overview

1. Resume Upload → PDF Parsing
2. Sentence-based chunking (NLTK)
3. Embeddings (all-MiniLM-L6-v2)
4. Custom Vector DB (JSON storage)
5. Job Description → Embedding → Retrieval
6. LLM (Ollama) → Candidate Scoring JSON
7. Flask UI → Candidate Selection → Email Sending

📂 Project Structure
ai-resume-screening-system/
│── app.py
│── utils/
│── templates/
│── static/
│── requirements.txt
│── README.md

🔧 Tech Stack

Python

Flask

NLTK

Sentence Transformers (MiniLM)

Ollama (LLM Inference)

Regex

Custom JSON Vector Database

Bootstrap 5

SMTP Email Automation

🎯 Future Improvements

Google Calendar integration

Meeting link generation

Candidate dashboard

Deployment on AWS / Azure