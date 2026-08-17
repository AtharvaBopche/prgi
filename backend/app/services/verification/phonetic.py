from typing import List

def get_soundex(text: str) -> str:
    """
    Standard Soundex algorithm implementation in Python.
    Maps word to 4-character code e.g. N526.
    """
    if not text:
        return ""
    
    words = text.upper().split()
    codes = []
    
    for word in words:
        # Keep letters only
        word = ''.join(c for c in word if c.isalpha())
        if not word:
            continue
        
        first_letter = word[0]
        
        # Mapping table
        mapping = {
            'B': '1', 'F': '1', 'P': '1', 'V': '1',
            'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
            'D': '3', 'T': '3',
            'L': '4',
            'M': '5', 'N': '5',
            'R': '6'
        }
        
        coded = first_letter
        prev_code = mapping.get(first_letter, '0')
        
        for char in word[1:]:
            curr_code = mapping.get(char, '0')
            if curr_code != '0' and curr_code != prev_code:
                coded += curr_code
                prev_code = curr_code
            elif curr_code == '0':
                prev_code = '0'
                
        # Remove vowels/H/W except first char
        coded = coded.replace('0', '')
        # Pad with zeros or truncate to 4 chars
        coded = (coded + '0000')[:4]
        codes.append(coded)
        
    return "-".join(codes)

def get_metaphone(text: str) -> str:
    """
    Simplified Metaphone algorithm variant for phonetic comparison of titles.
    Converts English & Indian transliterated words to simplified phonetic keys.
    """
    if not text:
        return ""
    
    words = text.upper().split()
    keys = []
    
    for word in words:
        w = ''.join(c for c in word if c.isalpha())
        if not w:
            continue
        
        # Phonetic transformation rules for English/Indian transliterations
        w = w.replace("SCH", "SK")
        w = w.replace("CK", "K")
        w = w.replace("PH", "F")
        w = w.replace("TH", "T")
        w = w.replace("SH", "X")
        w = w.replace("CH", "X")
        w = w.replace("GH", "G")
        w = w.replace("GN", "N")
        w = w.replace("KN", "N")
        w = w.replace("WR", "R")
        w = w.replace("WH", "W")
        w = w.replace("QU", "K")
        w = w.replace("SC", "SK")
        w = w.replace("C", "K")
        w = w.replace("Z", "S")
        w = w.replace("V", "F")
        w = w.replace("W", "F")
        w = w.replace("Y", "")
        
        # Remove consecutive duplicate letters
        buf = []
        for ch in w:
            if not buf or buf[-1] != ch:
                buf.append(ch)
        
        res = "".join(buf)
        keys.append(res)
        
    return "-".join(keys)

def calculate_phonetic_similarity(text1: str, text2: str) -> float:
    """Calculates percentage phonetic similarity between two titles."""
    s1 = get_soundex(text1)
    s2 = get_soundex(text2)
    m1 = get_metaphone(text1)
    m2 = get_metaphone(text2)
    
    if s1 == s2 and m1 == m2:
        return 100.0
    
    score = 0.0
    if s1 == s2:
        score += 50.0
    if m1 == m2:
        score += 50.0
    elif m1 and m2:
        # Partial metaphone overlap
        k1_set = set(m1.split('-'))
        k2_set = set(m2.split('-'))
        overlap = len(k1_set.intersection(k2_set))
        total = max(len(k1_set), len(k2_set))
        if total > 0:
            score += 40.0 * (overlap / total)
            
    return min(100.0, score)
