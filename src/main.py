# src/main.py
from src.sql_chain import create_sql_chain
from src.sqlite_database import SQLiteDatabase
import re

def extract_sql(text):
    # Extract the first valid SQL command from the evaluated response
    match = re.search(r"SELECT .*?;", text, re.IGNORECASE | re.DOTALL)
    return match.group(0).strip() if match else ""

def main():
    generate_and_evaluate_sql_chain = create_sql_chain()

    question = "What are the names of users older than 30?"
    
    # Step 1: Generate and evaluate SQL query
    chain_output = generate_and_evaluate_sql_chain.invoke({"question": question}).content.strip()

    # Step 2: Extract the final SQL query
    final_sql_query = extract_sql(chain_output)

    # Step 3: Execute the SQL query
    try:
        db = SQLiteDatabase("Users.db")
        result = db.cursor.execute(final_sql_query).fetchall()
    except sqlite3.Error as e:
        print(f"SQL execution error: {e}")
        result = []
    finally:
        db.close()

    # Step 4: Display results
    print("Query Result:", result)

if __name__ == "__main__":
    main()
