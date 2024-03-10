import sqlite3

def display_table_data(database_file, table_name):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
        conn.close()

def main():
    database_file = 'assessDB.db'

    while True:
        table_name = input("Enter the name of the table you'd like to view "
                           "(history, management, database, python, accounting): ").lower()

        if table_name not in ['history', 'management', 'database', 'python', 'accounting']:
            print("Invalid table name. Please try again.")
            continue

        display_table_data(database_file, table_name)

        choice = input("Do you want to view another table? (yes/no): " ).lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
