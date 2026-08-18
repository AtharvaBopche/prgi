import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATABASE_DIR / "master_database.db"

DISALLOWED_WORDS_FILE = DATA_DIR / "disallowed_words.txt"
DISALLOWED_PREFIXES_FILE = DATA_DIR / "disallowed_prefixes.txt"
DISALLOWED_SUFFIXES_FILE = DATA_DIR / "disallowed_suffixes.txt"
PERIODICITY_WORDS_FILE = DATA_DIR / "periodicity_words.txt"
MULTILINGUAL_TERMS_FILE = DATA_DIR / "multilingual_terms.json"

SIMILARITY_REJECTION_THRESHOLD = 70.0  # Percentage similarity above which title is rejected/risky
HIGH_SIMILARITY_THRESHOLD = 80.0
CANDIDATE_SEARCH_LIMIT = 500  # Number of SQLite candidates to fetch for deep comparison
