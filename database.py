import sqlite3
import json

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('/Users/samtiahmed/Desktop/VG2/Utvikling/python/sqlitePython/db/database.db')

cursor = conn.cursor()

# --------------------Create, Read------------------------

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
    #     ('Harry', 'Potter', 'harry@potter.com', 12345678),
    #     ('Hermione', 'Granger', 'hermione@granger.com', 87654321),
    #     ('Ron', 'Weasley', 'ron@weasley.com', 56781234)
    # ]
    # cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
    
# Fetch/query data
cursor.execute("SELECT * FROM users")
    # cursor.fetchone()
    # cursor.fetchall()
    # cursor.fetchmany(2)

print()
print(f"{'FULL NAME':<20} | {'EMAIL':<20} | {'NUMBER'}")
print("="*70)
for user in cursor.fetchall():
    full_name = f"{user[0]} {user[1]}"
    print(f"{full_name:<20} | {user[2]:<20} | {user[3]}")
print()

# ---------------------JSON Tricks-----------------------

data = cursor.fetchall()

# Convert the data to a list of dictionaries
data_dict = [{"first_name": f_name, "last_name": l_name, "email": email, "number": number} for f_name, l_name, email, number in data]

# Convert the list of dictionaries to a JSON-formatted string
json_data = json.dumps(data_dict)

# Write the JSON-formatted string to a file
with open('json-data.json', 'w') as file:
    json.dump(data_dict, file, indent=4)

# --------------------------------------------

conn.commit()
conn.close()