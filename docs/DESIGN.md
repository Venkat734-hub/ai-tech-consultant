# Design Notes (starter template)

## Problem
Small service businesses spend time searching help pages, answering repeated emails, and converting vague meetings into scopes. The system shares one Knowledge Brain so product facts are maintained once.

## Architecture
```text
Help center / local article store
              |
     Python Knowledge Brain API
       /query, /escalations
          /           \
 TypeScript Inbox    Python Meeting-to-Scope
       |                    |
 Draft + human review   Scope + estimate + proposal
       \                    /
        Versioned feedback, audit records, evaluations
```

## Decisions to explain
- Why the Knowledge Brain is an API rather than copied into each task.
- Why the selected retrieval method and storage fit the four-day scope.
- Which Claude model/configuration you tested and why you chose it.
- How image descriptions stay connected to source articles.
- How you prevent unsupported claims and require human approval.

## Deliberately deferred in the starter
- Full sitemap crawler and daily incremental ingestion.
- Vector database, hybrid search and reranking.
- Image downloading and vision model extraction.
- Persistent database, authentication and production deployment.
- Real email provider integration.
- Full agent orchestration and calibrated effort estimates.

## Limitations and next steps
Replace this section with actual limitations discovered during testing. Include the failures you observed and the next improvement you would make.
