import sqlite3

conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('/Users/samtiahmed/Desktop/VG2/Utvikling/python/sqlitePython/db/database.db')

cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        number REAL
    )
""")

# Add data
cursor.execute("""
    INSERT INTO users VALUES
    ('Samuel', 'Camp', 'samuelCamp@gmail.com', 98987676)
""")

conn.commit()
conn.close()