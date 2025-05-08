# # app.py
# import streamlit as st
# from src.sql_chain import create_sql_chain
# from src.sqlite_database import SQLiteDatabase
# import re
# import os
# from dotenv import load_dotenv

# def load_google_api_key():
#     load_dotenv()
#     return os.getenv("GOOGLE_API_KEY")

# def extract_sql(text):
#     match = re.search(r"SELECT .*?;", text, re.IGNORECASE | re.DOTALL)
#     return match.group(0).strip() if match else ""

# def app():
#     # Load Google API key
#     google_api_key = load_google_api_key()

#     # Create the SQL chain
#     generate_and_evaluate_sql_chain = create_sql_chain()

#     # Streamlit UI
#     st.title("Text-to-SQL Query Generator")
#     question = st.text_input("Enter your question:", "")

#     if st.button("Generate SQL"):
#         if question:
#             # Generate and evaluate SQL query
#             chain_output = generate_and_evaluate_sql_chain.invoke({"question": question}).content.strip()

#             # Extract the final SQL query
#             final_sql_query = extract_sql(chain_output)

#             # Display the generated SQL query
#             st.write("Generated SQL Query:", final_sql_query)

#             # Execute SQL query on SQLite database
#             try:
#                 db = SQLiteDatabase("Users.db")
#                 result = db.cursor.execute(final_sql_query).fetchall()
#                 db.close()
#             except Exception as e:
#                 st.error(f"Error executing query: {e}")
#                 result = []

#             # Show results
#             if result:
#                 st.write("Query Result:")
#                 st.write(result)
#             else:
#                 st.write("No results found.")
#         else:
#             st.write("Please enter a valid question.")

# if __name__ == "__main__":
#     app()


import streamlit as st
from src.sql_chain import create_sql_chain
from src.sqlite_database import SQLiteDatabase
import re
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

def extract_sql(text: str) -> str:
    match = re.search(r"(SELECT|INSERT|UPDATE|DELETE).*?;", text, re.IGNORECASE | re.DOTALL)
    return match.group(0).strip() if match else ""

def format_result(result):
    # Handles clean rendering of result
    if not result:
        st.warning("No results found.")
    else:
        # If only 1 column (like a list of names)
        if all(len(row) == 1 for row in result):
            st.subheader("Query Result:")
            for row in result:
                st.write(f"- {row[0]}")
        else:
            df = pd.DataFrame(result)
            st.dataframe(df)

st.set_page_config(page_title="Natural Language SQL Query App")
st.title("Ask Questions About Your SQL Database")

user_question = st.text_input("Enter your question:", "")

if st.button("Submit") and user_question.strip():
    # Step 1: Generate & evaluate SQL
    generate_and_evaluate_sql_chain = create_sql_chain()
    response = generate_and_evaluate_sql_chain.invoke({"question": user_question}).content.strip()

    st.markdown("**Generated SQL Query:**")
    sql_query = extract_sql(response)
    st.code(sql_query or "No valid SQL query found.")

    # Step 2: Execute SQL
    if sql_query:
        try:
            db = SQLiteDatabase("Users.db")
            result = db.cursor.execute(sql_query).fetchall()
            db.close()

            format_result(result)
        except Exception as e:
            st.error(f"SQL execution error: {e}")
