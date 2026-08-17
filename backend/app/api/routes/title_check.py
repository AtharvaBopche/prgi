from fastapi import APIRouter, HTTPException, status
from app.models.submission import SubmissionCreate
from app.models.result import VerificationResult
from app.services.verification.verifier import verifier_service

router = APIRouter(prefix="/api/title-check", tags=["Title Verification"])

@router.post("/verify", response_model=VerificationResult)
def verify_title(payload: SubmissionCreate):
    """
    Submits a title for automated PRGI verification, returning guideline checks,
    highest similarity score, matching titles, verification probability, and final status.
    """
    if not payload.title or not payload.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title string cannot be empty."
        )
        
    result = verifier_service.verify_title(payload.title.strip())
    return result
