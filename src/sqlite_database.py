import sqlite3

class SQLiteDatabase:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str, columns: dict):
        columns_with_types = ', '.join([f"{col} {typ}" for col, typ in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})")
        self.connection.commit()

    def insert(self, table_name: str, data: dict):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", tuple(data.values()))
        self.connection.commit()

    def fetch_all(self, table_name: str):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
