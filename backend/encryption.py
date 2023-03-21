from cryptography.fernet import Fernet
from config import key

cipher_suite = Fernet(key)

def encrypt_password(password: str) -> str:
    """Encrypt a password using the Fernet cipher suite."""
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8')).decode('utf-8')
    return encrypted_password

def decrypt_password(encrypted_password: str) -> str:
    """Decrypt an encrypted password using the Fernet cipher suite."""
    try:
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode('utf-8')).decode('utf-8')
        return decrypted_password
    except Exception as e:
        print(f"Error decrypting password: {e}")
        return None
