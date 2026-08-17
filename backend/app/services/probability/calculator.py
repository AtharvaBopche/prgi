from typing import Tuple, List
from app.core.constants import STATUS_ACCEPTED, STATUS_REJECTED, STATUS_FLAGGED
from app.models.result import GuidelineViolation

def calculate_verification_probability(
    highest_similarity: float,
    guideline_violations: List[GuidelineViolation]
) -> Tuple[float, str, str]:
    """
    Calculates the verification probability score and final decision status.
    
    Formula requirement:
    Verification Probability <= 100% - Similarity%
    (e.g., if similarity is 80%, probability shall not be more than 100 - 80 = 20%)
    
    If any guideline is explicitly violated, probability is set to 0.0% and status is REJECTED.
    """
    if guideline_violations:
        rejection_summary = "Rejected due to PRGI guideline violation(s): " + "; ".join(v.message for v in guideline_violations)
        return 0.0, STATUS_REJECTED, rejection_summary

    prob = max(0.0, min(100.0, 100.0 - highest_similarity))
    prob = round(prob, 2)
    
    if highest_similarity >= 70.0:
        status = STATUS_REJECTED
        rejection_summary = f"Rejected: Title has high similarity ({highest_similarity:.1f}%) to an existing registered title or application."
    elif highest_similarity >= 40.0:
        status = STATUS_FLAGGED
        rejection_summary = f"Flagged for Review: Title has moderate similarity ({highest_similarity:.1f}%) to existing titles."
    else:
        status = STATUS_ACCEPTED
        rejection_summary = "Eligible: Title is unique and complies with all PRGI submission guidelines."
        
    return prob, status, rejection_summary
