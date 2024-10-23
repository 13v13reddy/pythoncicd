import unittest
from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Add a test task
        self.app.post('/add', data={'task': 'Test Task'})

    def test_add_task(self):
        response = self.app.post('/add', data={'task': 'New Task'})
        self.assertEqual(response.status_code, 302)  # Redirect after adding
        response = self.app.get('/')
        self.assertIn(b'New Task', response.data)

    def test_remove_task(self):
        # Remove the task that was added during setup
        response = self.app.post('/remove/0')
        self.assertEqual(response.status_code, 302)  # Redirect after removing
        response = self.app.get('/')
        self.assertNotIn(b'Test Task', response.data)

if __name__ == '__main__':
    unittest.main()

