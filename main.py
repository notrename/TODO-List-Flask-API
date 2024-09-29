from dataclasses import asdict
from datetime import datetime

from flask import Flask, jsonify, request
from sqlalchemy import select, insert

from lib.db.db_controller import async_session_maker
from lib.db.tasks.dataclass import Task
from lib.db.tasks.models import Tasks
from lib.todo_list.checkers import check_body_tasks, check_datetime_fields

app = Flask(__name__)


@app.route('/todo/api/tasks', methods=['GET'])
async def get_tasks():
    async with async_session_maker() as session:
        query = select(Tasks)
        result = await session.execute(query)
        tasks = result.scalars().all()
        return tasks


@app.route('/todo/api/tasks', methods=['POST'])
async def insert_task():
    task = request.get_json(force=True)
    creation_datetime = datetime.now()
    if not check_body_tasks(actual_keys=list(task)):
        return fail_validation(request)
    fields = check_datetime_fields(task)
    if not fields:
        return wrong_format_datetime(request)
    task.update(deadline=fields.get('deadline'), creation_datetime=creation_datetime)
    # async with async_session_maker() as session:
    #     query = insert(Tasks).values(task)
    #     await session.execute(query)
    #     await session.commit()
    return jsonify(task)


@app.errorhandler(404)
def fail_validation(error):
    return jsonify({'Error': 'Unexpected json keys'})


@app.errorhandler(404)
def wrong_format_datetime(error):
    return jsonify({'Error': 'Wrong format datetime in deadline'})


if __name__ == '__main__':
    app.run(debug=True)
