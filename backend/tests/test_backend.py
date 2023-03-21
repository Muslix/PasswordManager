from backend.app import app, db
from backend.models import Password, PasswordHistory, save_password_history
from backend.encryption import encrypt_password, decrypt_password

def test_password_creation(db):
    """Test creating a new password."""
    with app.app_context():
        # Create a new password
        new_password = Password(title='Email', username='alice@example.com', password=encrypt_password('password123'), category='Personal')
        db.session.add(new_password)
        db.session.commit()

        # Check if the new password was added successfully
        assert Password.query.filter_by(title='Email').first() is not None

def test_password_update(db):
    """Test updating an existing password."""
    with app.app_context():
        # Update an existing password
        password = Password.query.filter_by(title='Email').first()
        password.username = 'bob@example.com'
        db.session.commit()

        # Check if the password was updated successfully
        assert Password.query.filter_by(title='Email', username='bob@example.com').first() is not None

def test_password_deletion(db):
    """Test deleting an existing password."""
    with app.app_context():
        # Delete an existing password
        password = Password.query.filter_by(title='Email').first()
        db.session.delete(password)
        db.session.commit()

        # Check if the password was deleted successfully
        assert Password.query.filter_by(title='Email').first() is None

def test_password_history(db):
    """Test saving a password history entry."""
    with app.app_context():
        # Add a new password history entry
        password = Password.query.filter_by(title='Email').first()
        save_password_history(password.id, password.title, password.username, password.password, password.category)

        # Check if the new password history entry was added successfully
        assert PasswordHistory.query.filter_by(password_id=password.id).first() is not None

def test_password_encryption():
    """Test encrypting and decrypting a password."""
    password = 'password123'
    encrypted_password = encrypt_password(password)
    decrypted_password = decrypt_password(encrypted_password)
    assert decrypted_password == password
