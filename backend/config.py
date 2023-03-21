from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

load_dotenv()

# Generate a Fernet encryption key or use an existing one
key = os.environ.get('FERNET_KEY')
if not key:
    key = Fernet.generate_key()
    os.environ['FERNET_KEY'] = key.decode('utf-8')
