from app import db, bcrypt
from models import Password
from encryption import encrypt_password

def main():
    # Add test data
    passwords = [
        Password(title='Email', username='alice@example.com', password=encrypt_password('password123'), category='Personal'),
        Password(title='Bank Account', username='alice', password=encrypt_password('bankpassword'), category='Work'),
        Password(title='Social Media', username='alice123', password=encrypt_password('socialmediapassword'), category='Personal')
    ]

    for p in passwords:
        db.session.add(p)

    db.session.commit()

if __name__ == '__main__':
    main()
