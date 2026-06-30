import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        role VARCHAR(50) NOT NULL CHECK (role IN ('student', 'teacher', 'guest'))
    )
    """)

cursor.execute("""
    INSERT INTO users (username, first_name, last_name, role) VALUES ('imart', 'Ishkhan', 'Martirosyan', 'teacher')
""")

cursor.execute("""
    INSERT INTO users (username, first_name, last_name, role) VALUES ('rash', 'Raushan', 'Hanipov', 'teacher')
""")

cursor.execute("""  
    SELECT * FROM users
""")

for row in cursor.fetchall():
    print(row)