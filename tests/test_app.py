# test_app.py

import unittest
from app import app, tasks  # Import tasks from the app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        tasks.clear()  # Clear tasks before each test to ensure a clean state

    def test_add_task(self):
        # Test adding a new task
        response = self.app.post('/add', data={'task': 'Another Task'})
        self.assertEqual(response.status_code, 302)  # Redirect after adding
        response = self.app.get('/')
        self.assertIn(b'Another Task', response.data)

    def test_remove_task(self):
        # Add tasks
        self.app.post('/add', data={'task': 'Test Task'})
        self.app.post('/add', data={'task': 'New Task'})

        # Remove the first task ('Test Task' at index 0)
        response = self.app.post('/remove/0')  # Remove the task at index 0
        self.assertEqual(response.status_code, 302)  # Redirect after removing

        # Check that 'Test Task' is no longer in the list
        response = self.app.get('/')
        self.assertNotIn(b'Test Task', response.data)
        self.assertIn(b'New Task', response.data)  # 'New Task' should remain

if __name__ == '__main__':
    unittest.main()

