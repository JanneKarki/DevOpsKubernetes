from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def initialize_database():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL
            );
        """)
        conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT task FROM todos;")
        todos = [row[0] for row in cur.fetchall()]
    conn.close()
    return jsonify(todos)

@app.route('/', methods=['POST'])
def create_todo():
    new_todo = request.json.get('todo')
    if new_todo:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO todos (task) VALUES (%s);", (new_todo,))
            conn.commit()
        conn.close()
        return jsonify({"message": "Todo added successfully"}), 201
    return jsonify({"error": "Invalid todo"}), 400

if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0', port=8080)
