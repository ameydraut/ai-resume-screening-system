📄 AI Resume Screening System (RAG + Flask + Vector DB)

An AI-powered Resume Screener that analyzes PDF resumes, matches candidates to job descriptions, ranks them by relevance, and allows you to send interview emails instantly.

This project uses a full Retrieval-Augmented Generation (RAG) pipeline with:

🧠 Sentence-transformer embeddings

🤖 LLM (Ollama – Llama 3.2)

📄 PDF reading + chunking

🔍 Custom-built Vector Database (JSON-based)

🌐 Flask web interface

✉ Automated email sending

🚀 Features

📄 Multi-PDF Resume Upload

✂️ Sentence-based chunking (NLTK)

🔎 Semantic search using MiniLM embeddings

🗂 Custom Vector DB (JSON) built from scratch

🤖 LLM (Ollama) for candidate scoring & reasoning

📧 Automated Interview Email Sending

🖥️ Modern Flask Web Interface

🧱 Architecture Overview

Resume Upload → PDF Parsing

Sentence-based Chunking (NLTK)

Embeddings (all-MiniLM-L6-v2)

Custom Vector DB Storage (JSON)

Job Description → Embedding → Retrieval

LLM (Ollama) → Structured Candidate Scoring JSON

Flask UI → Candidate Selection → Email Sending

📂 Project Structure
ai-resume-screening-system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── pipeline.py
│   ├── verctorDB.py
│   ├── chunker.py
│   ├── pdfReader.py
│   ├── embedding.py
│   ├── answergenerattion.py
│   ├── personalEmail.py
│   └── extarxtdata.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/         # optional (CSS/JS)
└── uploads/        # ignored in .gitignore

🛠 Tech Stack

Python

Flask

NLTK (Sentence Tokenization)

Sentence Transformers (MiniLM Embeddings)

Ollama (LLM Inference – Llama 3.2)

Regex

SMTP Email Automation

Bootstrap 5

Custom Vector Database (JSON-based)

📬 Email Integration

Uses environment variables:

SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=


And sends interview emails automatically when a candidate is selected.

⚙️ How to Run Locally
pip install -r requirements.txt
python app.py


Make sure Ollama is installed and running:

ollama run llama3.2

📌 Future Enhancements

Google Calendar meeting scheduling

Candidate dashboard

Re-ranking using cross-encoder

Deployment on AWS/Azure

⭐ About This Project

Built to learn and implement:

Retrieval-Augmented Generation (RAG)

Embeddings & similarity search

Resume parsing with LLMs

Flask backend engineering

Custom vector DB creation

End-to-end AI automation projects

📷 Output
<img width="1918" height="895" alt="Screenshot 2025-12-03 161914" src="https://github.com/user-attachments/assets/ee3cb204-f73f-47a9-a6a0-aec8b69fc4c7" />
<img width="1853" height="908" alt="Screenshot 2025-12-03 161844" src="https://github.com/user-attachments/assets/7a281406-5716-4125-9ffd-fb532b9ed8de" />
<img width="1919" height="844" alt="Screenshot 2025-12-03 161821" src="https://github.com/user-attachments/assets/2bce2296-4970-438a-b7f0-1edc72211088" />



