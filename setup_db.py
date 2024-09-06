import sqlite3

connection = sqlite3.connect('baza.db')  

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')

cursor.execute('''
INSERT INTO users (name, age, email) VALUES 
    ('Ana', 25, 'ana@gmail.com'),
    ('Boban', 30, 'boban@gmail.com'),
    ('Slavica', 22, 'slavica@gmail.com')
''')

connection.commit()

connection.close()

print("Database schema set up and initial data populated successfully.")
