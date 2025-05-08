import os
from langchain_core.runnables import RunnableMap
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompts import get_sql_generation_prompt, get_sql_evaluation_prompt
from dotenv import load_dotenv

def load_google_api_key():
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY")

def create_sql_chain():
    google_api_key = load_google_api_key()

    LLM = ChatGoogleGenerativeAI(
        temperature=0.7, 
        model="gemini-2.0-flash", 
        max_output_tokens=5124, 
        google_api_key=google_api_key
    )
    
    sql_generation_prompt = get_sql_generation_prompt()
    sql_evaluation_prompt = get_sql_evaluation_prompt()

    generate_sql_chain = sql_generation_prompt | LLM
    combine_inputs = RunnableMap({
        "question": lambda x: x["question"],
        "sql_query": generate_sql_chain
    })
    
    evaluate_sql_chain = combine_inputs | sql_evaluation_prompt | LLM

    generate_and_evaluate_sql_chain = (
        RunnableMap({
            "question": lambda x: x["question"]
        }) |
        RunnableMap({
            "question": lambda x: x["question"],
            "sql_query": generate_sql_chain
        }) |
        (sql_evaluation_prompt | LLM)
    )

    return generate_and_evaluate_sql_chain
