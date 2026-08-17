from pathlib import Path
from typing import List, Tuple
from app.core.config import DISALLOWED_WORDS_FILE
from app.core.constants import ERR_DISALLOWED_WORD
from app.services.preprocessing.normalizer import normalize_title

class ProhibitedWordsChecker:
    def __init__(self):
        self.prohibited_words = self._load_words()

    def _load_words(self) -> set:
        words = set()
        if Path(DISALLOWED_WORDS_FILE).exists():
            with open(DISALLOWED_WORDS_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip().upper()
                    if word:
                        words.add(word)
        return words

    def check(self, title: str) -> List[Tuple[str, str, str]]:
        """Checks if title contains prohibited words."""
        violations = []
        norm = normalize_title(title)
        tokens = set(norm.split())
        
        # Word token check
        found = tokens.intersection(self.prohibited_words)
        
        # Multi-word phrase check (e.g. "PRESS COUNCIL", "HIGH COURT")
        for phrase in self.prohibited_words:
            if " " in phrase and phrase in norm:
                found.add(phrase)
                
        for match in found:
            violations.append((
                ERR_DISALLOWED_WORD,
                f"Title contains prohibited term '{match}'",
                f"The word/phrase '{match}' is restricted under PRGI publishing guidelines."
            ))
            
        return violations

prohibited_checker = ProhibitedWordsChecker()
