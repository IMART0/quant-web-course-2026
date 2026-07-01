import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON;")

# conn.execute("""
# CREATE TABLE users (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              username VARCHAR(50) NOT NULL UNIQUE,
#              first_name VARCHAR(50) NOT NULL,
#              last_name VARCHAR(50) NOT NULL,
#              role VARCHAR(50) NOT NULL CHECK (role IN ('student', 'teacher', 'guest'))
#              )
# """)

# cursor.execute("""
#     INSERT INTO users (username, first_name, last_name, role) VALUES ('karuchkar', 'Karim', 'Gizatullin', 'student')
# """)

cursor.execute("""
        CREATE TABLE events (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name VARCHAR(50) NOT NULL UNIQUE,
             user_id VARCHAR(50) FOREIGN KEY NOT NULL,
               )
""")

cursor.execute("INSERT INTO events (name, user_id) VALUES ('Спортивное отгрызание уголков парты', 1)")