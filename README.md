🚀 AI Cover Letter Generator (FastAPI + Docker)

Generate tailored, professional cover letters automatically using a FastAPI backend powered by OpenAI’s GPT models. This project demonstrates the practical use of Generative AI, containerized deployment, and modern API design.

📘 Overview

This project exposes a REST API endpoint built with FastAPI that generates customized cover letters based on:

A user's resume text, and

A target job description.

The system uses OpenAI's GPT models to produce polished, context-aware cover letters suitable for job applications. The entire application is fully containerized using Docker, enabling portable and consistent deployment.

🧠 Features

✨ AI-Generated Cover Letters
Automatically writes personalized cover letters aligned with job requirements.

⚡ FastAPI Backend
Lightweight, high-performance REST API.

🐳 Dockerized Deployment
Runs identically on any machine using Docker.

🔐 Secure API Key Handling
Uses environment variables — no API keys stored in code or the repository.

📄 Interactive API Documentation
Access via Swagger UI at /docs.

🏗️ Project Architecture
Client (Swagger UI or HTTP Request)
            |
            v
     FastAPI Server
 (POST /generate-cover-letter)
            |
            v
   Cover Letter Generator
       (gen_ai.py)
            |
            v
      OpenAI GPT Model
            |
            v
   JSON Response with
   generated cover letter

📦 Tech Stack

Python 3.11

FastAPI

Uvicorn

OpenAI API (GPT-4.1-mini)

Docker

Pydantic

🛠️ How to Run Locally
1️⃣ Clone the repo
git clone https://github.com/VictorZhan928/coverletter-ai.git
cd coverletter-ai

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set your OpenAI API key (do NOT commit this)

macOS / Linux:

export OPENAI_API_KEY="your_key_here"


Windows PowerShell:

$env:OPENAI_API_KEY="your_key_here"

4️⃣ Start the server
uvicorn main:app --reload

5️⃣ Open the API docs

👉 http://127.0.0.1:8000/docs

Use the POST /generate-cover-letter endpoint:

{
  "resume": "Paste resume text here...",
  "job_description": "Paste job description here..."
}

🐳 Run with Docker
1️⃣ Build the Docker image
docker build -t coverletter-ai .

2️⃣ Run the container (inject your API key securely)

macOS / Linux:

docker run -p 8000:8000 -e OPENAI_API_KEY=$OPENAI_API_KEY coverletter-ai


Windows PowerShell:

docker run -p 8000:8000 -e OPENAI_API_KEY=$env:OPENAI_API_KEY coverletter-ai

3️⃣ Open Swagger UI

👉 http://localhost:8000/docs

📤 API Endpoint
POST /generate-cover-letter

Generates a personalized cover letter.

Request body
{
  "resume": "string",
  "job_description": "string"
}

Response
{
  "cover_letter": "Generated cover letter text..."
}

🔐 Security

This project does not store your OpenAI API key in the repository or code.
Keys are provided securely at runtime via environment variables or Docker -e flags.

🚀 Future Enhancements

Add tone selection (professional, concise, friendly, formal)

Add support for multiple cover letter variations

Add resume parsing from PDF uploads

Add a front-end interface (Streamlit / React)

Add keyword alignment scoring between resume and job description

📝 License

This project is for educational and demonstration purposes.
