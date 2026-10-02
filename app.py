
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data.get('title'),
        'description': data.get('description'),
        'completed': data.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify({'id': new_task['id']}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        data = request.get_json()
        if 'title' in data:
            task['title'] = data['title']
        if 'description' in data:
            task['description'] = data['description']
        if 'completed' in data:
            task['completed'] = data['completed']
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return jsonify({'status': 'Task deleted'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
