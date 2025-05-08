from langchain.prompts import PromptTemplate

def get_sql_generation_prompt():
    return PromptTemplate(
        input_variables=["question"],
        template="""
        You are an expert in converting English questions to SQL query! Given the {question}, you need to generate the SQL query for the database.
        The SQL database has the name Users and has the following columns - name, age, and location 
        SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
        the SQL command will be something like this SELECT COUNT(*) FROM Users ;
        \nExample 2 - Tell me all the Users located Amsterdam?, 
        the SQL command will be something like this SELECT * FROM Users WHERE location="Amsterdam" COLLATE NOCASE; 
        \nExample 3 - Tell me all the Users located Amsterdam and age is greater than 30?,
        the SQL command will be something like this SELECT * FROM Users WHERE location="Amsterdam" COLLATE NOCASE AND age>30 ; 
        also the sql code should not have ``` in beginning or end and sql word in output
        """
    )

def get_sql_evaluation_prompt():
    return PromptTemplate(
        input_variables=["question", "sql_query"],
        template="""
        You are an expert SQL database Engineer! Given the {question}, you need to check if the SQL query accurately retrieves the data from the database.
        You need to evaluate the SQL query and if the query doesn't accurately interpret the question, provide the SQL query that accurately retrieves the data from the database.

        Always return **only the final SQL query** on a single line — no explanation, no formatting, no markdown, and no backticks.
        
        SQL_Query: {sql_query}
        Check from an expert SQL database Engineer of the above question and SQL query.:
        """
    )
