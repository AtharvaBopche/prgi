from pathlib import Path
from typing import List, Tuple
from app.core.config import DISALLOWED_PREFIXES_FILE, DISALLOWED_SUFFIXES_FILE
from app.core.constants import ERR_DISALLOWED_PREFIX, ERR_DISALLOWED_SUFFIX
from app.services.preprocessing.normalizer import normalize_title

class PrefixSuffixChecker:
    def __init__(self):
        self.disallowed_prefixes = self._load_file(DISALLOWED_PREFIXES_FILE)
        self.disallowed_suffixes = self._load_file(DISALLOWED_SUFFIXES_FILE)

    def _load_file(self, path) -> list:
        items = []
        if Path(path).exists():
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    val = line.strip().upper()
                    if val:
                        items.append(val)
        return items

    def check(self, title: str, candidate_titles: list) -> List[Tuple[str, str, str]]:
        """
        Checks if adding/removing disallowed prefixes or suffixes causes
        the new title to closely resemble an existing title.
        """
        violations = []
        norm = normalize_title(title)
        tokens = norm.split()
        
        if not tokens:
            return violations

        first_word = tokens[0]
        last_word = tokens[-1]
        
        # Check prefix
        if first_word in self.disallowed_prefixes:
            stem = " ".join(tokens[1:])
            if stem and stem in candidate_titles:
                violations.append((
                    ERR_DISALLOWED_PREFIX,
                    f"Adding prefix '{first_word}' to existing title '{stem}' is not allowed",
                    f"Removing prefix '{first_word}' matches existing registered title '{stem}'."
                ))
                
        # Check suffix
        if last_word in self.disallowed_suffixes:
            stem = " ".join(tokens[:-1])
            if stem and stem in candidate_titles:
                violations.append((
                    ERR_DISALLOWED_SUFFIX,
                    f"Adding suffix '{last_word}' to existing title '{stem}' is not allowed",
                    f"Removing suffix '{last_word}' matches existing registered title '{stem}'."
                ))
                
        return violations

prefix_suffix_checker = PrefixSuffixChecker()
