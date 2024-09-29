import datetime
import json
from dataclasses import asdict

import requests

from lib.db.tasks.dataclass import Task

task = Task(
    name='Написать HTTP запросы',
    description='Написать обработчик и запрос для собственного api приложения',
    priority='medium',
    deadline=datetime.datetime(year=2024, month=9, day=29, hour=10, minute=10).strftime('%Y-%m-%d %H:%M'),
)


test = {
    'name': 'Test',
    'description': 'test description',
    'priority': 'low',
    'deadline': 'bebebe',
}
# expected_keys = ['name', 'description', 'priority', 'deadline']
# test_keys = ['deadline', 'boba', 'biba', 'roba']
# expected_keys_set = set(expected_keys)
# test_keys_set = set(test_keys)
# actual_keys_set = set(test)
#
# if expected_keys_set.intersection(actual_keys_set):
#     print('true')
# print(expected_keys_set, test_keys_set, actual_keys_set, sep='\n')
# e = 0

r = requests.post('http://127.0.0.1:5000/todo/api/tasks', json=test)
print(r.text)
# print(r.json())

