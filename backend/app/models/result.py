from pydantic import BaseModel, Field
from typing import List, Optional
from app.models.title import MatchedTitle

class GuidelineViolation(BaseModel):
    code: str
    message: str
    details: Optional[str] = None

class VerificationResult(BaseModel):
    submitted_title: str
    normalized_title: str
    status: str  # ACCEPTED, REJECTED, FLAGGED_FOR_REVIEW
    verification_probability: float  # 0.0 - 100.0%
    highest_similarity: float  # 0.0 - 100.0%
    matched_titles: List[MatchedTitle] = []
    guideline_violations: List[GuidelineViolation] = []
    rejection_summary: Optional[str] = None
    processed_at: str
