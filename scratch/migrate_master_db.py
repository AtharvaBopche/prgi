import sqlite3
import time
from app.services.preprocessing.normalizer import normalize_title
from app.services.verification.phonetic import get_soundex

db_path = "backend/database/master_database.db"
print(f"Connecting to {db_path}...")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Create prgi_titles table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS prgi_titles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    normalized_title TEXT NOT NULL,
    soundex_code TEXT,
    language TEXT DEFAULT 'English',
    periodicity TEXT DEFAULT 'Daily',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Check existing count in prgi_titles
cursor.execute("SELECT COUNT(*) FROM prgi_titles")
prgi_count = cursor.fetchone()[0]

if prgi_count < 20000:
    print("Migrating titles from my_table into indexed prgi_titles table...")
    t0 = time.time()
    
    cursor.execute('SELECT "SN.", Title, Language, Periodicity FROM my_table WHERE Title IS NOT NULL AND Title != ""')
    rows = cursor.fetchall()
    print(f"Read {len(rows)} raw rows from my_table.")
    
    records = []
    seen = set()
    
    for row in rows:
        sn, raw_title, lang, per = row
        title_str = str(raw_title).strip()
        norm = normalize_title(title_str)
        
        if norm and norm not in seen:
            seen.add(norm)
            soundex = get_soundex(title_str)
            language_val = str(lang).strip() if lang else "English"
            periodicity_val = str(per).strip() if per else "Daily"
            records.append((title_str, norm, soundex, language_val, periodicity_val))
            
    print(f"Prepared {len(records)} unique normalized title records.")
    
    cursor.executemany("""
        INSERT INTO prgi_titles (title, normalized_title, soundex_code, language, periodicity)
        VALUES (?, ?, ?, ?, ?)
    """, records)
    
    conn.commit()
    t1 = time.time()
    print(f"Migration completed in {t1 - t0:.2f} seconds.")

# Create indexes
cursor.execute("CREATE INDEX IF NOT EXISTS idx_normalized_title ON prgi_titles (normalized_title);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_soundex_code ON prgi_titles (soundex_code);")

# Table 2: User Submissions
cursor.execute("""
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id TEXT NOT NULL UNIQUE,
    submitted_title TEXT NOT NULL,
    normalized_title TEXT NOT NULL,
    similarity_score REAL NOT NULL,
    verification_probability REAL NOT NULL,
    status TEXT NOT NULL,
    rejection_reasons TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_sub_norm_title ON submissions (normalized_title);")

# FTS5 Virtual Table
try:
    cursor.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS titles_fts USING fts5(
        title,
        normalized_title,
        content='prgi_titles',
        content_rowid='id'
    );
    """)
    cursor.execute("INSERT INTO titles_fts(titles_fts) VALUES('rebuild');")
    conn.commit()
    print("FTS5 virtual table built successfully.")
except Exception as e:
    print(f"FTS5 setup note: {e}")

cursor.execute("SELECT COUNT(*) FROM prgi_titles")
total = cursor.fetchone()[0]
print(f"Final master_database.db contains {total} indexed PRGI titles.")

conn.close()
