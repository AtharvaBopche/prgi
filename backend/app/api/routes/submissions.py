from fastapi import APIRouter, Query
from typing import List, Dict, Any
from app.database.repository import repo

router = APIRouter(prefix="/api/submissions", tags=["Submissions"])

@router.get("/", response_model=List[Dict[str, Any]])
def get_submissions(limit: int = Query(100, ge=1, le=500)):
    """Retrieves user application submission history."""
    return repo.get_all_submissions(limit=limit)
