from flask import Flask, render_template
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres'),
        database=os.environ.get('DB_NAME', 'monitoring'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASSWORD', 'password')
    )
    return conn

@app.route('/')
def index():
    db_status = "Verbonden"
    try:
        conn = get_db_connection()
        conn.close()
    except Exception as e:
        db_status = f"Niet verbonden: {e}"

    return f"""
    <h1>The Knowledge Hub — Monitoring v4</h1>
    <p>Tijdstip: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p>Database status: {db_status}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
