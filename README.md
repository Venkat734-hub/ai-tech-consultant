# AI Tech Consultant — Beginner Starter

This is a **starter scaffold**, not a completed capstone. It gives you a small runnable baseline for all three tasks, sample data, and a step-by-step plan. You must run it, understand it, improve it, and record real evaluation results before submitting.

## What is included
- `task1-knowledge-brain/`: Python + FastAPI knowledge API with a tiny local knowledge base and simple retrieval.
- `task2-inbox-agent/`: TypeScript email drafting client that calls Task 1's API.
- `task3-meeting-to-scope/`: Python script that calls Task 1's API and creates a basic scope draft.
- `data/`: 50 synthetic email examples and 3 sample meeting transcripts (replace/refine these with your own role-play recordings/transcripts).
- `docs/`: architecture, evaluation template, AI log template, and a four-day plan.

## Prerequisites
Install Python 3.11+, Node.js 20+, and Git. An Anthropic API key is optional for the deterministic starter; add one when you implement Claude calls.

## Run Task 1
Open a terminal in the repository root:
```bash
cd task1-knowledge-brain
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Open `http://127.0.0.1:8000/docs` to explore the API.

## Run Task 2 (in a second terminal)
```bash
cd task2-inbox-agent
npm install
npm run draft -- ../data/emails.json 0
```
Task 1 must already be running. This drafts a reply for the first sample email.

## Run Task 3 (in a third terminal)
```bash
cd task3-meeting-to-scope
python -m venv .venv
# activate it as above, then:
pip install -r requirements.txt
python generate_scope.py ../data/transcripts/meeting_1.txt
```
Task 1 must be running. The script writes `scope_output.json`.

## Important limitations
The included retrieval is deliberately simple and is **not production RAG**. It does not yet crawl the real sitemap, understand screenshots, run daily sync, use a vector database, or call Claude. Those are explicit implementation steps in `docs/STEP_BY_STEP.md`. Do not claim those features work until you implement and test them.
