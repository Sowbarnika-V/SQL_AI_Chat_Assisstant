import streamlit as st
import sqlite3
from llama_cpp import Llama
import base64

# Path to the JPEG image
jpeg_image_path = "OIP (1).jpg"

def jpeg_to_base64(jpeg_path):
    with open(jpeg_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

jpeg_base64 = jpeg_to_base64(jpeg_image_path)

# Setting up Background Image & Custom Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{jpeg_base64}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(0, 0, 0, 0.7); /* Dark overlay */
        background-blend-mode: darken; /* Blend mode to dim */
    }}
    .sql-results {{
        color: white;
        font-size: 16px;
        font-weight: bold;
    }}
    /* Change "Enter your query:" label text to white */
    label {{
        color: white !important;
        font-size: 18px;
        font-weight: bold;
    }}
    /* Make user input text black inside the text box */
    .stTextInput > div > div > input {{
        color: black !important;
        font-size: 16px;
        font-weight: bold;
    }}
    /* Style the process button */
    .query-button {{
        background-color: white !important;
        color: black !important;
        font-weight: bold;
        font-size: 14px;
        padding: 6px 12px;
        border-radius: 8px;
        cursor: pointer;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown("""
    <p style="font-size:40px; color:Aquamarine; text-align:center; font-weight:bold;">
         Ajackus SQL Chat Assistant 🗄️
    </p>
    """, unsafe_allow_html=True)

st.markdown("""
    <p style="text-align:center;color:Cornsilk;">
        Convert natural language queries into SQL effortlessly!  
    Let AI generate and execute SQL commands to fetch insights from your database in seconds.
    </p>
    """, unsafe_allow_html=True)

# Load Llama Model
@st.cache_resource
def load_model():
    model_path = "meta-llama-3-8b.Q4_K_M.gguf"  # Ensure correct model path
    return Llama(model_path=model_path)

llm = load_model()

# SQLite Connection
def get_db_connection():
    return sqlite3.connect("ajackus.db")

# Function to generate SQL from natural language
def generate_sql(query):
    schema = """
    Database schema:
    - Employees (ID, Name, Department, Salary, Hire_Date)
    - Departments (ID, Name, Manager)
    """
    prompt = f"""Translate this natural language query into SQL:
    
    {schema}

    Query: {query}

    SQL:"""
    response = llm(prompt, max_tokens=100, stop=["\n"])
    return response['choices'][0]['text'].strip()

# Execute SQL
def execute_sql(sql):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return f"Error: {e}"

# Streamlit Interface
st.markdown('<p style="color:white; font-size:18px; font-weight:bold;">Enter your query:</p>', unsafe_allow_html=True)

# User input box (query should be in black)
user_query = st.text_input("", key="query_input", placeholder="Provide your SQL Query here...")  # Black text inside input

# Button below input box
process_button = st.button("⚡ Process", key="process_btn")  # White button with emoji

if process_button and user_query:
    sql_query = generate_sql(user_query)
    st.write(f"Generated SQL: `{sql_query}`")

    results = execute_sql(sql_query)
    st.write("Results:")

    # Display results in white color
    st.markdown(f'<p class="sql-results">{results}</p>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: black;
        color: white;
        text-align: right;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        Design & Developed by Sowbarnika
    </div>
    """, unsafe_allow_html=True)
