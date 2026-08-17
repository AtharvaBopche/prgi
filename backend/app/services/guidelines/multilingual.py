from typing import List, Tuple
from app.core.constants import ERR_MULTILINGUAL_MEANING
from app.services.verification.semantic import semantic_service
from app.services.preprocessing.normalizer import normalize_title

class MultilingualChecker:
    def check(self, title: str, candidate_titles: list) -> List[Tuple[str, str, str]]:
        """
        Checks if the title translates to or has identical semantic concept to an existing title.
        """
        violations = []
        norm = normalize_title(title)
        canonical_sub = semantic_service.get_canonical_representation(norm)
        
        for cand in candidate_titles:
            cand_norm = normalize_title(cand)
            cand_canonical = semantic_service.get_canonical_representation(cand_norm)
            
            # If canonical representation matches but original title strings differ
            if canonical_sub == cand_canonical and norm != cand_norm:
                violations.append((
                    ERR_MULTILINGUAL_MEANING,
                    f"Title '{title}' has identical semantic meaning to existing title '{cand}'",
                    f"Both titles map to the same cross-lingual publishing concept: '{canonical_sub}'."
                ))
                break
                
        return violations

multilingual_checker = MultilingualChecker()
