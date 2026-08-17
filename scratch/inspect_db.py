import sqlite3

db_path = "backend/database/master_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [t[0] for t in cursor.fetchall()]
print(f"Tables in master_database.db: {tables}\n")

for table in tables:
    print(f"--- Table: {table} ---")
    cursor.execute(f"PRAGMA table_info('{table}');")
    cols = cursor.fetchall()
    for col in cols:
        print(f"  Col #{col[0]}: {col[1]} ({col[2]})")
    
    cursor.execute(f"SELECT COUNT(*) FROM '{table}';")
    count = cursor.fetchone()[0]
    print(f"  Total Rows: {count}")
    
    cursor.execute(f"SELECT * FROM '{table}' LIMIT 5;")
    rows = cursor.fetchall()
    print("  Sample Rows:")
    for r in rows:
        print(f"    {r}")
    print()

conn.close()
