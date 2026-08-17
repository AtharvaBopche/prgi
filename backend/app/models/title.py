from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class TitleBase(BaseModel):
    title: str = Field(..., description="Publication title string")
    language: Optional[str] = Field("English", description="Language of title")
    periodicity: Optional[str] = Field("Daily", description="Publication periodicity")

class TitleCreate(TitleBase):
    pass

class TitleResponse(TitleBase):
    id: int
    normalized_title: str
    soundex_code: Optional[str] = None
    created_at: str

    model_config = ConfigDict(from_attributes=True)

class MatchedTitle(BaseModel):
    title: str
    similarity_percentage: float
    phonetic_match: bool = False
    match_type: str = "fuzzy"  # exact, phonetic, fuzzy, combination, periodicity, semantic
    source: str = "database"  # database or submission_history
