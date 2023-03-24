import unittest
import json
import os
from backend.app import create_app
from backend.app.database import db


class PasswordManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(os.path.abspath(os.path.dirname(__file__)) + "/..")
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_passwords_endpoint(self):
        response = self.client().get('/api/passwords')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
