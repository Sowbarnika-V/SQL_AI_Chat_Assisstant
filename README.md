# SQL Chat Assistant 🧠💬

A powerful AI-driven SQL Assistant using **FastAPI, SQLite, and Meta-Llama 3** to convert natural language queries into SQL.

---

## 🚀 **Project Overview**
This project allows users to enter **natural language queries**, and the **AI model (Llama 3)** translates them into **SQL queries**. The queries are then executed on an **SQLite database**.

- **Backend**: FastAPI  
- **Database**: SQLite (`ajackus.db`)  
- **AI Model**: Meta-Llama-3-8B (Local)  
- **Frontend**: Streamlit (For user interface)  
- **Deployment**: Railway (FastAPI) + Streamlit Cloud  

---

## 📂 **Project Structure**
📁 sql-chat-assistant/ │-- 📜 sql.py # SQLite DB setup & connection │-- 📜 code.py # FastAPI Backend (SQL query generation) │-- 📜 app.py # Streamlit Frontend (User Interface) │-- 📜 requirements.txt # Python dependencies │-- 📜 ajackus.db # SQLite database (Not uploaded to GitHub) │-- 📜 .gitignore # Ignores large files like Llama model │-- 📜 README.md # Project Documentation

## ** Install Dependencies**

pip install -r requirements.txt


## **Setup SQLite Database**

python sql.py

 
## **Start FastAPI Server**

uvicorn code:app --host 0.0.0.0 --port 8000

http://localhost:8000/docs


## **Run Streamlit App**
streamlit run app.py
