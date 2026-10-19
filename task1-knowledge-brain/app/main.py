from pathlib import Path
import re
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
KB_FILE = ROOT / "knowledge" / "articles.json"
app = FastAPI(title="Knowledge Brain API", version="0.1.0")

class QueryRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)

class Source(BaseModel):
    title: str
    url: str

class QueryResponse(BaseModel):
    answer: str
    status: str
    sources: List[Source]
    needs_human: bool

def load_articles():
    import json
    return json.loads(KB_FILE.read_text(encoding="utf-8"))

def terms(text: str):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    """Starter keyword retrieval. Replace with hybrid/vector retrieval and Claude grounded generation."""
    articles = load_articles()
    q_terms = terms(request.question)
    ranked = []
    for article in articles:
        body = article["title"] + " " + article["content"]
        score = len(q_terms & terms(body))
        if score:
            ranked.append((score, article))
    ranked.sort(key=lambda x: x[0], reverse=True)
    selected = [a for _, a in ranked[:3]]
    if not selected or ranked[0][0] < 2:
        return QueryResponse(
            answer="I couldn't find enough evidence in the current knowledge base. Please ask a human expert to review this question.",
            status="insufficient_evidence", sources=[], needs_human=True
        )
    answer = "Based on the available starter knowledge: " + " ".join(a["content"] for a in selected[:2])
    return QueryResponse(
        answer=answer,
        status="answered",
        sources=[Source(title=a["title"], url=a["url"]) for a in selected],
        needs_human=False
    )

@app.post("/escalations")
def create_escalation(payload: dict):
    """Minimal demo endpoint. Replace with persistent database storage."""
    return {"created": True, "ticket": "ESC-DEMO-001", "question": payload.get("question", "")}