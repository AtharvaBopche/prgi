import datetime
from typing import List, Dict, Any
from app.models.result import VerificationResult, GuidelineViolation
from app.models.title import MatchedTitle
from app.services.preprocessing.normalizer import normalize_title
from app.services.guidelines.checker import guideline_engine
from app.services.verification.similarity import compute_title_similarity
from app.services.probability.calculator import calculate_verification_probability
from app.database.repository import repo

class TitleVerifierService:
    def verify_title(self, submitted_title: str) -> VerificationResult:
        """
        Main verification orchestrator:
        1. Preprocess & Normalize
        2. Retrieve Candidates from DB & Submission History
        3. Run Guideline Engine
        4. Run Multi-Algorithm Similarity Engine
        5. Compute Verification Probability & Final Decision Status
        6. Persist Application Submission Record
        """
        norm_title = normalize_title(submitted_title)
        
        # 1. Candidate Retrieval
        db_candidates, sub_candidates = repo.get_candidate_titles(submitted_title)
        candidate_title_strings = [c['title'] for c in db_candidates + sub_candidates]
        registered_titles_set = repo.get_all_registered_titles_set()
        
        # 2. Guideline Enforcement Checks
        violations: List[GuidelineViolation] = guideline_engine.evaluate(
            title=submitted_title,
            candidate_titles=candidate_title_strings,
            registered_titles_set=registered_titles_set
        )
        
        # 3. Similarity Search against Candidates
        matched_titles: List[MatchedTitle] = []
        highest_similarity = 0.0
        
        all_candidates = db_candidates + sub_candidates
        for cand in all_candidates:
            cand_title = cand['title']
            sim_dict = compute_title_similarity(submitted_title, cand_title)
            score = sim_dict['similarity_percentage']
            
            if score > highest_similarity:
                highest_similarity = score
                
            if score >= 30.0:  # Include meaningful candidate matches
                matched_titles.append(MatchedTitle(
                    title=cand_title,
                    similarity_percentage=score,
                    phonetic_match=sim_dict['phonetic_match'],
                    match_type=sim_dict['match_type'],
                    source=cand.get('source', 'database')
                ))
                
        # Sort matched titles by similarity score descending
        matched_titles.sort(key=lambda x: x.similarity_percentage, reverse=True)
        top_matches = matched_titles[:10]  # Keep top 10 relevant matches
        
        # If high similarity violation wasn't caught by explicit guideline modules
        if highest_similarity >= 80.0 and not violations:
            violations.append(GuidelineViolation(
                code="ERR_HIGH_SIMILARITY",
                message=f"Title is {highest_similarity:.1f}% similar to an existing registered title.",
                details=f"Matches '{top_matches[0].title}' with {highest_similarity:.1f}% similarity." if top_matches else None
            ))
            
        # 4. Probability Score & Status Calculation
        probability, status, rejection_summary = calculate_verification_probability(
            highest_similarity=highest_similarity,
            guideline_violations=violations
        )
        
        rejection_reasons = [v.message for v in violations]
        
        # 5. Persist submission application record for future reference
        repo.save_submission(
            submitted_title=submitted_title,
            normalized_title=norm_title,
            similarity_score=highest_similarity,
            verification_probability=probability,
            status=status,
            rejection_reasons=rejection_reasons
        )
        
        return VerificationResult(
            submitted_title=submitted_title,
            normalized_title=norm_title,
            status=status,
            verification_probability=probability,
            highest_similarity=highest_similarity,
            matched_titles=top_matches,
            guideline_violations=violations,
            rejection_summary=rejection_summary,
            processed_at=datetime.datetime.now(datetime.timezone.utc).isoformat()
        )

verifier_service = TitleVerifierService()
