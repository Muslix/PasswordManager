# services/password_service.py

from database import db
from models import Password, Category, save_password_history
from encryption import encrypt_password

def add_password(title, username, password, category_id):
    encrypted_password = encrypt_password(password)
    category = Category.query.get(category_id)
    new_password = Password(title=title, username=username, password=encrypted_password, category=category)
    db.session.add(new_password)
    db.session.commit()
    return new_password

def update_password(password, title, username, new_password, category_id):
    encrypted_password = encrypt_password(new_password)
    save_password_history(password.id, password.title, password.username, password.password, password.category)
    category = Category.query.get(category_id)  # Get the category object by its id
    password.title = title
    password.username = username
    password.password = encrypted_password
    password.category = category
    db.session.commit()

def delete_password(password):
    save_password_history(password.id, password.title, password.username, password.password, password.category)
    db.session.delete(password)
    db.session.commit()
