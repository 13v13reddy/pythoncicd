import unittest
from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Add initial tasks to ensure predictable state
        self.app.post('/add', data={'task': 'Test Task'})
        self.app.post('/add', data={'task': 'New Task'})

    def test_add_task(self):
        # Test adding a new task
        response = self.app.post('/add', data={'task': 'Another Task'})
        self.assertEqual(response.status_code, 302)  # Redirect after adding
        response = self.app.get('/')
        self.assertIn(b'Another Task', response.data)

    def test_remove_task(self):
        # Test removing the first task ('Test Task' at index 0)
        response = self.app.post('/remove/0')  # Removing the first task
        self.assertEqual(response.status_code, 302)  # Redirect after removing

        # Check that 'Test Task' is no longer in the list
        response = self.app.get('/')
        self.assertNotIn(b'Test Task', response.data)

        # Check that 'New Task' still exists
        self.assertIn(b'New Task', response.data)

if __name__ == '__main__':
    unittest.main()

