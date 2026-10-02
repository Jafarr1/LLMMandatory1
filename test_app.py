```python
import unittest
from app import app, tasks

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        tasks.clear()

    def create_task(self, title, description=None, completed=False):
        return self.app.post('/tasks', json={
            'title': title,
            'description': description,
            'completed': completed
        })

    def test_create_task(self):
        response = self.create_task('Test Task')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        task_id = response.json['id']
        tasks.append({
            'id': task_id,
            'title': 'Test Task',
            'description': None,
            'completed': False
        })
        task = next((task for task in tasks if task['id'] == task_id), None)
        self.assertIsNotNone(task)

    def test_get_tasks(self):
        self.create_task('Task 1')
        self.create_task('Task 2')
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(tasks), 2)
        for task in data:
            self.assertIn('id', task)
            self.assertIn('title', task)
            self.assertIn('description', task)
            self.assertIn('completed', task)
            self.assertTrue('id' in tasks)

    def test_get_task(self):
        task_id = self.create_task('Task 1').json['id']
        response = self.app.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertIn('title', data)
        self.assertIn('description', data)
        self.assertIn('completed', data)
        self.assertEqual(data, {
            'id': task_id,
            'title': 'Task 1',
            'description': None,
            'completed': False
        })

    def test_update_task(self):
        task_id = self.create_task('Task 1').json['id']
        response = self.app.put(f'/tasks/{task_id}', json={
            'title': 'Updated Task',
            'description': 'Test description',
            'completed': True
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertIn('title', data)
        self.assertIn('description', data)
        self.assertIn('completed', data)
        self.assertEqual(data, {
            'id': task_id,
            'title': 'Updated Task',
            'description': 'Test description',
            'completed': True
        })

    def test_delete_task(self):
        task_id = self.create_task('Task 1').json['id']
        response = self.app.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.get_json())
        self.assertTrue(not any(task['id'] == task_id for task in tasks))

    def test_get_nonexistent_task(self):
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'error': 'Task not found'})

if __name__ == '__main__':
    unittest.main()
```