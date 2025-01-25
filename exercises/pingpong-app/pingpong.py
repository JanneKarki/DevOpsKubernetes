from flask import Flask
import os
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print(connection)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise

def initialize_database():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS counter (
                id SERIAL PRIMARY KEY,
                count INTEGER NOT NULL DEFAULT 0
            );
        """)
        conn.commit()
    conn.close()


@app.route('/', methods=['GET'])
def home():
    return "Pingpong is running", 200

@app.route('/pingpong', methods=['GET'])
def ping_pong():
    conn = get_db_connection()

    with conn.cursor() as cur:
        cur.execute("SELECT count FROM counter WHERE id = 1;")
        result = cur.fetchone()
        print(result, "result")
        
        if result is None:
            current_count = 0
            cur.execute("INSERT INTO counter (id, count) VALUES (1, %s);", (current_count,))
        else:
            current_count = result[0]
        
        current_count += 1
        cur.execute("UPDATE counter SET count = %s WHERE id = 1;", (current_count,))
        conn.commit()
    conn.close()
    if result:
        return str(result[0])
    return  200

if __name__ == '__main__':
    initialize_database()
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
