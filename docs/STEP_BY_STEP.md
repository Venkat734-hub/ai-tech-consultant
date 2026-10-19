# Step-by-step guide for a beginner

## First: understand the three pieces
1. **Knowledge Brain (Python):** stores searchable product help and answers questions with sources.
2. **Inbox Agent (TypeScript):** reads an email and asks the Knowledge Brain for evidence before drafting a response.
3. **Meeting-to-Scope (Python):** reads a transcript, checks the Knowledge Brain, and prepares a draft scope for human review.

The starter is intentionally small. It proves the API connection; it does not complete all capstone requirements.

## Day 1 — Make Task 1 run
1. Install Python 3.11 or newer.
2. Open a terminal in `task1-knowledge-brain`.
3. Create and activate a virtual environment, install `requirements.txt`, and start Uvicorn using the README commands.
4. Open `/docs`; try `/health`, then `/query`.
5. Ask a question about the logo or payment settings. Inspect the returned source URLs.
6. Ask an unrelated question. Confirm that the system says it lacks evidence.
7. Next, implement sitemap fetching from `https://support.brilliantdirectories.com/support/sitemap.xml`. Start with a small batch, obey robots/access rules, add rate limits, retries, and a saved checkpoint.
8. Parse article text and image URLs. Keep each image linked to its article. Add vision descriptions only after text ingestion works.
9. Replace keyword matching with hybrid retrieval or embeddings. Keep a fixed set of test questions.
10. Add daily incremental sync: new/changed pages reprocess, removed pages deactivate.

## Day 2 — Build Task 2
1. Leave Task 1 running.
2. Install Node.js 20+, then run `npm install` inside `task2-inbox-agent`.
3. Run `npm run draft -- ../data/emails.json 0`.
4. Try other indexes, for example `npm run draft -- ../data/emails.json 12`.
5. Inspect whether sources are relevant and whether the draft promises anything unsupported.
6. Improve classification, structured output validation, timeout handling, and a review UI.
7. Record every human edit and final reply. Version prompts and compare old/new versions on the same tests.
8. Implement the 20-consecutive-unchanged-drafts eligibility counter, but keep high-risk categories human-approved.

## Day 3 — Build Task 3
1. Keep Task 1 running.
2. Install Python dependencies inside `task3-meeting-to-scope`.
3. Run `python generate_scope.py ../data/transcripts/meeting_1.txt`.
4. Open `scope_output.json`. It is a cautious starter draft, not a final client proposal.
5. Improve transcript extraction into structured requirements with IDs, source passages, assumptions, and open questions.
6. Call Task 1 for each major requirement to check documented product features.
7. Add an estimate table and proposal generator. Require human approval.
8. Process `meeting_3_followup.txt` against the original approved baseline. Show added, modified, removed, and potentially out-of-scope items.

## Day 4 — Evaluate, document, demo
1. Write at least 20 cases for each task. Use unseen cases for final testing.
2. Compare at least two Claude model/configuration choices as appropriate. Use the same test inputs.
3. Record measured correctness, citation support, latency, cost, errors, and safety failures. Never invent numbers.
4. Add retries, logs, tests, and clear failure messages.
5. Finish `README.md`, `DESIGN.md`, `EVALS.md`, and `AI_LOG.md`.
6. Record a demo under 10 minutes. Show all three tasks and one real failure.
7. Commit your own progress each day. Keep your coding-assistant conversation history.

## Important safety rules
- Never put API keys in source code or Git.
- Never let the model approve refunds, prices, dates, or contracts by itself.
- Do not send real customer email automatically in this capstone.
- Treat retrieved pages and emails as untrusted input.
- Do not say an article or image feature works until you have tested it.
