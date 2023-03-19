# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
# Generate a Fernet encryption key or use an existing one
key = os.environ.get('FERNET_KEY')
if not key:
    key = Fernet.generate_key()
    os.environ['FERNET_KEY'] = key.decode('utf-8')
cipher_suite = Fernet(key)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False, default='Personal')

@app.route('/api/passwords', methods=['GET', 'POST'])
def passwords():
    if request.method == 'GET':
        passwords = Password.query.all()
        decrypted_passwords = []
        for p in passwords:
            try:
                decrypted_password = cipher_suite.decrypt(p.password.encode('utf-8')).decode('utf-8')
                decrypted_passwords.append({"id": p.id, "title": p.title, "username": p.username, "password": decrypted_password})
            except Exception as e:
                print(f"Error decrypting password: {e}")

        return jsonify(decrypted_passwords)

    elif request.method == 'POST':
        title = request.json['title']
        username = request.json['username']
        encrypted_password = cipher_suite.encrypt(request.json['password'].encode('utf-8')).decode('utf-8')
        category = request.json['category']

        new_password = Password(title=title, username=username, password=encrypted_password, category=category)
        db.session.add(new_password)
        db.session.commit()

        return jsonify({"message": "Password added", "id": new_password.id})
        
@app.route('/api/passwords/<int:password_id>', methods=['PUT', 'DELETE'])
def password_detail(password_id):
    password = Password.query.get_or_404(password_id)

    if request.method == 'PUT':
        title = request.json['title']
        username = request.json['username']
        encrypted_password = cipher_suite.encrypt(request.json['password'].encode('utf-8')).decode('utf-8')
        category = request.json['category']

        password.title = title
        password.username = username
        password.password = encrypted_password
        password.category = category

        db.session.commit()
        return jsonify({"message": "Password updated", "id": password.id})

    elif request.method == 'DELETE':
        db.session.delete(password)
        db.session.commit()
        return jsonify({"message": "Password deleted", "id": password.id})


if __name__ == '__main__':
    app.run(debug=True)
