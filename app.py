from fastapi import FastAPI
from pydantic import BaseModel
from services.ollama_service import ask_llm
from services.pdf_service import get_pdf_text
from services.chunker import split_into_chunks
from services.embedding_service import generate_embedding
from services.rag_service import answer_question
import config.logging_config

app = FastAPI()


class Prompt(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "A.I PDF assistant"}


@app.post("/ask")
def ask_ai(prompt: Prompt):
    answer =  answer_question(prompt.question)
    return {"answer":answer}