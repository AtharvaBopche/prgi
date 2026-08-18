import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import title_check, submissions, database
from app.database.seed import seed_database
from app.core.config import DB_PATH

app = FastAPI(
    title="PRGI Title Verification API",
    description="Automated newspaper & magazine title verification system for Press Registrar General of India",
    version="1.0.0"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(title_check.router)
app.include_router(submissions.router)
app.include_router(database.router)

@app.on_event("startup")
def startup_event():
    # Vercel's deployed filesystem is read-only. When the packaged seeded
    # SQLite file is unavailable, create it in /tmp rather than crashing the
    # function at import time.
    if not os.environ.get("VERCEL") or not DB_PATH.exists():
        seed_database()

@app.get("/")
def root():
    return {
        "system": "PRGI Title Verification API",
        "status": "Online",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
