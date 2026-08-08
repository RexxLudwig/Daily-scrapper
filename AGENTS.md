# AGENTS.md

## Project: Local Web Intelligence & Q&A System

## 1. Project Objective

Build a production-quality local web intelligence system that accepts a URL, extracts meaningful content from the webpage, generates a concise semantic understanding of the content using a local Ollama LLM, and allows users to ask questions about the scraped webpage.

The system must prioritize:

- Accurate webpage extraction
- Clean and meaningful content
- Local LLM inference through Ollama
- Retrieval-Augmented Generation (RAG) for large webpages
- Short, factual answers
- Low hallucination
- Source/section traceability
- Modular architecture
- Good error handling
- Testability
- Production-oriented engineering practices

The system should NOT simply dump raw HTML into the LLM.

---

# 2. Core User Flow

The primary workflow is:

```text
User
  |
  | URL
  v
URL Validator
  |
  v
Web Fetcher
  |
  +---- Normal HTML ----> HTTPX/Requests
  |
  +---- JS-heavy page ---> Playwright
  |
  v
Content Extractor
  |
  v
Content Cleaner
  |
  v
Structured Document
  |
  +--------------------+
  |                    |
  v                    v
Summary Generator   Chunking
                         |
                         v
                    Embeddings
                         |
                         v
                    Vector Store
                         |
                         v
                    User Question
                         |
                         v
                    Retrieval
                         |
                         v
                    Ollama LLM
                         |
                         v
                     Answer