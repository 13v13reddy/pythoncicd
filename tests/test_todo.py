# tests/test_todo.py

import unittest
from todo import add_task, remove_task

class TestTodo(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        add_task(self.tasks)
        self.assertEqual(len(self.tasks), 1)

    def test_remove_task(self):
        self.tasks.append("Test Task")
        remove_task(self.tasks)
        self.assertEqual(len(self.tasks), 0)

if __name__ == "__main__":
    unittest.main()

