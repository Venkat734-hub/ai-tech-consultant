"""Basic transcript-to-scope starter. Calls Task 1 API for feasibility context."""
import json
import sys
from pathlib import Path
import requests

KB_API = "http://127.0.0.1:8000"

def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python generate_scope.py path/to/transcript.txt")
    transcript_path = Path(sys.argv[1])
    transcript = transcript_path.read_text(encoding="utf-8")
    question = "Check existing product capabilities relevant to these meeting notes:\n" + transcript[:5000]
    try:
        result = requests.post(f"{KB_API}/query", json={"question": question}, timeout=10)
        result.raise_for_status()
        knowledge = result.json()
    except requests.RequestException as exc:
        raise SystemExit(f"Knowledge Brain API unavailable: {exc}") from exc

    # This is a transparent baseline, not an AI-generated final estimate.
    output = {
        "project_name": transcript_path.stem,
        "transcript_file": str(transcript_path),
        "requirements": [
            {"id":"REQ-001","description":"Review transcript and confirm exact requested behavior",
             "status":"needs_human_confirmation","acceptance_criteria":"Client confirms measurable expected behavior"}
        ],
        "knowledge_check": knowledge,
        "scope": {
            "deliverables":["Requirements clarification","Technical feasibility review"],
            "exclusions":["Unconfirmed features and third-party work"],
            "open_questions":["Which exact behavior should change?","What is the target deadline and budget?"]
        },
        "estimate": {"status":"not_estimated","reason":"A human must confirm requirements before a responsible estimate can be produced."},
        "proposal_status":"draft_requires_human_approval"
    }
    Path("scope_output.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
    print("Wrote scope_output.json. Review and complete it; do not send it to a client as-is.")

if __name__ == "__main__":
    main()
