import json
from pathlib import Path
from app.core.config import MULTILINGUAL_TERMS_FILE
from app.services.preprocessing.normalizer import normalize_title

class SemanticMatcher:
    def __init__(self):
        self.multilingual_dict = self._load_dictionary()
        # Build reverse lookup map
        self.term_to_canonical = {}
        for canonical, translations in self.multilingual_dict.items():
            self.term_to_canonical[canonical.upper()] = canonical.upper()
            for tr in translations:
                self.term_to_canonical[tr.upper()] = canonical.upper()

    def _load_dictionary(self):
        if Path(MULTILINGUAL_TERMS_FILE).exists():
            try:
                with open(MULTILINGUAL_TERMS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def get_canonical_representation(self, title: str) -> str:
        """Translates known multilingual publishing terms to their canonical English concept."""
        normalized = normalize_title(title)
        tokens = normalized.split()
        canonical_tokens = []
        
        for token in tokens:
            if token in self.term_to_canonical:
                canonical_tokens.append(self.term_to_canonical[token])
            else:
                canonical_tokens.append(token)
                
        return " ".join(canonical_tokens)

    def calculate_semantic_similarity(self, title1: str, title2: str) -> float:
        """Calculates semantic similarity based on concept mapping."""
        c1 = self.get_canonical_representation(title1)
        c2 = self.get_canonical_representation(title2)
        
        if c1 == c2:
            return 100.0
            
        t1_set = set(c1.split())
        t2_set = set(c2.split())
        
        if not t1_set or not t2_set:
            return 0.0
            
        intersection = len(t1_set.intersection(t2_set))
        union = len(t1_set.union(t2_set))
        
        return (intersection / union) * 100.0

semantic_service = SemanticMatcher()
