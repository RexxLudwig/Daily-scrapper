
---

# 3. `docs/LLM.md`

This is especially important because otherwise coding agents tend to make the LLM do **everything**.

```markdown
# LLM Strategy

## 1. Principle

The LLM is responsible for semantic reasoning.

The LLM is NOT responsible for deterministic operations.

---

# 2. Use Python For

Use normal code for:

- URL validation
- HTTP requests
- HTML parsing
- HTML cleaning
- Token counting
- Chunking
- Hashing
- Metadata extraction
- Database operations
- Vector search
- Validation
- Error handling

---

# 3. Use Ollama For

Use Ollama for:

- Summarization
- Semantic classification when required
- Question answering
- Information synthesis
- Meaning extraction

---

# 4. Model Configuration

Never hard-code the model.

Use:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_LLM_MODEL=qwen3:8b
OLLAMA_EMBEDDING_MODEL=nomic-embed-text