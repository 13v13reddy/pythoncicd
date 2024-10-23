# tests/test_app.py

import unittest
from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.app.post('/add', data={'task': 'Test Task'})
        self.assertEqual(response.status_code, 302)  # Redirect to index
        response = self.app.get('/')
        self.assertIn(b'Test Task', response.data)

    def test_remove_task(self):
        self.app.post('/add', data={'task': 'Test Task'})
        response = self.app.post('/remove/0')
        self.assertEqual(response.status_code, 302)  # Redirect to index
        response = self.app.get('/')
        self.assertNotIn(b'Test Task', response.data)

if __name__ == "__main__":
    unittest.main()

