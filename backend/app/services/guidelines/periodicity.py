from pathlib import Path
from typing import List, Tuple
from app.core.config import PERIODICITY_WORDS_FILE
from app.core.constants import ERR_PERIODICITY_MODIFICATION
from app.services.preprocessing.normalizer import normalize_title

class PeriodicityChecker:
    def __init__(self):
        self.periodicity_words = self._load_words()

    def _load_words(self) -> set:
        words = set()
        if Path(PERIODICITY_WORDS_FILE).exists():
            with open(PERIODICITY_WORDS_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    w = line.strip().upper()
                    if w:
                        words.add(w)
        return words

    def check(self, title: str, candidate_titles: list) -> List[Tuple[str, str, str]]:
        """
        Checks if removing periodicity terms from the submitted title matches an existing registered title.
        """
        violations = []
        norm = normalize_title(title)
        tokens = norm.split()
        
        # Check if title contains any periodicity term
        periodicity_found = [t for t in tokens if t in self.periodicity_words]
        
        if not periodicity_found:
            return violations
            
        # Strip all periodicity words from title
        stripped_tokens = [t for t in tokens if t not in self.periodicity_words]
        stripped_title = " ".join(stripped_tokens)
        
        if stripped_title and stripped_title in candidate_titles:
            violations.append((
                ERR_PERIODICITY_MODIFICATION,
                f"Adding periodicity modifier ({', '.join(periodicity_found)}) to existing title '{stripped_title}' is prohibited.",
                f"Removing periodicity terms yields '{stripped_title}' which is an existing registered title."
            ))
            
        return violations

periodicity_checker = PeriodicityChecker()
