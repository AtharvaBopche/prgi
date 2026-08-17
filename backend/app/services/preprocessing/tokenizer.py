from typing import List

def tokenize(text: str) -> List[str]:
    """Tokenizes normalized text into word tokens."""
    if not text:
        return []
    return [token for token in text.split() if token]

def generate_ngram_tokens(text: str, n: int = 3) -> List[str]:
    """Generates character n-grams from text for sub-string matching."""
    text_compact = text.replace(" ", "")
    if len(text_compact) < n:
        return [text_compact]
    return [text_compact[i:i+n] for i in range(len(text_compact) - n + 1)]
