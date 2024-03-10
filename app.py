import sqlite3

conn = sqlite3.connect('assessDB.db')
cursor = conn.cursor()

def display_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Available tables:")
    for table in tables:
        print(table[0])

def ask_question(table_name):
    cursor.execute(f"SELECT question, answer FROM {table_name}")
    questions = cursor.fetchall()
    
    for question, answer in questions:
        user_answer = input(f"Question: {question}\nYour answer: ").strip()
        if user_answer.lower() == answer.lower():
            print("\033[92mCorrect\033[0m\n")  # Green color for correct
        else:
            print("\033[91mIncorrect\033[0m\n")  # Red color for incorrect

def main():
    while True:
        display_tables()
        table_name = input("Choose a table (history, management, database, python, accounting): ").strip().lower()
        if table_name in ['history', 'management', 'database', 'python', 'accounting']:
            ask_question(table_name)
        else:
            print("Invalid table name. Please choose from the available tables.")
        
        choice = input("Do you want to choose another table? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()

# Close connection
conn.close()
