from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DATABASE_HOST', 'localhost'),
            database=os.getenv('DATABASE_NAME', 'myappdb'),
            user=os.getenv('DATABASE_USER', 'myappuser'),
            password=os.getenv('DATABASE_PASSWORD', 'mypassword')
        )
        return conn
    except Exception as e:
        app.logger.error(f"Error connecting to database: {e}")
        return None

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        app.logger.error(f"Error fetching users: {e}")
        return jsonify({'error': 'Failed to fetch users'}), 500

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    username = new_user['username']
    password = new_user['password']

    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Failed to connect to database'}), 500

    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'status': 'User added'}), 201
    except Exception as e:
        app.logger.error(f"Error adding user: {e}")
        return jsonify({'error': 'Failed to add user'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
