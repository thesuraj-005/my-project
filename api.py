import sqlite3

DB_PATH = "db1.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Ensure table exists
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS emp(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        mob VARCHAR(50),
        city VARCHAR(50)
    )
    """
)

# Delete record safely (won't crash if table is empty)
cur.execute("DELETE FROM emp WHERE id = ?", (1,))

conn.commit()
conn.close()

print("Done. Deleted emp where id=1 (if it existed).")

