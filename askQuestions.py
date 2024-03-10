import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('assessDB.db')
cursor = conn.cursor()

# Function to display available tables
def display_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Available tables:")
    for table in tables:
        print(table[0])

# Function to ask questions based on the selected table
def ask_question(table_name):
    # Fetch questions and answers from the selected table
    cursor.execute(f"SELECT question, answer FROM {table_name}")
    questions = cursor.fetchall()
    
    # Loop through each question and ask the user
    for question, answer in questions:
        user_answer = input(f"Question: {question}\nYour answer: ").strip()
        if user_answer.lower() == answer.lower():
            print("\033[92mCorrect\033[0m\n")  # Green color for correct
        else:
            print("\033[91mIncorrect\033[0m\n")  # Red color for incorrect

# Main function
def main():
    while True:
        display_tables()
        table_name = input("Choose a table (history, management, database, python, accounting): ").strip().lower()
        if table_name in ['history', 'management', 'database', 'python', 'accounting']:
            ask_question(table_name)
        else:
            print("Invalid table name. Please choose from the available tables.")
        
        # Ask the user if they want to choose another table
        choice = input("Do you want to choose another table? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()

# Close connection
conn.close()
