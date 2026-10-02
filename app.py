from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

tasks = []

def create_task(task_data):
    task_id = str(uuid4())
    task = {
        "id": task_id,
        "title": task_data["title"],
        "description": task_data["description"],
        "completed": False
    }
    tasks.append(task)
    return task

@app.route("/tasks", methods=["POST"])
def create_task_endpoint():
    task_data = request.get_json()
    task = create_task(task_data)
    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def get_tasks_endpoint():
    return jsonify(tasks)

@app.route("/tasks/<task_id>", methods=["GET"])
def get_task_endpoint(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task_endpoint(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task_data = request.get_json()
    task["title"] = task_data.get("title", task["title"])
    task["description"] = task_data.get("description", task["description"])
    task["completed"] = task_data.get("completed", task["completed"])
    return jsonify(task)

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task_endpoint(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks.remove(task)
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)
