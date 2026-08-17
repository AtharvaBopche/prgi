import sqlite3
from app.database.connection import init_db, get_db_connection
from app.services.preprocessing.normalizer import normalize_title
from app.services.verification.phonetic import get_soundex

SEED_TITLES = [
    # Famous National & Regional Newspapers
    ("The Hindu", "English", "Daily"),
    ("Indian Express", "English", "Daily"),
    ("Times of India", "English", "Daily"),
    ("Hindustan Times", "English", "Daily"),
    ("Mumbai Samachar", "Gujarati", "Daily"),
    ("Namaskar", "Hindi", "Monthly"),
    ("Dainik Jagran", "Hindi", "Daily"),
    ("Dainik Bhaskar", "Hindi", "Daily"),
    ("Amar Ujala", "Hindi", "Daily"),
    ("Punjab Kesari", "Hindi", "Daily"),
    ("Navbharat Times", "Hindi", "Daily"),
    ("Prabhat Khabar", "Hindi", "Daily"),
    ("Rajasthan Patrika", "Hindi", "Daily"),
    ("Malayala Manorama", "Malayalam", "Daily"),
    ("Mathrubhumi", "Malayalam", "Daily"),
    ("Deshabhimani", "Malayalam", "Daily"),
    ("Lokmat", "Marathi", "Daily"),
    ("Sakal", "Marathi", "Daily"),
    ("Saamna", "Marathi", "Daily"),
    ("Pudhari", "Marathi", "Daily"),
    ("Anandabazar Patrika", "Bengali", "Daily"),
    ("Bartaman", "Bengali", "Daily"),
    ("Sangbad Pratidin", "Bengali", "Daily"),
    ("Ei Samay", "Bengali", "Daily"),
    ("Dina Thanthi", "Tamil", "Daily"),
    ("Dinamalar", "Tamil", "Daily"),
    ("Dinakaran", "Tamil", "Daily"),
    ("Eenadu", "Telugu", "Daily"),
    ("Sakshi", "Telugu", "Daily"),
    ("Andhra Jyothi", "Telugu", "Daily"),
    ("Deccan Chronicle", "English", "Daily"),
    ("Deccan Herald", "English", "Daily"),
    ("The Telegraph", "English", "Daily"),
    ("Financial Express", "English", "Daily"),
    ("Economic Times", "English", "Daily"),
    ("Business Standard", "English", "Daily"),
    ("The Tribune", "English", "Daily"),
    ("The Pioneer", "English", "Daily"),
    ("Free Press Journal", "English", "Daily"),
    ("Daily Evening", "English", "Daily"),
    ("ABC News", "English", "Daily"),
    ("Vanguard Herald", "English", "Weekly"),
    ("National Voice", "English", "Daily"),
    ("Sun Observer", "English", "Monthly"),
    ("Star Standard", "English", "Weekly"),
    ("Citizen Echo", "English", "Daily"),
    ("Bharat Samachar", "Hindi", "Daily"),
    ("Rastra Vani", "Hindi", "Daily"),
    ("Navbharat", "Hindi", "Daily"),
    ("Jan Satta", "Hindi", "Daily"),
]

# Generate synthetic variations to reach thousands of realistic PRGI database titles
CITIES = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Lucknow", "Patna", "Bhopal", "Chandigarh", "Guwahati", "Ranchi", "Indore", "Nagpur", "Surat", "Varanasi", "Agra"]
TOPICS = ["Business", "Financial", "Sports", "Cinema", "Science", "Technology", "Health", "Youth", "Agriculture", "Auto", "Real Estate", "Education", "World", "Metro", "Capital", "Coast", "Valley", "Frontier", "Heritage"]
SUFFIXES = ["Chronicle", "Gazette", "Times", "Express", "Patrika", "Samachar", "Herald", "Post", "Tribune", "Reporter", "Mirror", "Observer", "Journal", "Voice", "Echo", "Standard", "Dispatch", "Review"]

def seed_database():
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check current count
    cursor.execute("SELECT COUNT(*) FROM prgi_titles")
    count = cursor.fetchone()[0]
    
    if count >= 1000:
        print(f"Database already seeded with {count} titles.")
        conn.close()
        return

    records = []
    seen = set()

    for title, lang, per in SEED_TITLES:
        norm = normalize_title(title)
        if norm not in seen:
            seen.add(norm)
            soundex = get_soundex(title)
            records.append((title, norm, soundex, lang, per))

    # Generate synthetic titles for scale
    for city in CITIES:
        for suffix in SUFFIXES:
            t = f"{city} {suffix}"
            norm = normalize_title(t)
            if norm not in seen:
                seen.add(norm)
                soundex = get_soundex(t)
                records.append((t, norm, soundex, "English", "Daily"))

    for topic in TOPICS:
        for suffix in SUFFIXES:
            t = f"{topic} {suffix}"
            norm = normalize_title(t)
            if norm not in seen:
                seen.add(norm)
                soundex = get_soundex(t)
                records.append((t, norm, soundex, "English", "Daily"))

    cursor.executemany("""
        INSERT OR IGNORE INTO prgi_titles (title, normalized_title, soundex_code, language, periodicity)
        VALUES (?, ?, ?, ?, ?)
    """, records)

    # Populate FTS index
    try:
        cursor.execute("INSERT INTO titles_fts(titles_fts) VALUES('rebuild');")
    except Exception:
        pass

    conn.commit()
    conn.close()
    print(f"Successfully seeded database with {len(records)} PRGI titles.")

if __name__ == "__main__":
    seed_database()
