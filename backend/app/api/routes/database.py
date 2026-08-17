from fastapi import APIRouter, Query
from typing import Dict, Any
from app.database.repository import repo

router = APIRouter(prefix="/api/database", tags=["Database"])

@router.get("/titles")
def get_titles(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    search: str = Query("", description="Optional search term"),
    language: str = Query("all", description="Language filter")
):
    """Retrieves paginated read-only view of registered titles in the PRGI database."""
    return repo.get_paginated_titles(page=page, limit=limit, search=search, language=language)

@router.get("/stats")
def get_stats():
    """Returns database summary statistics."""
    return repo.get_db_stats()
