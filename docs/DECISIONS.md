
---

# 10. One more file I strongly recommend: `docs/DECISIONS.md`

This solves a major AI-agent problem: **the agent keeps changing decisions that were already made.**

```markdown
# Architecture Decision Records

This file records important architectural decisions.

The coding agent must not reverse these decisions without explicit
instruction.

---

## ADR-001

### Decision

Use a modular monolith.

### Reason

The initial system does not justify microservices.

---

## ADR-002

### Decision

Use Ollama for local LLM inference.

### Reason

The system is designed to run locally and avoid dependency on
cloud LLM APIs.

---

## ADR-003

### Decision

Use Chroma as the initial vector database.

### Reason

It is simple to operate locally and sufficient for the initial
single-machine RAG workload.

---

## ADR-004

### Decision

Use HTTPX first and Playwright as fallback.

### Reason

Browser automation is significantly more expensive than normal
HTTP fetching.

---

## ADR-005

### Decision

Use RAG instead of sending the entire webpage to the LLM.

### Reason

This reduces context size, latency, cost/resource usage, and
improves retrieval relevance.

---

## ADR-006

### Decision

Deterministic code should handle deterministic operations.

### Reason

There is no reason to use an LLM for URL validation, parsing,
chunking, hashing, database operations, etc.