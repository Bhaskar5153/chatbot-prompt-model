# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from app.genai_service.llm_call import llm_service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Khazipur TaxBot API",
    description="FastAPI backend for Gemini-powered tax dataset chatbot",
    version="1.0.0"
)

# Allow Streamlit frontend to call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(payload: Query):
    answer = llm_service.get_response(payload.question)
    return {"answer": answer}


@app.get("/")
async def root():
    return {"message": "Khazipur TaxBot API is running"}
