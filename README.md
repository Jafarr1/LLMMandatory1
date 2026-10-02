# Task Management API Documentation

**Overview**

This is a simple Task Management API built using Flask, a lightweight web framework for Python. The API allows users to create, read, update, and delete tasks.

**Requirements**

* Python 3.8+
* Flask 2.0+
* No external dependencies required

**Installation**

1. Clone the repository: `git clone https://github.com/your-username/task-management-api.git`
2. Install Flask: `pip install flask`

**Running the Application**

1. Navigate to the repository directory: `cd task-management-api`
2. Run the application: `python app.py`
3. The application will run on `http://localhost:5000`

**Running Automated Tests**

1. Navigate to the repository directory: `cd task-management-api`
2. Run the automated tests: `python -m unittest test_app.py`

**API Endpoints**

### 1. Create Task

* URL: `/tasks`
* Method: `POST`
* Request Body: `{"title": "string", "description": "string"}`
* Response: `{"id": "string", "title": "string", "description": "string", "completed": false}`

### 2. Get Tasks

* URL: `/tasks`
* Method: `GET`
* Response: `[{"id": "string", "title": "string", "description": "string", "completed": false}]`

### 3. Get Task

* URL: `/tasks/<task_id>`
* Method: `GET`
* Response: `{"id": "string", "title": "string", "description": "string", "completed": false}`

### 4. Update Task

* URL: `/tasks/<task_id>`
* Method: `PUT`
* Request Body: `{"title": "string", "description": "string"}`
* Response: `{"id": "string", "title": "string", "description": "string", "completed": false}`

### 5. Delete Task

* URL: `/tasks/<task_id>`
* Method: `DELETE`
* Response: `{"message": "Task deleted"}`

**Example JSON for Creating a Task**

