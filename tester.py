import requests

r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')
print(r.json())