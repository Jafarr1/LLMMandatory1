import unittest
from app import app, tasks
from unittest.mock import patch
from flask import jsonify

class TestTaskManagementAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        tasks.clear()

    def test_create_task(self):
        task_data = {"title": "Test Task", "description": "Test description"}
        response = self.app.post("/tasks", json=task_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(tasks), 1)

    def test_get_tasks(self):
        task_data = {"title": "Test Task", "description": "Test description"}
        self.app.post("/tasks", json=task_data)
        response = self.app.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_get_task(self):
        task_data = {"title": "Test Task", "description": "Test description"}
        task_id = self.app.post("/tasks", json=task_data).json["id"]
        response = self.app.get(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["id"], task_id)

    def test_get_nonexistent_task(self):
        task_id = str(uuid4())
        response = self.app.get(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 404)

    def test_update_task(self):
        task_data = {"title": "Test Task", "description": "Test description"}
        task_id = self.app.post("/tasks", json=task_data).json["id"]
        response = self.app.put(f"/tasks/{task_id}", json={"title": "Updated Task"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["title"], "Updated Task")

    def test_delete_task(self):
        task_data = {"title": "Test Task", "description": "Test description"}
        task_id = self.app.post("/tasks", json=task_data).json["id"]
        response = self.app.delete(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()
