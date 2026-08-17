import sqlite3
from pathlib import Path
from app.core.config import DB_PATH
from app.services.preprocessing.normalizer import normalize_title
from app.services.verification.phonetic import get_soundex

def get_db_connection():
    """Establishes and returns a SQLite connection with row factory enabled."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes SQLite database tables and FTS5 search indexes for all 21,500 titles."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Table 1: PRGI Registered Titles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prgi_titles (
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
    except Exception:
        pass
        
    conn.commit()
    conn.close()
