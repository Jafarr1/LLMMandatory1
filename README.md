# Task Management API
================================

## Project Description

This is a minimal Flask REST API for managing tasks using an in-memory list. The API provides endpoints for creating, retrieving, updating, and deleting tasks.

## Prerequisites

* Python 3.8+
* Flask 2.0+
* pip (for installing dependencies)

## Setup Instructions

1. Clone the repository `git clone https://github.com/your-username/task-management-api.git`
2. Install dependencies `pip install -r requirements.txt`
3. Run the application `python app.py`

## How to Run the Application

1. Run the application `python app.py`
2. The API will be accessible at `http://localhost:5000`

## API Endpoints
----------------

### POST /tasks

Creates a new task.

* Request Body:
	+ `title` (string): The title of the task.
	+ `description` (string): The description of the task.
	+ `completed` (boolean): Whether the task is completed.
* Response:
	+ `id` (integer): The ID of the newly created task.

### GET /tasks

Retrieve a list of all tasks.

### GET /tasks/<id>

Retrieve a task by its ID.

* Response:
	+ `id` (integer): The ID of the task.
	+ `title` (string): The title of the task.
	+ `description` (string): The description of the task.
	+ `completed` (boolean): Whether the task is completed.

### PUT /tasks/<id>

Updates a task by its ID.

* Request Body:
	+ `title` (string): The new title of the task.
	+ `description` (string): The new description of the task.
	+ `completed` (boolean): Whether the task is completed (optional).
* Response:
	+ The updated task.

### DELETE /tasks/<id>

Deletes a task by its ID.

* Response:
	+ `status` (string): Whether the task was deleted.

## Example JSON Requests
------------------------

### Create Task

`POST /tasks`
```json
{
  "title": "Create a new task",
  "description": "This is a new task",
  "completed": false
}
```

### Get All Tasks

`GET /tasks`
```json
{}
```

### Get Task with ID 1

`GET /tasks/1`
```json
{
  "id": 1,
  "title": "Create a new task",
  "description": "This is a new task",
  "completed": false
}
```

### Update Task with ID 1

`PUT /tasks/1`
```json
{
  "title": "Updated task title",
  "description": "This is an updated task",
  "completed": true
}
```

### Delete Task with ID 1

`DELETE /tasks/1`
```
{}
```

## How to Run the Tests

`python -m unittest test_app.py -v`

Note: Do not expect tests to currently pass.

## Operational Notes

* The API uses an in-memory list for task storage, which means that tasks will be lost when the application restarts.
* The API does not support authentication or authorization.

## Known Limitations

* The API does not support databases or cloud infrastructure.
* The API does not support authentication or authorization.
* The API uses an in-memory list for task storage, which means that tasks will be lost when the application restarts.