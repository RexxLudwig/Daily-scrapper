from fastapi import FastAPI
from app.core.logging import setup_logging

# Setup logging on startup
setup_logging()

app = FastAPI(
    title="Web Intelligence System",
    description="Local web intelligence and Q&A system",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
