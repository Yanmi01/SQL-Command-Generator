#  SQL Command Generator

This project allows users to ask questions in plain English and get answers directly from a local SQLite database using a Large Language Model (Gemini) to generate and validate SQL queries. It's built with:

- Gemini 2.0 flash via LangChain
- Python
- SQLite
- Streamlit (for the frontend)

---

## Features

- Converts natural language questions to SQL.
- Validates generated SQL for correctness.
- Queries a local SQLite database.
- Simple Streamlit-based web interface.

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Yanmi01/SQL-Command-Generator.git
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a .env file in the root with your Gemini API key:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Create the SQLite database
Run the database seeding script:
```bash
python sqlite.py
```

### 5. Run the Streamlit app
```bash
streamlit run app.py
```
