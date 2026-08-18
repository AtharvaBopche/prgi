import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "database"

DATA_DIR.mkdir(parents=True, exist_ok=True)

# Set PRGI_DATABASE_DIR to a persistent-disk mount (for example /var/data on
# Render) to retain submissions across restarts and redeployments. On first
# start, the packaged title database is copied into that directory.
PERSISTENT_DATABASE_DIR = os.getenv("PRGI_DATABASE_DIR")
if PERSISTENT_DATABASE_DIR:
    runtime_database_dir = Path(PERSISTENT_DATABASE_DIR)
    runtime_database_dir.mkdir(parents=True, exist_ok=True)
    DB_PATH = runtime_database_dir / "master_database.db"
    bundled_database = DATABASE_DIR / "master_database.db"
    if not DB_PATH.exists() and bundled_database.exists():
        shutil.copy2(bundled_database, DB_PATH)
else:
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    DB_PATH = DATABASE_DIR / "master_database.db"

DISALLOWED_WORDS_FILE = DATA_DIR / "disallowed_words.txt"
DISALLOWED_PREFIXES_FILE = DATA_DIR / "disallowed_prefixes.txt"
DISALLOWED_SUFFIXES_FILE = DATA_DIR / "disallowed_suffixes.txt"
PERIODICITY_WORDS_FILE = DATA_DIR / "periodicity_words.txt"
MULTILINGUAL_TERMS_FILE = DATA_DIR / "multilingual_terms.json"

SIMILARITY_REJECTION_THRESHOLD = 70.0  # Percentage similarity above which title is rejected/risky
HIGH_SIMILARITY_THRESHOLD = 80.0
CANDIDATE_SEARCH_LIMIT = 500  # Number of SQLite candidates to fetch for deep comparison
