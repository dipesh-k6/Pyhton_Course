import sqlite3

conn = sqlite3.connect("student_info.db")
cursor = conn.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS student_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        age INTEGER,
        subject VARCHAR(50),
        fee INTEGER
        )
    '''
)

conn.commit()
conn.close()