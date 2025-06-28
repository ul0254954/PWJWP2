from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Ładowanie modelu podsumowywania
summarizer = pipeline("summarization")

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    summary = summarizer(request.text, max_length=150, min_length=30, do_sample=False)
    return {"summary": summary[0]['summary_text']}
