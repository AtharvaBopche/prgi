from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class SubmissionCreate(BaseModel):
    title: str = Field(..., min_length=2, description="Submitted title for verification")
    owner_name: Optional[str] = Field(None, description="Optional applicant owner name")

class SubmissionResponse(BaseModel):
    id: int
    application_id: str
    submitted_title: str
    normalized_title: str
    similarity_score: float
    verification_probability: float
    status: str
    rejection_reasons: List[str]
    submitted_at: str

    model_config = ConfigDict(from_attributes=True)
