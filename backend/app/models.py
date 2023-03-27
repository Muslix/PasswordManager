from database import db
from datetime import datetime


class Password(db.Model):
    __tablename__ = 'password'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('passwords', lazy=True))

class PasswordHistory(db.Model):
    __tablename__ = 'password_history'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    password_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }      
    def is_in_use(self):
        # Überprüfen, ob es Passwörter gibt, die auf diese Kategorie verweisen
        if self.passwords:
            return True
        return False

def save_password_history(password_id, title, username, password, category):
    password_history = PasswordHistory(
        password_id=password_id,
        title=title,
        username=username,
        password=password,
        category=category.name,  # Save the id of the category instead of the entire object
        timestamp=datetime.utcnow()
    )
    db.session.add(password_history)
    db.session.commit()