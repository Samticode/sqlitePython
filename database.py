import sqlite3

conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('/Users/samtiahmed/Desktop/VG2/Utvikling/python/sqlitePython/db/database.db')

cursor = conn.cursor()

# --------------------------------------------

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        number REAL
    )
""")

# Add one row/entry of data
    # cursor.execute("""
    #     INSERT INTO users VALUES
    #     ('Samuel', 'Camp', 'samuelCamp@gmail.com', 98987676)
    # """)

# Add multiple rows/entries of data
    # users = [
    #     ('Donald', 'Duck', 'Donald@duck.com', 12345678),
    #     ('Mickey', 'Mouse', 'Mickey@mouse.com', 87654321),
    #     ('Goofy', 'Goof', 'Goofy@goof.com', 56781234)
    # ]
    # cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
    
# Fetch/query data
cursor.execute("SELECT * FROM users")
# cursor.fetchone()
# cursor.fetchall()
# cursor.fetchmany(2)

for user in cursor.fetchall():
    print(user)

# --------------------------------------------

conn.commit()
conn.close()