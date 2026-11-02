import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS MEMBER(
Member_ID INTEGER PRIMARY KEY,
Member_Name TEXT,
Email TEXT,
Phone_No TEXT,
Address TEXT,
Join_Date TEXT
)
""")

conn.commit()
conn.close()