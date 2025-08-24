import sqlite3

# Connect to SQLite database (it will create file if not exists)
db = sqlite3.connect("mydatabase.db")
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
""")

# Insert a user
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Python User",))
db.commit()

# Fetch all users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("✅ Users in database:")
for row in rows:
    print(row)

db.close()