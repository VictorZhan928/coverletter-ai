import os
from openai import OpenAI

# Create OpenAI client using environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(resume: str, job_description: str) -> str:
    """
    Call the OpenAI API to generate a tailored cover letter
    using the provided resume and job description.
    """

    prompt = f"""
You are a professional career coach and cover letter writer.

Create a complete, polished, compelling cover letter written to "Hiring Manager"
based on the following resume and job description.

Resume:
\"\"\"{resume}\"\"\"

Job Description:
\"\"\"{job_description}\"\"\"

Write with:
- A strong introduction
- 1–2 paragraphs highlighting relevant experience
- A professional closing
- Clear alignment with the job description
- No placeholders
- No bullet points
- Professional but warm tone
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",       # or "gpt-4.1" if you want
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    # Extract the generated cover letter text
    return response.choices[0].message.content
