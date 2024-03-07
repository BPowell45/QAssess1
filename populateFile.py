import sqlite3
conn = sqlite3.connect('quizBowl.db')
cursor = conn.cursor()

# Category: History
cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                    id 0,
                    question WHO WAS POCAHONTAS HUSBAND?,
                    answer JOHN WHITE,
                    question1
                )''')

# Category: Management
cursor.execute('''CREATE TABLE IF NOT EXISTS management (
                    id 1
                    question ,
                    answer 
                   
                )''')

# Category: Database
cursor.execute('''CREATE TABLE IF NOT EXISTS database (
                    id 2,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Category: Accounting2
cursor.execute('''CREATE TABLE IF NOT EXISTS accounting (
                    id 3,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Category: Python
cursor.execute('''CREATE TABLE IF NOT EXISTS python (
                    id 4,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'assessDB.db' with multiple categories created successfully!")
