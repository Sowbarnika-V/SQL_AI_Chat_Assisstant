# 🧠 SQL Chat Assistant  

An **AI-powered SQL Assistant** that translates **natural language queries** into **SQL commands** and executes them on an **SQLite database**.  

## 🚀 Project Overview  

This project uses **Meta-Llama-3-8B.Q4_K_M** to process user queries and generate SQL statements. The application is built using **Streamlit** for an interactive user interface.  

### **Key Features**  
✅ Accepts **natural language queries** and generates **SQL**  
✅ Executes queries on **SQLite database (`ajackus.db`)**  
✅ Interactive UI built with **Streamlit**  
✅ Uses **Meta-Llama-3-8B.Q4_K_M** for AI-driven SQL generation  

---

## 📂 Project Structure  

📁 SQL-Chat-Assistant 
│── 📜 README.md # Project Documentation 
│── 📜 requirements.txt # Required Dependencies
│── 📜 sql.py # SQLite DB Connection & Implementation 
│── 📜 code.py # Streamlit UI + AI Model Integration 
│── 📜 ajackus.db # SQLite Database File 

## 📂 Place Model File
The Meta-Llama-3-8B.Q4_K_M.gguf file is required but not included due to its large size.

Download it separately and place it in the project directory.

## 📂 Run the Application

streamlit run code.py

## 📂 Working
1️⃣ User enters a natural language query
2️⃣ Meta-Llama-3-8B generates the corresponding SQL command
3️⃣ The SQL query is executed on ajackus.db (SQLite database)
4️⃣ Results are displayed in the Streamlit interface

## 📂 Files & Their Roles

1️⃣ sql.py: 

Handles SQLite database connection
Executes SQL queries on ajackus.db

2️⃣ code.py

Implements Streamlit UI
Loads Meta-Llama-3-8B.Q4_K_M model
Converts natural language queries into SQL
Executes SQL queries on the SQLite database

3️⃣ ajackus.db

SQLite database containing structured tables & data
Used to execute SQL queries


