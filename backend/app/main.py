import os
from app import create_app

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, '..')  # Gehe ein Verzeichnis höher
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')

if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

app = create_app(BASE_DIR)

if __name__ == '__main__':
    app.run(debug=True)
