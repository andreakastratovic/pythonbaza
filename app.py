from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('baza.db')  
    conn.row_factory = sqlite3.Row 
    return conn

# Route to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()  # Fetch all users
    conn.close()
    return jsonify([dict(user) for user in users])  # Return data as JSON

# Route to fetch a single user by ID 
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
    conn.close()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(dict(user))

# Route to add a new user 
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()  # Gets new user data from the request
    name = new_user['name']
    age = new_user['age']
    email = new_user['email']

    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', (name, age, email))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User created successfully!'}), 201

# Route to update a user 
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    name = user_data['name']
    age = user_data['age']
    email = user_data['email']

    conn = get_db_connection()
    conn.execute('UPDATE users SET name = ?, age = ?, email = ? WHERE id = ?', (name, age, email, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User updated successfully!'})

# Route to delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'User deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)