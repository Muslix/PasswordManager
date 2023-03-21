# Password Manager

Ein einfacher, sicherer und benutzerfreundlicher Passwort-Manager, der auf Flask (Backend) und Vue.js (Frontend) basiert. Mit dieser Anwendung können Sie Passwörter speichern, anzeigen, bearbeiten und löschen.

## Funktionen

- Passwortliste nach Kategorien (z. B. Arbeit, Soziales, Persönliches, Sonstiges)
- Anzeigen, Bearbeiten und Löschen von Passwörtern
- Passwortstärkeanzeige
- Passwortverlauf
- Datenverschlüsselung

## Installation

Stellen Sie sicher, dass Sie Python, Node.js und npm auf Ihrem Computer installiert haben, bevor Sie fortfahren.

1. Klonen Sie das Repository:

```
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```


2. Erstellen Sie eine virtuelle Umgebung und aktivieren Sie sie:

```
python -m venv venv
source venv/bin/activate # Für Linux/macOS
.\venv\Scripts\activate # Für Windows
```

3. Installieren Sie die erforderlichen Python-Pakete:

```
pip install -r requirements.txt
```


4. Navigieren Sie zum Frontend-Verzeichnis und installieren Sie die erforderlichen JavaScript-Pakete:

```
cd frontend
npm install
```


5. Erstellen Sie eine `.env` Datei im Hauptverzeichnis des Projekts und fügen Sie einen FERNET_KEY hinzu:

```
FERNET_KEY=IhrFernetSchlüsselHier
```


Sie können einen Fernet-Schlüssel mit dem folgenden Python-Skript generieren:

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())
```
6. Initialisieren Sie die Datenbank, indem Sie die create_db.py Datei ausführen:

```
python create_db.py
```

## Initialisierung

1. Starten Sie den Flask-Server im Hauptverzeichnis der Anwendung:

```
export FLASK_APP=app.py # Für Linux/macOS
set FLASK_APP=app.py # Für Windows
flask run
```


2. Starten Sie den Vue.js-Server im Frontend-Verzeichnis:

```
cd frontend
npm run serve
```


3. Öffnen Sie Ihren Webbrowser und navigieren Sie zu `http://localhost:8080`, um die Anwendung zu verwenden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.



### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
