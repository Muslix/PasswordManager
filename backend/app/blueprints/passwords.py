from flask import request, jsonify
from models import Password, PasswordHistory, Category  
from encryption import decrypt_password
from services.password_service import add_password, update_password, delete_password
from . import api_blueprint



@api_blueprint.route('/passwords', methods=['GET', 'POST'])
def passwords():
    if request.method == 'GET':
        passwords = Password.query.all()
        decrypted_passwords = []
        for p in passwords:
            decrypted_password = decrypt_password(p.password)
            if decrypted_password:
                decrypted_passwords.append({"id": p.id, "title": p.title, "username": p.username, "password": decrypted_password, "category": p.category.to_dict() if p.category else None})

        return jsonify(decrypted_passwords)

    elif request.method == 'POST':
        title = request.json['title']
        username = request.json['username']
        password = request.json['password']
        category_id  = request.json['category_id']

        new_password = add_password(title, username, password, category_id )
        return jsonify({"message": "Password added", "id": new_password.id})

@api_blueprint.route('/passwords/<int:password_id>', methods=['PUT', 'DELETE'])
def password_detail(password_id):
    password = Password.query.get_or_404(password_id)

    if request.method == 'PUT':
        title = request.json['title']
        username = request.json['username']
        new_password = request.json['password']
        category_id  = request.json['category_id']

        update_password(password, title, username, new_password, category_id )
        return jsonify({"message": "Password updated", "id": password.id})

    elif request.method == 'DELETE':
        delete_password(password)
        return jsonify({"message": "Password deleted", "id": password.id})

@api_blueprint.route('/passwords/history', methods=['GET'])
def password_history():
    history_entries = PasswordHistory.query.all()
    decrypted_history = []
    for entry in history_entries:
        decrypted_password = decrypt_password(entry.password)
        if decrypted_password:
            decrypted_history.append({
                "id": entry.id,
                "title": entry.title,
                "password_id": entry.password_id,
                "username": entry.username,
                "password": decrypted_password,
                "category": entry.category,
                "timestamp": entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            })

    return jsonify(decrypted_history)