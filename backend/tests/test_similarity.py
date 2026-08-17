from app.services.verification.phonetic import calculate_phonetic_similarity, get_soundex
from app.services.verification.fuzzy import levenshtein_ratio, token_sort_ratio
from app.services.verification.similarity import compute_title_similarity

def test_phonetic_similarity():
    # Namaskar vs Namascar
    sim = calculate_phonetic_similarity("Namaskar", "Namascar")
    assert sim >= 80.0, f"Expected high phonetic similarity for Namaskar vs Namascar, got {sim}"

def test_fuzzy_similarity():
    ratio = levenshtein_ratio("HINDU", "INDIAN EXPRESS")
    assert ratio < 50.0

def test_compute_title_similarity():
    res = compute_title_similarity("Namaskar Samachar", "Namascar Samachar")
    assert res['similarity_percentage'] >= 75.0
    assert res['phonetic_match'] is True
