from typing import List

def levenshtein_distance(s1: str, s2: str) -> int:
    """Computes exact Levenshtein edit distance between s1 and s2."""
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def levenshtein_ratio(s1: str, s2: str) -> float:
    """Computes normalized Levenshtein similarity ratio between 0.0 and 100.0%."""
    if not s1 and not s2:
        return 100.0
    if not s1 or not s2:
        return 0.0
    dist = levenshtein_distance(s1, s2)
    max_len = max(len(s1), len(s2))
    return (1.0 - (dist / max_len)) * 100.0

def token_sort_ratio(s1: str, s2: str) -> float:
    """Computes similarity after sorting tokens alphabetically."""
    t1 = " ".join(sorted(s1.split()))
    t2 = " ".join(sorted(s2.split()))
    return levenshtein_ratio(t1, t2)

def token_set_ratio(s1: str, s2: str) -> float:
    """Computes similarity taking unique token intersection and set differences into account."""
    tokens1 = set(s1.split())
    tokens2 = set(s2.split())
    
    intersection = tokens1.intersection(tokens2)
    diff1 = tokens1 - tokens2
    diff2 = tokens2 - tokens1
    
    sorted_inter = " ".join(sorted(list(intersection)))
    sorted_d1 = " ".join(sorted(list(diff1)))
    sorted_d2 = " ".join(sorted(list(diff2)))
    
    t1 = (sorted_inter + " " + sorted_d1).strip()
    t2 = (sorted_inter + " " + sorted_d2).strip()
    
    r1 = levenshtein_ratio(sorted_inter, t1) if sorted_inter else 0.0
    r2 = levenshtein_ratio(sorted_inter, t2) if sorted_inter else 0.0
    r3 = levenshtein_ratio(t1, t2)
    
    return max(r1, r2, r3)

def jaccard_ngram_similarity(s1: str, s2: str, n: int = 3) -> float:
    """Computes character n-gram Jaccard similarity index."""
    s1_clean = s1.replace(" ", "")
    s2_clean = s2.replace(" ", "")
    
    if not s1_clean or not s2_clean:
        return 0.0
        
    set1 = set(s1_clean[i:i+n] for i in range(max(1, len(s1_clean) - n + 1)))
    set2 = set(s2_clean[i:i+n] for i in range(max(1, len(s2_clean) - n + 1)))
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    if union == 0:
        return 0.0
    return (intersection / union) * 100.0
