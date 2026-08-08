
---

# 2. `docs/ARCHITECTURE.md`

This tells the agent **how the pieces fit together**.

```markdown
# Architecture

## 1. Architecture Style

Use a modular monolith.

Do not create microservices.

The system should be structured into independent modules with clear
responsibilities.

---

# 2. High-Level Architecture

```text
                    FastAPI
                       |
             +---------+---------+
             |                   |
          Scrape                Ask
             |                   |
             v                   v
         Scraper             Retrieval
             |                   |
             v                   v
        Extractor            Embeddings
             |                   |
             v                   v
          Cleaner            Vector Store
             |                   |
             +---------+---------+
                       |
                       v
                    Ollama