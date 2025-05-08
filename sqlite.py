import sqlite3
from src.sqlite_database import SQLiteDatabase

DB_NAME = "Users.db"

def setup_users_table(reset=False):
    db = SQLiteDatabase(DB_NAME)

    if reset:
        db.cursor.execute("DROP TABLE IF EXISTS users")

    db.create_table('users', {
        'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT',
        'age': 'INTEGER',
        'location': 'TEXT'
    })

    sample_data = [
        {'name': 'John Doe', 'age': 28, 'location': 'New York'},
        {'name': 'Jane Smith', 'age': 32, 'location': 'San Francisco'},
        {'name': 'Alice', 'age': 30, 'location': 'Los Angeles'},
        {'name': 'Bob', 'age': 25, 'location': 'Chicago'},
        {'name': 'Charlie', 'age': 35, 'location': 'Seattle'},
        {'name': 'Charlie', 'age': 35, 'location': 'Seattle'},
        {'name': 'Charlie', 'age': 35, 'location': 'Seattle'},
        {'name': 'David', 'age': 28, 'location': 'Boston'},
        {'name': 'Eve', 'age': 22, 'location': 'Austin'},
        {'name': 'Eve', 'age': 22, 'location': 'Austin'},
        {'name': 'Frank', 'age': 29, 'location': 'Denver'}
    ]

    for row in sample_data:
        db.insert('users', row)

    all_users = db.fetch_all('users')
    print("All Users in DB:")
    for user in all_users:
        print(user)

    db.close()

if __name__ == "__main__":
    setup_users_table(reset=True)  # change to False to retain existing table


