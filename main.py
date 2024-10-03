from flask import Flask, jsonify, request
from pydantic import ValidationError

from lib.db.tasks.utils import tasks_get, task_insert, task_delete
from lib.schemas.models import TaskQuery

app = Flask(__name__)


@app.get('/todo/api/tasks')
async def get_tasks():
    tasks = await tasks_get()
    if not tasks:
        return jsonify(None)
    return jsonify(tasks), 200


@app.post('/todo/api/tasks')
async def insert_task():
    task = TaskQuery(**request.get_json())
    info = await task_insert(data=task.dict())
    return jsonify(info), 201


@app.delete('/todo/api/tasks/<task_id>')
async def delete_task(task_id):
    if not task_id.isdigit():
        return jsonify({'error': 'send task id'}), 203
    info = await task_delete(int(task_id))
    return jsonify(info), 202


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify(e.errors()), 422


if __name__ == '__main__':
    app.run(debug=True)
