# tests/test_todo.py

import unittest
from todo import add_task, remove_task

class TestTodo(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        add_task(self.tasks, "Test Task")  # Pass the task directly
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0], "Test Task")  # Check if the correct task was added

    def test_remove_task(self):
        self.tasks.append("Test Task")
        remove_task(self.tasks, 0)  # Pass the index directly
        self.assertEqual(len(self.tasks), 0)

if __name__ == "__main__":
    unittest.main()

