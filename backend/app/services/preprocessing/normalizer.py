import re
import unicodedata

# Unicode character transliteration maps for Indic scripts (Devanagari, Gujarati, Gurmukhi, Bengali, Tamil, Telugu, Kannada, Malayalam)
INDIC_CHAR_MAP = {
    # Devanagari (Hindi, Marathi, Sanskrit)
    'अ': 'A', 'आ': 'AA', 'इ': 'I', 'ई': 'EE', 'उ': 'U', 'ऊ': 'OO', 'ऋ': 'RI', 'ए': 'E', 'ऐ': 'AI', 'ओ': 'O', 'औ': 'AU',
    'क': 'K', 'ख': 'KH', 'ग': 'G', 'घ': 'GH', 'ङ': 'NG',
    'च': 'CH', 'छ': 'CHH', 'ज': 'J', 'झ': 'JH', 'ञ': 'NY',
    'ट': 'T', 'ठ': 'TH', 'ड': 'D', 'ढ': 'DH', 'ण': 'N',
    'त': 'T', 'थ': 'TH', 'द': 'D', 'ध': 'DH', 'न': 'N',
    'प': 'P', 'फ': 'PH', 'ब': 'B', 'भ': 'BH', 'म': 'M',
    'य': 'Y', 'र': 'R', 'ल': 'L', 'व': 'V', 'श': 'SH', 'ष': 'SH', 'स': 'S', 'ह': 'H',
    'ा': 'A', 'ि': 'I', 'ी': 'EE', 'ु': 'U', 'ू': 'OO', 'ृ': 'RI', 'े': 'E', 'ै': 'AI', 'ो': 'O', 'ौ': 'AU',
    '्': '', 'ं': 'N', 'ः': 'H', 'ँ': 'N', '़': '',
    
    # Gujarati
    'અ': 'A', 'આ': 'AA', 'ઇ': 'I', 'ઈ': 'EE', 'ઉ': 'U', 'ઊ': 'OO', 'એ': 'E', 'ઐ': 'AI', 'ઓ': 'O', 'ઔ': 'AU',
    'ક': 'K', 'ખ': 'KH', 'ગ': 'G', 'ઘ': 'GH', 'ચ': 'CH', 'છ': 'CHH', 'જ': 'J', 'ઝ': 'JH',
    'ટ': 'T', 'ઠ': 'TH', 'ડ': 'D', 'ઢ': 'DH', 'ણ': 'N', 'ત': 'T', 'થ': 'TH', 'દ': 'D', 'ધ': 'DH', 'ન': 'N',
    'પ': 'P', 'ફ': 'PH', 'બ': 'B', 'ભ': 'BH', 'મ': 'M', 'ય': 'Y', 'ર': 'R', 'લ': 'L', 'વ': 'V', 'શ': 'SH', 'ષ': 'SH', 'સ': 'S', 'હ': 'H',
    'ા': 'A', 'િ': 'I', 'ી': 'EE', 'ુ': 'U', 'ૂ': 'OO', 'ે': 'E', 'ૈ': 'AI', 'ો': 'O', 'ૌ': 'AU', '્': '', 'ં': 'N',
    
    # Gurmukhi (Punjabi)
    'ਅ': 'A', 'ਆ': 'AA', 'ਇ': 'I', 'ਈ': 'EE', 'ਉ': 'U', 'ਊ': 'OO', 'ਏ': 'E', 'ਐ': 'AI', 'ਓ': 'O', 'ਔ': 'AU',
    'ਕ': 'K', 'ਖ': 'KH', 'ਗ': 'G', 'ਘ': 'GH', 'ਚ': 'CH', 'ਛ': 'CHH', 'ਜ': 'J', 'ਝ': 'JH',
    'ਟ': 'T', 'ਠ': 'TH', 'ਡ': 'D', 'ਢ': 'DH', 'ਣ': 'N', 'ਤ': 'T', 'ਥ': 'TH', 'ਦ': 'D', 'ਧ': 'DH', 'ਨ': 'N',
    'ਪ': 'P', 'ਫ': 'PH', 'ਬ': 'B', 'ਭ': 'BH', 'ਮ': 'M', 'ਯ': 'Y', 'ਰ': 'R', 'ਲ': 'L', 'ਵ': 'V', 'ਸ਼': 'SH', 'ਸ': 'S', 'ਹ': 'H',
    'ਾ': 'A', 'ਿ': 'I', 'ੀ': 'EE', 'ੁ': 'U', 'ੂ': 'OO', 'ੇ': 'E', 'ੈ': 'AI', 'ੋ': 'O', 'ੌ': 'AU', '੍': '', 'ਂ': 'N',
    
    # Bengali
    'অ': 'A', 'আ': 'AA', 'ই': 'I', 'ঈ': 'EE', 'উ': 'U', 'ঊ': 'OO', 'এ': 'E', 'ঐ': 'AI', 'ও': 'O', 'ঔ': 'AU',
    'ক': 'K', 'খ': 'KH', 'গ': 'G', 'ঘ': 'GH', 'চ': 'CH', 'ছ': 'CHH', 'জ': 'J', 'ঝ': 'JH',
    'ট': 'T', 'ঠ': 'TH', 'ড': 'D', 'ঢ': 'DH', 'ণ': 'N', 'ত': 'T', 'থ': 'TH', 'দ': 'D', 'ধ': 'DH', 'ন': 'N',
    'প': 'P', 'ফ': 'PH', 'ব': 'B', 'ভ': 'BH', 'ম': 'M', 'য': 'Y', 'র': 'R', 'ল': 'L', 'শ': 'SH', 'ষ': 'SH', 'স': 'S', 'হ': 'H',
    'া': 'A', 'ি': 'I', 'ী': 'EE', 'ু': 'U', 'ূ': 'OO', 'ে': 'E', 'ৈ': 'AI', 'ো': 'O', 'ৌ': 'AU', '্': '', 'ং': 'N'
}

CONSONANTS_SET = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहકખગઘચછજઝટઠડઢણતથદધનપફબભમયરલવશષસહਕਖਗਘਚਛਜਝਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵਸ਼ਸਹকখগঘচছজঝটঠডঢণতথদধনপফবভমযরলশষসহ")

def transliterate_indic_to_latin(title: str) -> str:
    """Converts Indic scripts into phonetic Latin ASCII string."""
    if not title:
        return ""
        
    res = []
    for i, char in enumerate(title):
        if char in INDIC_CHAR_MAP:
            mapped = INDIC_CHAR_MAP[char]
            res.append(mapped)
            
            # Implicit vowel 'A' handling for consonants
            if char in CONSONANTS_SET and i + 1 < len(title):
                next_char = title[i+1]
                if next_char in CONSONANTS_SET or next_char == ' ':
                    res.append('A')
        else:
            res.append(char)
            
    return "".join(res)

def normalize_title(title: str) -> str:
    """
    Normalizes a title string:
    - Transliterates Indic scripts (Devanagari, Gujarati, Bengali, Gurmukhi) to Latin ASCII phonetics
    - Converts to uppercase
    - Removes non-alphanumeric special symbols
    - Normalizes multiple spaces into single space
    """
    if not title:
        return ""
    
    # 1. Transliterate non-ASCII Indic scripts to Latin ASCII phonetics
    text = transliterate_indic_to_latin(title)
    
    # 2. Unicode NFKD normalization & ASCII fallback
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ASCII', 'ignore').decode('utf-8')
    
    # 3. Uppercase canonical standard
    text = text.upper()
    
    # 4. Remove punctuation & symbols keeping alphanumerics & spaces
    text = re.sub(r'[^A-Z0-9\s]', '', text)
    
    # 5. Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def remove_common_stop_words(normalized_title: str, stop_words: set) -> str:
    tokens = normalized_title.split()
    filtered = [t for t in tokens if t not in stop_words]
    return " ".join(filtered)
