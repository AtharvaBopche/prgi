from app.services.verification.fuzzy import (
    levenshtein_ratio,
    token_sort_ratio,
    token_set_ratio,
    jaccard_ngram_similarity
)
from app.services.verification.phonetic import calculate_phonetic_similarity
from app.services.verification.semantic import semantic_service
from app.services.preprocessing.normalizer import normalize_title

def compute_title_similarity(t1: str, t2: str) -> dict:
    """
    Computes comprehensive similarity metrics between two publication titles.
    Returns composite percentage, match type breakdown, and component scores.
    """
    norm1 = normalize_title(t1)
    norm2 = normalize_title(t2)
    
    if norm1 == norm2:
        return {
            "similarity_percentage": 100.0,
            "match_type": "exact",
            "phonetic_match": True,
            "fuzzy_ratio": 100.0,
            "token_ratio": 100.0,
            "phonetic_ratio": 100.0,
            "semantic_ratio": 100.0
        }
        
    lev_ratio = levenshtein_ratio(norm1, norm2)
    tok_sort = token_sort_ratio(norm1, norm2)
    tok_set = token_set_ratio(norm1, norm2)
    ngram_sim = jaccard_ngram_similarity(norm1, norm2, n=3)
    phon_sim = calculate_phonetic_similarity(norm1, norm2)
    sem_sim = semantic_service.calculate_semantic_similarity(norm1, norm2)
    
    # Highest fuzzy edit metric
    fuzzy_max = max(lev_ratio, tok_sort, tok_set, ngram_sim)
    
    # Weighted calculation
    # 40% Token/Fuzzy, 30% Edit distance, 20% Phonetic, 10% Semantic
    composite = (0.40 * max(tok_sort, tok_set)) + (0.30 * lev_ratio) + (0.20 * phon_sim) + (0.10 * sem_sim)
    
    # Special boost for high phonetic match with small edit distance difference (e.g. Namaskar vs Namascar)
    if phon_sim >= 90.0 and lev_ratio >= 75.0:
        composite = max(composite, 85.0)
        
    # Determine primary match type
    match_type = "fuzzy"
    if norm1 == norm2:
        match_type = "exact"
    elif sem_sim >= 90.0:
        match_type = "semantic"
    elif phon_sim >= 85.0:
        match_type = "phonetic"
    elif tok_set >= 90.0:
        match_type = "token"
        
    return {
        "similarity_percentage": round(min(100.0, max(composite, fuzzy_max * 0.9)), 2),
        "match_type": match_type,
        "phonetic_match": (phon_sim >= 75.0),
        "fuzzy_ratio": round(lev_ratio, 2),
        "token_ratio": round(max(tok_sort, tok_set), 2),
        "phonetic_ratio": round(phon_sim, 2),
        "semantic_ratio": round(sem_sim, 2)
    }
