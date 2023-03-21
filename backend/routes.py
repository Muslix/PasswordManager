from flask import request, jsonify
from app import app, db
from models import Password, PasswordHistory, save_password_history
from encryption import encrypt_password, decrypt_password

@app.route('/api/passwords', methods=['GET', 'POST'])
def passwords():
    if request.method == 'GET':
        passwords = Password.query.all()
        decrypted_passwords = []
        for p in passwords:
            decrypted_password = decrypt_password(p.password)
            if decrypted_password:
                decrypted_passwords.append({"id": p.id, "title": p.title, "username": p.username, "password": decrypted_password, "category": p.category})

        return jsonify(decrypted_passwords)

    elif request.method == 'POST':
        title = request.json['title']
        username = request.json['username']
        encrypted_password = encrypt_password(request.json['password'])
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
        encrypted_password = encrypt_password(request.json['password'])
        category = request.json['category']

        save_password_history(password.id, password.username, password.password, password.category)

        password.title = title
        password.username = username
        password.password = encrypted_password
        password.category = category

        db.session.commit()
        return jsonify({"message": "Password updated", "id": password.id})

    elif request.method == 'DELETE':
        save_password_history(password.id, password.username, password.password, password.category)
        db.session.delete(password)
        db.session.commit()
        return jsonify({"message": "Password deleted", "id": password.id})

@app.route('/api/passwords/history', methods=['GET'])
def password_history():
    history_entries = PasswordHistory.query.all()
    decrypted_history = []
    for entry in history_entries:
        decrypted_password = decrypt_password(entry.password)
        if decrypted_password:
            decrypted_history.append({
                "id": entry.id,
                "password_id": entry.password_id,
                "username": entry.username,
                "password": decrypted_password,
                "category": entry.category,
                "timestamp": entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            })

    return jsonify(decrypted_history)
