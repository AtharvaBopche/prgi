import unicodedata
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Comprehensive Unicode Mapping for Devanagari & Indian Scripts to Latin ASCII
DEVANAGARI_MAP = {
    'अ': 'A', 'आ': 'AA', 'इ': 'I', 'ई': 'EE', 'उ': 'U', 'ऊ': 'OO', 'ऋ': 'RI', 'ए': 'E', 'ऐ': 'AI', 'ओ': 'O', 'औ': 'AU',
    'क': 'K', 'ख': 'KH', 'ग': 'G', 'घ': 'GH', 'ङ': 'NG',
    'च': 'CH', 'छ': 'CHH', 'ज': 'J', 'झ': 'JH', 'ञ': 'NY',
    'ट': 'T', 'ठ': 'TH', 'ड': 'D', 'ढ': 'DH', 'ण': 'N',
    'त': 'T', 'थ': 'TH', 'द': 'D', 'ध': 'DH', 'न': 'N',
    'प': 'P', 'फ': 'PH', 'ब': 'B', 'भ': 'BH', 'म': 'M',
    'य': 'Y', 'र': 'R', 'ल': 'L', 'व': 'V', 'श': 'SH', 'ष': 'SH', 'स': 'S', 'ह': 'H',
    'ा': 'A', 'ि': 'I', 'ी': 'EE', 'ु': 'U', 'ू': 'OO', 'ृ': 'RI', 'े': 'E', 'ै': 'AI', 'ो': 'O', 'ौ': 'AU',
    '्': '', 'ं': 'N', 'ः': 'H', 'ँ': 'N', '़': ''
}

def transliterate_indic_to_latin(text: str) -> str:
    """Converts Indic scripts (Devanagari, etc.) into Latin phonetic ASCII tokens."""
    if not text:
        return ""
    
    res = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in DEVANAGARI_MAP:
            # Lookahead for implicit vowel 'A' if consonant followed by consonant (no virama)
            mapped = DEVANAGARI_MAP[char]
            res.append(mapped)
            
            # Check if consonant and next char is consonant or end of word (add implicit 'A')
            is_consonant = char in 'कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह'
            if is_consonant and i + 1 < len(text):
                next_char = text[i+1]
                # If next char is another consonant or space, insert implicit 'A'
                if next_char in 'कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह' or next_char == ' ':
                    res.append('A')
        else:
            res.append(char)
        i += 1
        
    return "".join(res)

test_inputs = ["नमस्कार", "दैनिक जागरण", "पंजाब केसरी", "प्रभात खबर", "नवभारत"]
for inp in test_inputs:
    print(f"{inp} -> {transliterate_indic_to_latin(inp)}")
