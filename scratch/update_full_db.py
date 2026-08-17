import sqlite3
import time
from app.services.preprocessing.normalizer import normalize_title
from app.services.verification.phonetic import get_soundex

db_path = "backend/database/master_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Drop existing prgi_titles and rebuild with all 21,500 records
cursor.execute("DROP TABLE IF EXISTS prgi_titles;")
cursor.execute("DROP TABLE IF EXISTS titles_fts;")

cursor.execute("""
CREATE TABLE prgi_titles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sn INTEGER,
    title TEXT NOT NULL,
    normalized_title TEXT NOT NULL,
    soundex_code TEXT,
    language TEXT,
    reg_no TEXT,
    reg_date TEXT,
    periodicity TEXT,
    publisher TEXT,
    owner TEXT,
    state TEXT,
    district TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute('SELECT "SN.", Title, Language, "Registration Number", "Registration Date", Periodicity, Publisher, Owner, "Publication State", "Publication District" FROM my_table WHERE Title IS NOT NULL AND Title != ""')
rows = cursor.fetchall()
print(f"Total raw rows in my_table: {len(rows)}")

records = []
for row in rows:
    sn, raw_title, lang, reg_no, reg_date, per, pub, owner, state, dist = row
    title_str = str(raw_title).strip()
    norm = normalize_title(title_str)
    soundex = get_soundex(title_str)
    
    lang_str = str(lang).strip() if lang else "English"
    reg_no_str = str(reg_no).strip() if reg_no else "-"
    reg_date_str = str(reg_date).strip() if reg_date else "-"
    per_str = str(per).strip() if per else "Daily"
    pub_str = str(pub).strip() if pub else "-"
    owner_str = str(owner).strip() if owner else "-"
    state_str = str(state).strip() if state else "-"
    dist_str = str(dist).strip() if dist else "-"
    
    records.append((sn, title_str, norm, soundex, lang_str, reg_no_str, reg_date_str, per_str, pub_str, owner_str, state_str, dist_str))

cursor.executemany("""
    INSERT INTO prgi_titles (sn, title, normalized_title, soundex_code, language, reg_no, reg_date, periodicity, publisher, owner, state, district)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", records)

cursor.execute("CREATE INDEX IF NOT EXISTS idx_normalized_title ON prgi_titles (normalized_title);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_soundex_code ON prgi_titles (soundex_code);")

# Build FTS5
try:
    cursor.execute("""
    CREATE VIRTUAL TABLE titles_fts USING fts5(
        title,
        normalized_title,
        content='prgi_titles',
        content_rowid='id'
    );
    """)
    cursor.execute("INSERT INTO titles_fts(titles_fts) VALUES('rebuild');")
except Exception as e:
    print(f"FTS note: {e}")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM prgi_titles")
total = cursor.fetchone()[0]
print(f"Successfully populated prgi_titles with ALL {total} records!")

conn.close()
