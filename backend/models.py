from app import db
from datetime import datetime

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False, default='Personal')

class PasswordHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    password_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False, default='Personal')
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

def save_password_history(password_id, title, username, password, category):
    history_entry = PasswordHistory(
        password_id=password_id,
        title=title,
        username=username,
        password=password,
        category=category
    )
    db.session.add(history_entry)
    db.session.commit()