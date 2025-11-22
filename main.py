from fastapi import FastAPI
from pydantic import BaseModel
from gen_ai import generate_cover_letter

app = FastAPI(
    title="AI Cover Letter Generator",
    description="Generates tailored cover letters using OpenAI based on a resume and job description.",
    version="1.0.0",
)

class CoverLetterRequest(BaseModel):
    resume: str
    job_description: str

class CoverLetterResponse(BaseModel):
    cover_letter: str

@app.post("/generate-cover-letter", response_model=CoverLetterResponse)
async def create_cover_letter(req: CoverLetterRequest):
    """
    Generate a cover letter from resume + job description.
    """
    cover_text = generate_cover_letter(req.resume, req.job_description)
    return CoverLetterResponse(cover_letter=cover_text)
