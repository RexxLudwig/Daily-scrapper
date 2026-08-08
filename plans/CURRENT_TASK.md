
---

# 8. `plans/CURRENT_TASK.md`

This is actually one of the **most useful files for your AI coding agent**.

Keep only the current task here.

For example, if you're starting from zero:

```markdown
# Current Task

## Phase

Phase 1 — Project Foundation

---

## Objective

Create the initial FastAPI project structure and establish the
configuration and health-check foundation.

---

## Implement

1. Create the project structure defined in `AGENTS.md`.
2. Create FastAPI application.
3. Add `/health`.
4. Add environment configuration.
5. Add Pydantic settings.
6. Add basic logging.
7. Add test infrastructure.
8. Add `.env.example`.
9. Add `requirements.txt`.

---

## Do Not Implement Yet

Do NOT implement:

- Web scraping
- Ollama
- Chroma
- Embeddings
- RAG
- Playwright
- Q&A
- Agents
- MCP

These belong to later phases.

---

## Acceptance Criteria

The following must work:

```bash
uvicorn app.main:app --reload